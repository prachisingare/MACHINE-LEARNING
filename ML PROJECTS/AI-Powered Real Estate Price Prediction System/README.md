# 🏠 AI-Powered Real Estate Price Prediction System

A complete Machine Learning and Flask-based web application for predicting housing prices. The system trains multiple regression models, evaluates their performance, and serves predictions through an interactive web interface.

# 🚀 Features

# 📊 Model Training & Evaluation

Implements 13 regression algorithms:
Linear, Ridge, Lasso, ElasticNet, Robust, Polynomial, SGD, ANN (MLP), Random Forest, SVM, LightGBM, XGBoost, KNN.

Evaluates models using MAE, MSE, R².

Saves trained models as .pkl files and logs performance in model_evaluation_results.csv.

# 🌐 Flask Web Application

User-friendly input form for features:

Avg. Area Income

Avg. Area House Age

Avg. Area Number of Rooms

Avg. Area Number of Bedrooms

Area Population

Predicts house prices using selected ML model.

Displays evaluation results in a dynamic HTML table.

# 🛠 Modular Codebase

regression_model.py → Training & evaluation.

app.py → Flask app for model inference & dashboards.

