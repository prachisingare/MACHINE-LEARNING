# 🥑 Avocado Price Prediction

This project focuses on predicting the average price of avocados using machine learning techniques. The dataset contains historical sales, pricing, and region-wise avocado consumption details. The workflow includes Exploratory Data Analysis (EDA), regression modeling, and model comparison to identify the best-performing algorithm.

# 📂 Project Structure

EDA.ipynb → Exploratory Data Analysis of avocado dataset

Data cleaning and preprocessing

Visualization of trends (yearly, region-wise, type-wise)

Insights into demand and price variations

Price Regression.ipynb → Building regression models

Feature engineering

Training linear regression and other models

Model evaluation (MAE, RMSE, R² Score)

comparison-of-models.ipynb → Comparing multiple algorithms

Linear Regression, Decision Tree, Random Forest, XGBoost, etc.

Performance benchmarking

Selection of the best model for deployment

# 📊 Dataset

The dataset consists of the following key columns:

Date → Date of observation

AveragePrice → Average avocado price (target variable)

Total Volume → Total sales volume

Total Bags → Number of bags sold

Small/Large/XLarge Bags → Distribution of bag sizes

Type → Avocado type (conventional or organic)

Year → Year of observation

Region → US region of sales

# ⚙️ Technologies Used

Python 3

Pandas & NumPy → Data preprocessing

Matplotlib & Seaborn → Data visualization

Scikit-learn → Regression models, metrics

XGBoost / Random Forest → Advanced ML algorithms

Jupyter Notebook → Interactive development

# 🚀 Workflow

Data Preprocessing

Handle missing values

Feature encoding (Type, Region)

Train-test split

Exploratory Data Analysis

Distribution of avocado prices

Yearly and regional trends

Type-wise price variations

Model Training & Evaluation

Train multiple regression models

Evaluate using metrics (MAE, RMSE, R²)

Compare results to select the best model

Results

Insights into pricing trends

Best model chosen for prediction

# 📈 Results & Insights

Organic avocados are generally more expensive than conventional ones.

Avocado prices show yearly fluctuations depending on demand and seasonality.

Among tested models, [best performing model – fill based on results] achieved the highest accuracy for price prediction.

# 🔮 Future Improvements

Hyperparameter tuning for better accuracy

Deploy model using Flask / Streamlit

Build an interactive dashboard for price forecasting

👩‍💻 Author

Developed by Prachi Singare as part of a Machine Learning project on Avocado Price Prediction.
