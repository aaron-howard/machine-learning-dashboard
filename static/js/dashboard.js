// ML Dashboard JavaScript
class MLDashboard {
    constructor() {
        this.modelType = null;
        this.isRealTimeEnabled = true;
        this.updateInterval = null;
        this.performanceHistory = [];
        this.predictionsData = null;
        
        this.initializeEventListeners();
        this.initializeCharts();
    }

    initializeEventListeners() {
        // Training buttons
        document.getElementById('train-classification').addEventListener('click', () => {
            this.trainModel('classification');
        });

        document.getElementById('train-regression').addEventListener('click', () => {
            this.trainModel('regression');
        });

        // Real-time toggle
        document.getElementById('real-time-toggle').addEventListener('change', (e) => {
            this.toggleRealTime(e.target.checked);
        });
    }

    async trainModel(type) {
        this.showLoadingModal();
        this.showStatusMessage(`Training ${type} model...`, 'info');

        try {
            const response = await fetch(`/api/train/${type}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            const result = await response.json();
            
            if (result.status === 'success') {
                this.modelType = type;
                this.showStatusMessage(`Model trained successfully!`, 'success');
                this.hideLoadingModal();
                this.loadModelInfo();
                this.loadPerformanceMetrics();
                this.loadPredictions();
                this.showDashboardSections();
                this.startRealTimeUpdates();
            } else {
                throw new Error(result.message);
            }
        } catch (error) {
            this.hideLoadingModal();
            this.showStatusMessage(`Error: ${error.message}`, 'danger');
        }
    }

    async loadModelInfo() {
        try {
            const response = await fetch('/api/model/info');
            const result = await response.json();
            
            if (result.status === 'success') {
                this.displayModelInfo(result);
            }
        } catch (error) {
            console.error('Error loading model info:', error);
        }
    }

    displayModelInfo(data) {
        const modelDetails = document.getElementById('model-details');
        modelDetails.innerHTML = `
            <div class="col-md-3">
                <div class="metric-card">
                    <div class="metric-value">${data.model_type}</div>
                    <div class="metric-label">Model Type</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="metric-card">
                    <div class="metric-value">${data.total_params.toLocaleString()}</div>
                    <div class="metric-label">Total Parameters</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="metric-card">
                    <div class="metric-value">${data.layers.length}</div>
                    <div class="metric-label">Layers</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="metric-card">
                    <div class="metric-value">${this.getModelSize(data.total_params)}</div>
                    <div class="metric-label">Model Size</div>
                </div>
            </div>
        `;
    }

    getModelSize(paramCount) {
        const sizeInMB = (paramCount * 4) / (1024 * 1024); // Assuming float32
        return sizeInMB < 1 ? `${(sizeInMB * 1024).toFixed(0)} KB` : `${sizeInMB.toFixed(1)} MB`;
    }

    async loadPerformanceMetrics() {
        try {
            const response = await fetch('/api/performance');
            const result = await response.json();
            
            if (result.status === 'success') {
                this.displayPerformanceMetrics(result.metrics);
                this.updatePerformanceTrend(result.metrics);
            }
        } catch (error) {
            console.error('Error loading performance metrics:', error);
        }
    }

    displayPerformanceMetrics(metrics) {
        const metricsCards = document.getElementById('metrics-cards');
        let metricsHTML = '';

        if (this.modelType === 'classification') {
            metricsHTML = `
                <div class="col-md-3">
                    <div class="metric-card">
                        <div class="metric-value">${(metrics.accuracy * 100).toFixed(1)}%</div>
                        <div class="metric-label">Accuracy</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="metric-card">
                        <div class="metric-value">${(metrics.precision * 100).toFixed(1)}%</div>
                        <div class="metric-label">Precision</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="metric-card">
                        <div class="metric-value">${(metrics.recall * 100).toFixed(1)}%</div>
                        <div class="metric-label">Recall</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="metric-card">
                        <div class="metric-value">${(metrics.f1_score * 100).toFixed(1)}%</div>
                        <div class="metric-label">F1 Score</div>
                    </div>
                </div>
            `;
        } else {
            metricsHTML = `
                <div class="col-md-3">
                    <div class="metric-card">
                        <div class="metric-value">${metrics.rmse.toFixed(3)}</div>
                        <div class="metric-label">RMSE</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="metric-card">
                        <div class="metric-value">${metrics.mae.toFixed(3)}</div>
                        <div class="metric-label">MAE</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="metric-card">
                        <div class="metric-value">${(metrics.r2_score * 100).toFixed(1)}%</div>
                        <div class="metric-label">R² Score</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="metric-card">
                        <div class="metric-value">${metrics.mse.toFixed(3)}</div>
                        <div class="metric-label">MSE</div>
                    </div>
                </div>
            `;
        }

        metricsCards.innerHTML = metricsHTML;
    }

    async loadPredictions() {
        try {
            const response = await fetch('/api/predictions?n=20');
            const result = await response.json();
            
            if (result.status === 'success') {
                this.predictionsData = result.predictions;
                this.displayPredictionsTable(result.predictions);
                this.updatePredictionsScatter(result.predictions);
            }
        } catch (error) {
            console.error('Error loading predictions:', error);
        }
    }

    displayPredictionsTable(predictions) {
        const tbody = document.querySelector('#predictions-table tbody');
        tbody.innerHTML = '';

        predictions.actual.forEach((actual, index) => {
            const predicted = predictions.predicted[index];
            const confidence = predictions.confidence[index];
            const isCorrect = actual === predicted;
            
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${predictions.indices[index]}</td>
                <td>${actual}</td>
                <td>${predicted}</td>
                <td>
                    <div class="progress" style="height: 20px;">
                        <div class="progress-bar ${isCorrect ? 'bg-success' : 'bg-danger'}" 
                             style="width: ${(confidence * 100).toFixed(1)}%">
                            ${(confidence * 100).toFixed(1)}%
                        </div>
                    </div>
                </td>
                <td>
                    <span class="${isCorrect ? 'status-correct' : 'status-incorrect'}">
                        <i class="fas fa-${isCorrect ? 'check' : 'times'}"></i>
                        ${isCorrect ? 'Correct' : 'Incorrect'}
                    </span>
                </td>
            `;
            tbody.appendChild(row);
        });
    }

