from pymongo import MongoClient

# MongoDB connection string (replace <username>, <password>, and <dbname> with your actual details)
connection_string = "mongodb+srv://per18044:mEANFqihdP9BPGwt@cluster0.oowe8qv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB Atlas
client = MongoClient(connection_string)

# Create or access the database "pai_db"
db = client["pai_db"]

# Create collections
survey_collection = db["survey_data"]
housing_collection = db["housing_data"]
crime_collection = db["crime_data"]
sentiment_collection = db["sentiment_analysis"]
age_collection = db["age_data"]
income_collection = db["income_data"]
population_collection = db["population_data"]
houses_collection = db["number_of_houses_data"]
occupied_houses_collection = db["occupied_houses_data"]
unemployment_collection = db["unemployment_data"]

# Insert 10 samples for survey_data, including questions
survey_examples = [
    {"user_id": "user_001", "questions": {"q1": "Do you own a home?", "q2": "Do you feel safe in your neighborhood?"}, "answers": {"q1": "yes", "q2": "yes"}, "timestamp": "2024-10-01T09:00:00Z"},
    {"user_id": "user_002", "questions": {"q1": "Do you own a home?", "q2": "Do you feel safe in your neighborhood?"}, "answers": {"q1": "no", "q2": "yes"}, "timestamp": "2024-10-05T11:30:00Z"},
    {"user_id": "user_003", "questions": {"q1": "Do you own a home?", "q2": "Do you feel safe in your neighborhood?"}, "answers": {"q1": "yes", "q2": "no"}, "timestamp": "2024-10-10T14:00:00Z"},
    {"user_id": "user_004", "questions": {"q1": "Do you own a home?", "q2": "Do you feel safe in your neighborhood?"}, "answers": {"q1": "no", "q2": "no"}, "timestamp": "2024-10-12T16:15:00Z"},
    {"user_id": "user_005", "questions": {"q1": "Do you own a home?", "q2": "Do you feel safe in your neighborhood?"}, "answers": {"q1": "yes", "q2": "yes"}, "timestamp": "2024-10-15T18:45:00Z"},
    {"user_id": "user_006", "questions": {"q1": "Do you own a home?", "q2": "Do you feel safe in your neighborhood?"}, "answers": {"q1": "yes", "q2": "no"}, "timestamp": "2024-10-20T12:30:00Z"},
    {"user_id": "user_007", "questions": {"q1": "Do you own a home?", "q2": "Do you feel safe in your neighborhood?"}, "answers": {"q1": "no", "q2": "yes"}, "timestamp": "2024-10-22T14:45:00Z"},
    {"user_id": "user_008", "questions": {"q1": "Do you own a home?", "q2": "Do you feel safe in your neighborhood?"}, "answers": {"q1": "yes", "q2": "yes"}, "timestamp": "2024-10-25T17:15:00Z"},
    {"user_id": "user_009", "questions": {"q1": "Do you own a home?", "q2": "Do you feel safe in your neighborhood?"}, "answers": {"q1": "no", "q2": "no"}, "timestamp": "2024-10-27T11:45:00Z"},
    {"user_id": "user_010", "questions": {"q1": "Do you own a home?", "q2": "Do you feel safe in your neighborhood?"}, "answers": {"q1": "yes", "q2": "yes"}, "timestamp": "2024-10-29T09:30:00Z"}
]
survey_collection.insert_many(survey_examples)

# Insert 10 samples for housing_data
housing_examples = [
    {"area": "Downtown Calgary", "price": 1200, "date": "2024-08-27"},
    {"area": "Beltline", "price": 1400, "date": "2024-08-28"},
    {"area": "Southeast Calgary", "price": 1100, "date": "2024-09-01"},
    {"area": "Northeast Calgary", "price": 1300, "date": "2024-09-05"},
    {"area": "Fish Creek", "price": 1150, "date": "2024-09-10"},
    {"area": "West Calgary", "price": 1500, "date": "2024-09-15"},
    {"area": "Chinook", "price": 1450, "date": "2024-09-18"},
    {"area": "East Calgary", "price": 1250, "date": "2024-09-20"},
    {"area": "Sundance", "price": 1350, "date": "2024-09-25"},
    {"area": "Southwest Calgary", "price": 1600, "date": "2024-09-30"}
]
housing_collection.insert_many(housing_examples)

# Insert 10 samples for crime_data
crime_examples = [
    {"neighborhood": "Beltline", "crime_type": "Theft", "date": "2024-08-01"},
    {"neighborhood": "Downtown", "crime_type": "Assault", "date": "2024-08-03"},
    {"neighborhood": "Chinook", "crime_type": "Robbery", "date": "2024-08-10"},
    {"neighborhood": "Southeast Calgary", "crime_type": "Burglary", "date": "2024-08-15"},
    {"neighborhood": "Northeast Calgary", "crime_type": "Theft", "date": "2024-08-20"},
    {"neighborhood": "Fish Creek", "crime_type": "Vandalism", "date": "2024-08-25"},
    {"neighborhood": "West Calgary", "crime_type": "Fraud", "date": "2024-09-01"},
    {"neighborhood": "Sundance", "crime_type": "Theft", "date": "2024-09-05"},
    {"neighborhood": "East Calgary", "crime_type": "Robbery", "date": "2024-09-10"},
    {"neighborhood": "Chinook", "crime_type": "Assault", "date": "2024-09-15"}
]
crime_collection.insert_many(crime_examples)

# Insert 10 samples for sentiment_analysis
sentiment_examples = [
    {"text": "Housing prices are skyrocketing!", "sentiment": "negative", "date": "2024-09-01"},
    {"text": "Crime rates seem to be decreasing.", "sentiment": "positive", "date": "2024-09-03"},
    {"text": "Public transportation is getting better.", "sentiment": "positive", "date": "2024-09-05"},
    {"text": "I'm worried about the rising rent costs.", "sentiment": "negative", "date": "2024-09-07"},
    {"text": "The new policies are helping improve safety.", "sentiment": "positive", "date": "2024-09-09"},
    {"text": "The economy is looking uncertain.", "sentiment": "negative", "date": "2024-09-12"},
    {"text": "I'm hopeful that housing will become more affordable.", "sentiment": "positive", "date": "2024-09-14"},
    {"text": "There is too much crime in the downtown area.", "sentiment": "negative", "date": "2024-09-16"},
    {"text": "I feel safer in my neighborhood after the new policies.", "sentiment": "positive", "date": "2024-09-18"},
    {"text": "Rents are still way too high.", "sentiment": "negative", "date": "2024-09-20"}
]
sentiment_collection.insert_many(sentiment_examples)

# Insert 10 samples for age_data (population divided by age groups)
age_examples = [
    {"age_group": "15-24", "population": 150000},
    {"age_group": "25-34", "population": 250000},
    {"age_group": "35-44", "population": 300000},
    {"age_group": "45-54", "population": 600000},
]