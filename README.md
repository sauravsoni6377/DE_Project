# IndiaTour Insights: Predicting and Analyzing Tourist Behavior in India
Welcome to the IndiaTour Insights repository! This project aims to analyze and predict tourist behavior in India by leveraging machine learning models and interactive web technologies. It provides valuable insights into tourism trends, including domestic and foreign visitors, monument popularity, and foreign exchange earnings. The platform integrates robust technologies for data analysis, prediction, and visualization.</b>

## Table of Contents
Introduction
Features
Technologies Used
Setup and Installation
Usage
Challenges and Solutions
Demo and Resources
Introduction
IndiaTour Insights analyzes foreign and domestic tourism trends using government-provided data. By employing machine learning and big data techniques, the project provides:

Predictions of visitor trends for major monuments.
Insights into the impact of events (e.g., pandemics) on tourism.
Visualizations for data-driven decision-making.
Features
Data Integration and Storage

Unified MySQL database storing tourism-related data (visitor counts, monuments, earnings).
Scalable structure for real-time updates.
Machine Learning Predictions

Linear Regression and Decision Trees for forecasting trends.
Predictions for both domestic and foreign visitors with high accuracy.
Interactive Web Interface

Built using Streamlit for seamless visualization and analysis.
Features include filtering, comparisons, and trend analysis.
Data Export and Customization

Export filtered datasets in CSV format.
Advanced analysis tools like correlation heatmaps and scatter plots.
Deployment with Docker

Containerized application for easy deployment across environments.
Ensures consistency, scalability, and minimal setup challenges.
Technologies Used
Data Processing and Machine Learning
Python: Pandas, NumPy, Matplotlib for data wrangling and visualization.
Scikit-learn: Implementation of predictive models.
Apache Spark: Big data processing and scalable machine learning.
Web Development
Streamlit: Interactive dashboard for visualization and user interaction.
Backend and Database
MySQL: Database for storing and querying tourism data.
Deployment
Docker: Containerization for consistent and reproducible environments.
Setup and Installation
Prerequisites
Docker and Docker Compose installed on your system.
MySQL server running locally or accessible remotely.
Installation Steps
Clone the Repository:
bash
Copy code
git clone https://github.com/dhruvak001/data_engg
cd data_engg
Set Up Docker Containers:
bash
Copy code
docker-compose up --build
Access the Streamlit Dashboard:
Navigate to http://localhost:8501 in your web browser.
Usage
Explore Data Trends:
Use the dashboard to filter and compare visitor trends.
View Predictions:
Analyze machine learning predictions for selected monuments.
Export Insights:
Download datasets for offline analysis.
Challenges and Solutions
Data Quality:
Addressed missing values with data wrangling techniques.
Model Performance:
Cross-validated models to avoid overfitting.
Big Data Processing:
Employed Apache Spark for efficient parallel computations.
Deployment:
Used Docker to simplify multi-environment deployment.
Demo and Resources
Source Code: GitHub Repository
Demo Video: Watch Here
Colab Notebook: Data Analysis Notebook
Conclusion
IndiaTour Insights provides a robust platform for analyzing and predicting tourist behavior, making it a valuable tool for stakeholders in the tourism industry. Future extensions include real-time data integration and more granular analysis.

Contributors:

Saurav Soni (B22AI035)
Dhruva Kumar Kaushal (B22AI017)
Feel free to contribute or raise issues in the repository! 🚀