    initializeCharts() {
        this.initializePerformanceTrendChart();
        this.initializePredictionsScatterChart();
    }

    initializePerformanceTrendChart() {
        const container = d3.select('#performance-trend-chart');
        container.selectAll('*').remove();

        const margin = { top: 20, right: 30, bottom: 40, left: 50 };
        const width = container.node().offsetWidth - margin.left - margin.right;
        const height = 350 - margin.top - margin.bottom;

        const svg = container
            .append('svg')
            .attr('width', width + margin.left + margin.right)
            .attr('height', height + margin.top + margin.bottom);

        const g = svg
            .append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);

        // Add axes
        g.append('g')
            .attr('class', 'x-axis')
            .attr('transform', `translate(0,${height})`);

        g.append('g')
            .attr('class', 'y-axis');

        g.append('text')
            .attr('class', 'axis-label')
            .attr('transform', 'rotate(-90)')
            .attr('y', 0 - margin.left)
            .attr('x', 0 - (height / 2))
            .attr('dy', '1em')
            .style('text-anchor', 'middle')
            .text('Performance');

        g.append('text')
            .attr('class', 'axis-label')
            .attr('transform', `translate(${width / 2}, ${height + margin.bottom - 10})`)
            .style('text-anchor', 'middle')
            .text('Time');

