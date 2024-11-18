import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from io import BytesIO
import plotly.express as px
import plotly.graph_objects as go
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# MySQL connection
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'port': 3306,
    'database': 'tourism_db'
}
engine = create_engine(f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

# Query data from MySQL
query = "SELECT * FROM tourism_data"
data = pd.read_sql(query, con=engine)

def load_ml_models():
    # Define scalers
    scaler_X = MinMaxScaler()
    scaler_y_domestic = MinMaxScaler()
    scaler_y_foreign = MinMaxScaler()
    
    # Load pretrained models
    model_domestic = tf.keras.models.load_model("/Users/sanjay/data_engg/weights/domestic_visitor_weights.h5")
    model_foreign = tf.keras.models.load_model("/Users/sanjay/data_engg/weights/foreign_visitor_weights.h5")
    
    return model_domestic, model_foreign, scaler_X, scaler_y_domestic, scaler_y_foreign

model_domestic, model_foreign, scaler_X, scaler_y_domestic, scaler_y_foreign = load_ml_models()

# Streamlit Dashboard Setup
st.set_page_config(page_title="India Tourism Dashboard", layout="wide")
st.title("India Tourism Dashboard 🇮🇳")

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = st.sidebar.radio("Go to", ["Home", "Search & Filter", "Insights & Comparisons", "Custom Analysis", "ML Predictions", "Export Data"])



# Streamlit app
st.set_page_config(page_title="India Tourism Dashboard", layout="wide")
st.title("India Tourism Dashboard 🇮🇳")

# Sidebar navigation
st.sidebar.title("Navigation")
pages = st.sidebar.radio("Go to", ["Home", "Search & Filter", "Insights & Comparisons", "Custom Analysis", "Export Data"])

if pages == "Home":
    st.header("Overview")
    
    # Display key metrics
    total_domestic = data['domestic_2019_20'].sum()
    total_foreign = data['foreign_2019_20'].sum()
    total_monuments = data['Name of the Monument'].nunique()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Domestic Visitors", f"{total_domestic:,}")
    col2.metric("Total Foreign Visitors", f"{total_foreign:,}")
    col3.metric("Total Monuments", total_monuments)

    # Top 10 monuments by visitors
    st.subheader("Top 10 Monuments by Domestic Visitors")
    top_monuments = data[['Name of the Monument', 'domestic_2019_20']].sort_values(by='domestic_2019_20', ascending=False).head(10)
    fig = px.bar(top_monuments, x="Name of the Monument", y="domestic_2019_20", title="Top 10 Monuments by Domestic Visitors", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

elif pages == "Search & Filter":
    st.header("Search & Filter Data")
    
    # Circle filter
    selected_circle = st.selectbox("Select Circle", ["All"] + sorted(data['circle'].unique().tolist()))
    filtered_data = data if selected_circle == "All" else data[data['circle'] == selected_circle]

    # Visitor count filter
    min_visitors = st.slider("Minimum Domestic Visitors (2019-20)", 0, int(data['domestic_2019_20'].max()), 0)
    filtered_data = filtered_data[filtered_data['domestic_2019_20'] >= min_visitors]
    
    # Display filtered data
    st.subheader("Filtered Data")
    st.dataframe(filtered_data)

    # Display filtered data statistics
    st.subheader("Filtered Data Statistics")
    st.write(filtered_data.describe())

elif pages == "Insights & Comparisons":
    st.header("Insights & Comparisons")
    
    # Comparison by circles
    st.subheader("Comparison of Domestic vs Foreign Visitors by Circle")
    comparison_data = data.groupby('circle').agg({
        'domestic_2019_20': 'sum',
        'foreign_2019_20': 'sum'
    }).reset_index()
    fig = px.bar(comparison_data, x="circle", y=["domestic_2019_20", "foreign_2019_20"], barmode="group", title="Visitors by Circle")
    st.plotly_chart(fig, use_container_width=True)
    
    # Growth rate visualization
    st.subheader("Growth Rates (Domestic vs Foreign)")
    growth_data = data[['Name of the Monument', 'growth_domestic', 'growth_foreign']]
    fig = px.scatter(growth_data, x='growth_domestic', y='growth_foreign', color='Name of the Monument', title="Growth Rate Comparison")
    st.plotly_chart(fig, use_container_width=True)

elif pages == "Custom Analysis":
    st.header("Custom Analysis")
    
    # Pairwise comparisons
    st.subheader("Pairwise Analysis of Visitors")
    feature_x = st.selectbox("Select X-Axis Feature", data.columns)
    feature_y = st.selectbox("Select Y-Axis Feature", data.columns)
    fig = px.scatter(data, x=feature_x, y=feature_y, color="circle", title=f"Comparison: {feature_x} vs {feature_y}")
    st.plotly_chart(fig, use_container_width=True)
    
    # Correlation heatmap
    st.subheader("Correlation Heatmap")
    corr = data.corr(numeric_only=True)
    fig = px.imshow(corr, text_auto=True, title="Correlation Matrix")
    st.plotly_chart(fig, use_container_width=True)



elif pages == "ML Predictions":
    st.header("Machine Learning Predictions")
    
    st.subheader("Input Features")
    # Inputs for model prediction
    num_features = st.slider("Number of Features", 2, 10, 5)
    feature_values = np.array([
        st.number_input(f"Feature {i+1}", min_value=0.0, max_value=1.0, value=0.5) 
        for i in range(num_features)
    ]).reshape(1, -1)
    
    # Scale input features
    scaled_features = scaler_X.transform(feature_values)
    
    # Predictions
    domestic_pred_scaled = model_domestic.predict(scaled_features)
    foreign_pred_scaled = model_foreign.predict(scaled_features)
    
    # Reverse scale predictions
    domestic_pred = scaler_y_domestic.inverse_transform(domestic_pred_scaled)
    foreign_pred = scaler_y_foreign.inverse_transform(foreign_pred_scaled)
    
    st.subheader("Predictions")
    st.write(f"Predicted Domestic Visitors (2020-21): {domestic_pred[0, 0]:,.0f}")
    st.write(f"Predicted Foreign Visitors (2020-21): {foreign_pred[0, 0]:,.0f}")

    st.markdown("---")
    st.subheader("Model Evaluation")
    st.write("Visualizations for model evaluation can be added here.")


elif pages == "Export Data":
    st.header("Export Data")
    
    # Select columns to export
    export_columns = st.multiselect("Select Columns", data.columns.tolist(), default=data.columns.tolist())
    export_data = data[export_columns]
    
    # Download filtered data
    buffer = BytesIO()
    export_data.to_csv(buffer, index=False)
    buffer.seek(0)
    st.download_button(
        label="Download Data as CSV",
        data=buffer,
        file_name="filtered_tourism_data.csv",
        mime="text/csv"
    )
