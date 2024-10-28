from pymongo import MongoClient

# MongoDB Connection Setup
client = MongoClient("mongodb+srv://per18044:mEANFqihdP9BPGwt@cluster0.oowe8qv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.pai_db

# Collections
survey_collection = db.survey_data
housing_collection = db.housing_data
crime_collection = db.crime_data
sentiment_collection = db.sentiment_analysis