        this.performanceChart = { svg, g, width, height, margin };
    }

    updatePerformanceTrend(metrics) {
        if (!this.performanceChart) return;

        this.performanceHistory.push({
            ...metrics,
            timestamp: new Date(metrics.timestamp)
        });

        // Keep only last 50 data points
        if (this.performanceHistory.length > 50) {
            this.performanceHistory.shift();
        }

        const { g, width, height } = this.performanceChart;
        const metricKey = this.modelType === 'classification' ? 'accuracy' : 'r2_score';
        
        const xScale = d3.scaleTime()
            .domain(d3.extent(this.performanceHistory, d => d.timestamp))
            .range([0, width]);

        const yScale = d3.scaleLinear()
            .domain([0, 1])
            .range([height, 0]);

        // Update axes
        g.select('.x-axis')
            .call(d3.axisBottom(xScale).tickFormat(d3.timeFormat('%H:%M:%S')));

        g.select('.y-axis')
            .call(d3.axisLeft(yScale).tickFormat(d3.format('.2f')));

        // Create line generator
        const line = d3.line()
            .x(d => xScale(d.timestamp))
            .y(d => yScale(d[metricKey]))
            .curve(d3.curveMonotoneX);

        // Update or create line
        let path = g.select('.performance-line');
        if (path.empty()) {
            path = g.append('path')
                .attr('class', 'performance-line')
                .attr('fill', 'none')
                .attr('stroke', '#667eea')
                .attr('stroke-width', 3);
        }

        path.datum(this.performanceHistory)
            .attr('d', line);

        // Add circles for data points
        const circles = g.selectAll('.data-point')
            .data(this.performanceHistory);

        circles.exit().remove();

        circles.enter()
            .append('circle')
            .attr('class', 'data-point circle')
            .attr('r', 4)
            .attr('fill', '#667eea')
            .merge(circles)
            .attr('cx', d => xScale(d.timestamp))
            .attr('cy', d => yScale(d[metricKey]));
    }

    initializePredictionsScatterChart() {
        const container = d3.select('#predictions-scatter-chart');
        container.selectAll('*').remove();

        const margin = { top: 20, right: 20, bottom: 40, left: 40 };
        const width = container.node().offsetWidth - margin.left - margin.right;
        const height = 300 - margin.top - margin.bottom;

        const svg = container
            .append('svg')
            .attr('width', width + margin.left + margin.right)
            .attr('height', height + margin.top + margin.bottom);

        const g = svg
            .append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);

        // Add axes
        g.append('g')
            .attr('class', 'x-axis')
            .attr('transform', `translate(0,${height})`);

        g.append('g')
            .attr('class', 'y-axis');

        g.append('text')
            .attr('class', 'axis-label')
            .attr('transform', 'rotate(-90)')
            .attr('y', 0 - margin.left)
            .attr('x', 0 - (height / 2))
            .attr('dy', '1em')
            .style('text-anchor', 'middle')
            .text('Predicted');

        g.append('text')
            .attr('class', 'axis-label')
            .attr('transform', `translate(${width / 2}, ${height + margin.bottom - 10})`)
            .style('text-anchor', 'middle')
            .text('Actual');

        this.scatterChart = { svg, g, width, height, margin };
    }

    updatePredictionsScatter(predictions) {
        if (!this.scatterChart || !predictions) return;

        const { g, width, height } = this.scatterChart;
        
        const xScale = d3.scaleLinear()
            .domain(d3.extent(predictions.actual))
            .range([0, width]);

        const yScale = d3.scaleLinear()
            .domain(d3.extent(predictions.predicted))
            .range([height, 0]);

        // Update axes
        g.select('.x-axis')
            .call(d3.axisBottom(xScale));

        g.select('.y-axis')
            .call(d3.axisLeft(yScale));

        // Create data points
        const data = predictions.actual.map((actual, i) => ({
            actual,
            predicted: predictions.predicted[i],
            confidence: predictions.confidence[i],
            correct: actual === predictions.predicted[i]
        }));

        // Clear existing points
        g.selectAll('.scatter-point').remove();

        // Add points
        g.selectAll('.scatter-point')
            .data(data)
            .enter()
            .append('circle')
            .attr('class', 'scatter-point circle')
            .attr('cx', d => xScale(d.actual))
            .attr('cy', d => yScale(d.predicted))
            .attr('r', d => 3 + d.confidence * 3)
            .attr('fill', d => d.correct ? '#28a745' : '#dc3545')
            .attr('opacity', 0.7)
            .on('mouseover', function(event, d) {
                d3.select(this).attr('r', 6);
            })
            .on('mouseout', function(event, d) {
                d3.select(this).attr('r', 3 + d.confidence * 3);
            });

        // Add perfect prediction line
        const minVal = Math.min(...predictions.actual, ...predictions.predicted);
        const maxVal = Math.max(...predictions.actual, ...predictions.predicted);
        
        g.append('line')
            .attr('class', 'perfect-line')
            .attr('x1', xScale(minVal))
            .attr('y1', yScale(minVal))
            .attr('x2', xScale(maxVal))
            .attr('y2', yScale(maxVal))
            .attr('stroke', '#666')
            .attr('stroke-width', 2)
            .attr('stroke-dasharray', '5,5');
    }

    showDashboardSections() {
        document.getElementById('model-info-section').style.display = 'block';
        document.getElementById('performance-section').style.display = 'block';
        document.getElementById('charts-section').style.display = 'block';
        document.getElementById('predictions-table-section').style.display = 'block';
    }

    showLoadingModal() {
        const modal = new bootstrap.Modal(document.getElementById('loadingModal'));
        modal.show();
    }

    hideLoadingModal() {
        const modal = bootstrap.Modal.getInstance(document.getElementById('loadingModal'));
        if (modal) {
            modal.hide();
        }
    }

    showStatusMessage(message, type) {
        const statusDiv = document.getElementById('status-message');
        const statusText = document.getElementById('status-text');
        
        statusDiv.className = `alert alert-${type}`;
        statusText.textContent = message;
        statusDiv.style.display = 'block';

        // Auto-hide after 5 seconds
        setTimeout(() => {
            statusDiv.style.display = 'none';
        }, 5000);
    }

    toggleRealTime(enabled) {
        this.isRealTimeEnabled = enabled;
        
        if (enabled && this.modelType) {
            this.startRealTimeUpdates();
        } else {
            this.stopRealTimeUpdates();
        }
    }

    startRealTimeUpdates() {
        if (!this.isRealTimeEnabled || !this.modelType) return;

        this.stopRealTimeUpdates(); // Clear any existing interval
        
        this.updateInterval = setInterval(() => {
            this.loadPerformanceMetrics();
            this.loadPredictions();
        }, 5000); // Update every 5 seconds
    }

    stopRealTimeUpdates() {
        if (this.updateInterval) {
            clearInterval(this.updateInterval);
            this.updateInterval = null;
        }
    }
}

// Initialize dashboard when page loads
document.addEventListener('DOMContentLoaded', () => {
    window.mlDashboard = new MLDashboard();
});

// Handle window resize
window.addEventListener('resize', () => {
    if (window.mlDashboard) {
        // Reinitialize charts on resize
        window.mlDashboard.initializeCharts();
        if (window.mlDashboard.predictionsData) {
            window.mlDashboard.updatePredictionsScatter(window.mlDashboard.predictionsData);
        }
    }
});
