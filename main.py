from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import survey_collection, housing_collection, crime_collection, sentiment_collection

app = FastAPI()

# Pydantic Models for API Input
class SurveyResponse(BaseModel):
    user_id: str
    answers: dict
    timestamp: str

class HousingData(BaseModel):
    area: str
    price: float
    date: str

class CrimeReport(BaseModel):
    neighborhood: str
    crime_type: str
    date: str

class SentimentAnalysis(BaseModel):
    text: str
    sentiment: str
    date: str

# 1. Fetch Real-Time Data for Housing
@app.get("/housing")
async def get_housing_data():
    data = list(housing_collection.find({}, {"_id": 0}))
    if not data:
        raise HTTPException(status_code=404, detail="No housing data found")
    return data

# 2. Add New Housing Data (POST)
@app.post("/housing")
async def add_housing_data(housing_data: HousingData):
    try:
        housing_collection.insert_one(housing_data.dict())
        return {"message": "Housing data added successfully"}
    except:
        raise HTTPException(status_code=500, detail="Failed to add housing data")

# 3. Store User Survey Responses
@app.post("/survey")
async def store_survey_data(response: SurveyResponse):
    try:
        survey_collection.insert_one(response.dict())
        return {"message": "Survey data stored successfully"}
    except:
        raise HTTPException(status_code=500, detail="Failed to store survey data")

# 4. Fetch Real-Time Crime Reports
@app.get("/crime")
async def get_crime_data():
    data = list(crime_collection.find({}, {"_id": 0}))
    if not data:
        raise HTTPException(status_code=404, detail="No crime data found")
    return data

# 5. Store Sentiment Analysis Data
@app.post("/sentiment")
async def store_sentiment_data(sentiment: SentimentAnalysis):
    try:
        sentiment_collection.insert_one(sentiment.dict())
        return {"message": "Sentiment data stored successfully"}
    except:
        raise HTTPException(status_code=500, detail="Failed to store sentiment data")

# 6. Fetch Sentiment Analysis Results
@app.get("/sentiment")
async def get_sentiment_data():
    data = list(sentiment_collection.find({}, {"_id": 0}))
    if not data:
        raise HTTPException(status_code=404, detail="No sentiment data found")
    return data

# 7. Delete Housing Data by Area and Date (DELETE)
@app.delete("/housing")
async def delete_housing_data(area: str, date: str):
    result = housing_collection.delete_one({"area": area, "date": date})
    if result.deleted_count == 1:
        return {"message": "Housing data deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Housing data not found")

# 8. Delete Crime Data by Neighborhood and Date (DELETE)
@app.delete("/crime")
async def delete_crime_data(neighborhood: str, date: str):
    result = crime_collection.delete_one({"neighborhood": neighborhood, "date": date})
    if result.deleted_count == 1:
        return {"message": "Crime data deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Crime data not found")

# 9. Delete Sentiment Data by Date and Sentiment (DELETE)
@app.delete("/sentiment")
async def delete_sentiment_data(date: str, sentiment: str):
    result = sentiment_collection.delete_one({"date": date, "sentiment": sentiment})
    if result.deleted_count == 1:
        return {"message": "Sentiment data deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Sentiment data not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
