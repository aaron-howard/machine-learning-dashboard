from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import pandas as pd
import json
import os
from datetime import datetime, timedelta
import random
import threading
import time
from sklearn.datasets import make_classification, make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

app = Flask(__name__)
CORS(app)

# Global variables for model and data
model = None
X_test = None
y_test = None
scaler = None
model_type = None
performance_history = []
prediction_history = []

class MLModelManager:
    def __init__(self):
        self.model = None
        self.model_type = None
        self.scaler = StandardScaler()
        self.X_test = None
        self.y_test = None
        self.performance_history = []
        self.prediction_history = []
        
    def create_classification_model(self):
        """Create and train a classification model"""
        # Generate sample data
        X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, 
                                 n_redundant=5, n_classes=3, random_state=42)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Create and train model
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(20,)),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(3, activation='softmax')
        ])
        
        self.model.compile(optimizer='adam',
                          loss='sparse_categorical_crossentropy',
                          metrics=['accuracy'])
        
        # Train model
        history = self.model.fit(X_train_scaled, y_train, 
                               epochs=50, batch_size=32, 
                               validation_split=0.2, verbose=0)
        
        # Store test data
        self.X_test = X_test_scaled
        self.y_test = y_test
        self.model_type = 'classification'
        
        return history.history
    
    def create_regression_model(self):
        """Create and train a regression model"""
        # Generate sample data
        X, y = make_regression(n_samples=1000, n_features=20, noise=0.1, random_state=42)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Create and train model
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(20,)),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(1)
        ])
        
        self.model.compile(optimizer='adam', loss='mse', metrics=['mae'])
        
        # Train model
        history = self.model.fit(X_train_scaled, y_train, 
                               epochs=50, batch_size=32, 
                               validation_split=0.2, verbose=0)
        
        # Store test data
        self.X_test = X_test_scaled
        self.y_test = y_test
        self.model_type = 'regression'
        
        return history.history
    
    def get_performance_metrics(self):
        """Calculate current performance metrics"""
        if self.model is None or self.X_test is None:
            return None
            
        predictions = self.model.predict(self.X_test, verbose=0)
        
        if self.model_type == 'classification':
            y_pred = np.argmax(predictions, axis=1)
            metrics = {
                'accuracy': float(accuracy_score(self.y_test, y_pred)),
                'precision': float(precision_score(self.y_test, y_pred, average='weighted')),
                'recall': float(recall_score(self.y_test, y_pred, average='weighted')),
                'f1_score': float(f1_score(self.y_test, y_pred, average='weighted'))
            }
        else:  # regression
            y_pred = predictions.flatten()
            metrics = {
                'mse': float(mean_squared_error(self.y_test, y_pred)),
                'rmse': float(np.sqrt(mean_squared_error(self.y_test, y_pred))),
                'r2_score': float(r2_score(self.y_test, y_pred)),
                'mae': float(np.mean(np.abs(self.y_test - y_pred)))
            }
        
        return metrics
    
    def get_predictions_sample(self, n=10):
        """Get a sample of predictions for visualization"""
        if self.model is None or self.X_test is None:
            return None
            
        # Get random sample
        indices = np.random.choice(len(self.X_test), min(n, len(self.X_test)), replace=False)
        sample_X = self.X_test[indices]
        sample_y = self.y_test[indices]
        
        predictions = self.model.predict(sample_X, verbose=0)
        
        if self.model_type == 'classification':
            y_pred = np.argmax(predictions, axis=1)
            confidence = np.max(predictions, axis=1)
        else:
            y_pred = predictions.flatten()
            confidence = np.ones_like(y_pred)  # Placeholder for regression
        
        return {
            'actual': sample_y.tolist(),
            'predicted': y_pred.tolist(),
            'confidence': confidence.tolist(),
            'indices': indices.tolist()
        }

# Initialize model manager
ml_manager = MLModelManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/train/classification', methods=['POST'])
def train_classification():
    """Train a classification model"""
    try:
        history = ml_manager.create_classification_model()
        return jsonify({
            'status': 'success',
            'message': 'Classification model trained successfully',
            'history': history
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/train/regression', methods=['POST'])
def train_regression():
    """Train a regression model"""
    try:
        history = ml_manager.create_regression_model()
        return jsonify({
            'status': 'success',
            'message': 'Regression model trained successfully',
            'history': history
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/performance', methods=['GET'])
def get_performance():
    """Get current model performance metrics"""
    try:
        metrics = ml_manager.get_performance_metrics()
        if metrics is None:
            return jsonify({'status': 'error', 'message': 'No model trained yet'}), 400
        
        # Add timestamp
        metrics['timestamp'] = datetime.now().isoformat()
        
        # Store in history
        ml_manager.performance_history.append(metrics)
        if len(ml_manager.performance_history) > 100:  # Keep last 100 records
            ml_manager.performance_history.pop(0)
        
        return jsonify({
            'status': 'success',
            'metrics': metrics,
            'model_type': ml_manager.model_type
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/predictions', methods=['GET'])
def get_predictions():
    """Get sample predictions for visualization"""
    try:
        n = request.args.get('n', 10, type=int)
        predictions = ml_manager.get_predictions_sample(n)
        if predictions is None:
            return jsonify({'status': 'error', 'message': 'No model trained yet'}), 400
        
        return jsonify({
            'status': 'success',
            'predictions': predictions,
            'model_type': ml_manager.model_type
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/history/performance', methods=['GET'])
def get_performance_history():
    """Get performance history for trend visualization"""
    try:
        return jsonify({
            'status': 'success',
            'history': ml_manager.performance_history
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/model/info', methods=['GET'])
def get_model_info():
    """Get model information and architecture"""
    try:
        if ml_manager.model is None:
            return jsonify({'status': 'error', 'message': 'No model trained yet'}), 400
        
        # Get model summary
        summary = []
        for layer in ml_manager.model.layers:
            summary.append({
                'name': layer.name,
                'type': layer.__class__.__name__,
                'output_shape': str(layer.output_shape),
                'param_count': layer.count_params()
            })
        
        return jsonify({
            'status': 'success',
            'model_type': ml_manager.model_type,
            'total_params': ml_manager.model.count_params(),
            'layers': summary
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def simulate_real_time_data():
    """Simulate real-time data updates"""
    while True:
        if ml_manager.model is not None:
            # Add some noise to simulate real-time performance changes
            metrics = ml_manager.get_performance_metrics()
            if metrics:
                # Add small random variations
                for key in metrics:
                    if key != 'timestamp':
                        noise = random.uniform(-0.01, 0.01)
                        metrics[key] = max(0, min(1, metrics[key] + noise))
                
                metrics['timestamp'] = datetime.now().isoformat()
                ml_manager.performance_history.append(metrics.copy())
                
                # Keep only last 100 records
                if len(ml_manager.performance_history) > 100:
                    ml_manager.performance_history.pop(0)
        
        time.sleep(5)  # Update every 5 seconds

# Start real-time data simulation in background
real_time_thread = threading.Thread(target=simulate_real_time_data, daemon=True)
real_time_thread.start()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
