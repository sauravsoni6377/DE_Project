# IndiaTour Insights: Predicting and Analyzing Tourist Behavior in India
Welcome to the IndiaTour Insights repository! This project aims to analyze and predict tourist behavior in India by leveraging machine learning models and interactive web technologies. It provides valuable insights into tourism trends, including domestic and foreign visitors, monument popularity, and foreign exchange earnings. The platform integrates robust technologies for data analysis, prediction, and visualization.</b>

## Table of Contents
Introduction</b>
Features</b>
Technologies Used</b>
Setup and Installation</b>
Usage</b>
Challenges and Solutions</b>
Demo and Resources</b>
## Introduction
IndiaTour Insights analyzes foreign and domestic tourism trends using government-provided data. By employing machine learning and big data techniques, the project provides:</b>

Predictions of visitor trends for major monuments.
Insights into the impact of events (e.g., pandemics) on tourism.
Visualizations for data-driven decision-making.

## Features
- Data Integration and Storage</b>

- Unified MySQL database storing tourism-related data (visitor counts, monuments, earnings).
Scalable structure for real-time updates.</b>
Machine Learning Predictions</b>

Linear Regression and Decision Trees for forecasting trends.
Predictions for both domestic and foreign visitors with high accuracy.</b>
Interactive Web Interface</b>

Built using Streamlit for seamless visualization and analysis.
Features include filtering, comparisons, and trend analysis.</b>
Data Export and Customization</b>

Export filtered datasets in CSV format.
Advanced analysis tools like correlation heatmaps and scatter plots.</b>
Deployment with Docker</b>

Containerized application for easy deployment across environments.
Ensures consistency, scalability, and minimal setup challenges.</b>
## Technologies Used
Data Processing and Machine Learning</b>
Python: Pandas, NumPy, Matplotlib for data wrangling and visualization.
Scikit-learn: Implementation of predictive models.
Apache Spark: Big data processing and scalable machine learning.</b>
Web Development</b>
Streamlit: Interactive dashboard for visualization and user interaction.</b>
Backend and Database</b>
MySQL: Database for storing and querying tourism data.</b>
Deployment</b>
Docker: Containerization for consistent and reproducible environments.</b>
Setup and Installation</b>

## Prerequisites
Docker and Docker Compose installed on your system.</b>
MySQL server running locally or accessible remotely.</b>
## Installation Steps
Clone the Repository:</b>

git clone https://github.com/dhruvak001/data_engg</b>
cd data_engg</b>

Set Up Docker Containers:</b>

docker-compose up --build</b>

Access the Streamlit Dashboard:</b>
Navigate to http://localhost:8501 in your web browser.</b>
Usage</b>
Explore Data Trends:
Use the dashboard to filter and compare visitor trends.</b>
View Predictions:
Analyze machine learning predictions for selected monuments.</b>
Export Insights:
Download datasets for offline analysis.</b>
## Challenges and Solutions
Data Quality:
Addressed missing values with data wrangling techniques.</b>
Model Performance:
Cross-validated models to avoid overfitting.</b>
Big Data Processing:
Employed Apache Spark for efficient parallel computations.</b>
Deployment:
Used Docker to simplify multi-environment deployment.</b>
## Demo and Resources
Source Code: GitHub Repository
Colab Notebook: Data Analysis Notebook</b>

## Conclusion
IndiaTour Insights provides a robust platform for analyzing and predicting tourist behavior, making it a valuable tool for stakeholders in the tourism industry. Future extensions include real-time data integration and more granular analysis.

## Contributors:

Saurav Soni (B22AI035)<br>
Dhruva Kumar Kaushal (B22AI017)<br>
Feel free to contribute or raise issues in the repository! 🚀
