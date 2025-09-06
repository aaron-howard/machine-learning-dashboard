# 🤖 Machine Learning Dashboard

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3%2B-green.svg)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20%2B-orange.svg)](https://tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI/CD](https://github.com/your-username/machine-learning-dashboard/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/your-username/machine-learning-dashboard/actions)

A comprehensive web-based dashboard for visualizing machine learning model performance and predictions with interactive charts and real-time data updates.

![ML Dashboard Screenshot](https://via.placeholder.com/800x400/667eea/ffffff?text=ML+Dashboard+Preview)

## ✨ Features

- **🚀 Interactive Model Training**: Train classification and regression models using TensorFlow
- **📊 Real-time Performance Monitoring**: Live updates of model performance metrics
- **📈 Interactive Visualizations**: D3.js powered charts for performance trends and predictions
- **📱 Responsive Design**: Bootstrap-based UI that works on all devices
- **🔍 Model Information**: Detailed model architecture and parameter information
- **🎯 Predictions Analysis**: Visual comparison of actual vs predicted values
- **⚡ Real-time Updates**: Automatic data refresh every 5 seconds

## 🚀 Quick Start

### Option 1: One-Click Start (Windows)
```bash
start_dashboard.bat
```

### Option 2: Cross-Platform
```bash
python run.py
```

### Option 3: Direct Flask
```bash
python app.py
```

Then open your browser to: **http://localhost:5000**

## 📋 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

## Technologies Used

- **Backend**: Python, Flask, TensorFlow
- **Frontend**: HTML5, Bootstrap 5, D3.js
- **Data Processing**: NumPy, Pandas, Scikit-learn
- **Visualization**: D3.js, Matplotlib, Seaborn
- **Real-time Updates**: JavaScript polling

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Node.js (optional, for frontend dependencies)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd machine-learning-dashboard
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install frontend dependencies (optional)**
   ```bash
   npm install
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## Usage

### Training Models

1. **Classification Model**
   - Click "Train Classification" to train a neural network for multi-class classification
   - The model will be trained on synthetic data with 3 classes
   - Performance metrics include accuracy, precision, recall, and F1-score

2. **Regression Model**
   - Click "Train Regression" to train a neural network for regression tasks
   - The model will be trained on synthetic regression data
   - Performance metrics include RMSE, MAE, R² score, and MSE

### Viewing Results

- **Model Information**: View model type, parameter count, and architecture details
- **Performance Metrics**: Real-time display of current model performance
- **Performance Trend**: Interactive line chart showing performance over time
- **Predictions vs Actual**: Scatter plot comparing predicted vs actual values
- **Sample Predictions**: Table showing individual predictions with confidence scores

### Real-time Updates

- Toggle real-time updates on/off using the switch in the control panel
- When enabled, the dashboard automatically refreshes data every 5 seconds
- Performance metrics and predictions are updated in real-time

## API Endpoints

### Model Training
- `POST /api/train/classification` - Train a classification model
- `POST /api/train/regression` - Train a regression model

### Model Information
- `GET /api/model/info` - Get model architecture and information

### Performance Data
- `GET /api/performance` - Get current performance metrics
- `GET /api/history/performance` - Get performance history for trends

### Predictions
- `GET /api/predictions?n=10` - Get sample predictions (n = number of samples)

## Project Structure

```
machine-learning-dashboard/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── package.json          # Node.js dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── css/
    │   └── dashboard.css # Custom styles
    ├── js/
    │   └── dashboard.js  # Main JavaScript application
    └── images/           # Static images
```

## Customization

### Adding New Model Types

1. Add a new training method in `MLModelManager` class
2. Create corresponding API endpoint in Flask app
3. Update frontend to handle new model type
4. Add appropriate visualizations

### Modifying Visualizations

- Edit `static/js/dashboard.js` to modify D3.js charts
- Update `static/css/dashboard.css` for styling changes
- Modify chart data processing in the JavaScript class methods

### Adding New Metrics

1. Update the `get_performance_metrics()` method in `MLModelManager`
2. Modify the `displayPerformanceMetrics()` method in JavaScript
3. Update the performance trend chart to include new metrics

## Troubleshooting

### Common Issues

1. **Port already in use**
   - Change the port in `app.py` (line with `app.run()`)
   - Or kill the process using the port

2. **Module not found errors**
   - Ensure virtual environment is activated
   - Reinstall requirements: `pip install -r requirements.txt`

3. **Charts not displaying**
   - Check browser console for JavaScript errors
   - Ensure D3.js is loading correctly
   - Verify data is being returned from API endpoints

4. **Real-time updates not working**
   - Check if real-time toggle is enabled
   - Verify browser allows automatic refresh
   - Check network tab for API call failures

### Performance Optimization

- For large datasets, consider implementing pagination
- Use WebSockets instead of polling for better real-time performance
- Implement data caching for frequently accessed metrics
- Add data compression for large prediction datasets

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Quick Contribution Guide

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add some amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/machine-learning-dashboard.git
cd machine-learning-dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python test_installation.py
```

## 📊 Project Status

![GitHub last commit](https://img.shields.io/github/last-commit/your-username/machine-learning-dashboard)
![GitHub issues](https://img.shields.io/github/issues/your-username/machine-learning-dashboard)
![GitHub pull requests](https://img.shields.io/github/issues-pr/your-username/machine-learning-dashboard)
![GitHub stars](https://img.shields.io/github/stars/your-username/machine-learning-dashboard?style=social)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions or issues, please create an issue in the repository or contact the development team.

---

**Developed by Aaron**  
*ServiceNow Administrator/Developer & PagerDuty Administrator/Developer*  
*City of Dallas*
