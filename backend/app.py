import os
import pandas as pd
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy



from flask import Flask, jsonify
from flask_cors import CORS

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})



# Load and clean the dataset
file_path = 'India-Tourism-Statistics-2021-Table-5.2.3.csv'
data = pd.read_csv(file_path)

# Fill missing values and rename columns
data['% Growth 2021-21/2019-20-Domestic'].fillna(0, inplace=True)
data['% Growth 2021-21/2019-20-Foreign'].fillna(0, inplace=True)
data.rename(columns={
    'Circle': 'circle',
    'Name of the Monument ': 'monument_name',
    'Domestic-2019-20': 'domestic_2019_20',
    'Foreign-2019-20': 'foreign_2019_20',
    'Domestic-2020-21': 'domestic_2020_21',
    'Foreign-2020-21': 'foreign_2020_21',
    '% Growth 2021-21/2019-20-Domestic': 'growth_domestic',
    '% Growth 2021-21/2019-20-Foreign': 'growth_foreign'
}, inplace=True)

# Flask application setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tourism_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the database schema
class TourismData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    circle = db.Column(db.String(100), nullable=False)
    monument_name = db.Column(db.String(200), nullable=False)
    domestic_2019_20 = db.Column(db.Integer, nullable=False)
    foreign_2019_20 = db.Column(db.Integer, nullable=False)
    domestic_2020_21 = db.Column(db.Integer, nullable=False)
    foreign_2020_21 = db.Column(db.Integer, nullable=False)
    growth_domestic = db.Column(db.Float, nullable=False)
    growth_foreign = db.Column(db.Float, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Populate the database
def populate_database(dataframe):
    for _, row in dataframe.iterrows():
        record = TourismData(
            circle=row['circle'],
            monument_name=row['monument_name'],
            domestic_2019_20=row['domestic_2019_20'],
            foreign_2019_20=row['foreign_2019_20'],
            domestic_2020_21=row['domestic_2020_21'],
            foreign_2020_21=row['foreign_2020_21'],
            growth_domestic=row['growth_domestic'],
            growth_foreign=row['growth_foreign']
        )
        db.session.add(record)
    db.session.commit()

with app.app_context():
    populate_database(data)


# Define API endpoints
@app.route('/api/data', methods=['GET'])
def get_data():
    records = TourismData.query.all()
    return jsonify([{
        'id': record.id,
        'circle': record.circle,
        'monument_name': record.monument_name,
        'domestic_2019_20': record.domestic_2019_20,
        'foreign_2019_20': record.foreign_2019_20,
        'domestic_2020_21': record.domestic_2020_21,
        'foreign_2020_21': record.foreign_2020_21,
        'growth_domestic': record.growth_domestic,
        'growth_foreign': record.growth_foreign
    } for record in records])

@app.route('/api/data/circle/<circle_name>', methods=['GET'])
def get_data_by_circle(circle_name):
    records = TourismData.query.filter_by(circle=circle_name).all()
    if not records:
        return jsonify({'message': 'No data found for the specified circle'}), 404
    return jsonify([{
        'id': record.id,
        'circle': record.circle,
        'monument_name': record.monument_name,
        'domestic_2019_20': record.domestic_2019_20,
        'foreign_2019_20': record.foreign_2019_20,
        'domestic_2020_21': record.domestic_2020_21,
        'foreign_2020_21': record.foreign_2020_21,
        'growth_domestic': record.growth_domestic,
        'growth_foreign': record.growth_foreign
    } for record in records])

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Tourism Data API!'})


if __name__ == '__main__':
    app.run(debug=True)
