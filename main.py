from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import housing_collection, crime_collection, sentiment_collection

app = FastAPI()

# Define Pydantic models for input validation
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

# Fetch all Housing Data
@app.get("/housing")
async def get_housing_data():
    data = list(housing_collection.find({}, {"_id": 0}))
    if not data:
        raise HTTPException(status_code=404, detail="No housing data found")
    return data

# Add new Housing Data (POST)
@app.post("/housing")
async def add_housing_data(housing_data: HousingData):
    try:
        housing_collection.insert_one(housing_data.dict())
        return {"message": "Housing data added successfully"}
    except:
        raise HTTPException(status_code=500, detail="Failed to add housing data")

# Update Housing Data (PUT)
@app.put("/housing")
async def update_housing_data(area: str, date: str, price: float):
    result = housing_collection.update_one(
        {"area": area, "date": date},
        {"$set": {"price": price}}
    )
    if result.modified_count == 1:
        return {"message": "Housing data updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Housing data not found or no change made")

# Delete Housing Data (DELETE)
@app.delete("/housing")
async def delete_housing_data(area: str, date: str):
    result = housing_collection.delete_one({"area": area, "date": date})
    if result.deleted_count == 1:
        return {"message": "Housing data deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Housing data not found")

# Fetch all Crime Data
@app.get("/crime")
async def get_crime_data():
    data = list(crime_collection.find({}, {"_id": 0}))
    if not data:
        raise HTTPException(status_code=404, detail="No crime data found")
    return data

# Add new Crime Report (POST)
@app.post("/crime")
async def add_crime_data(crime_report: CrimeReport):
    try:
        crime_collection.insert_one(crime_report.dict())
        return {"message": "Crime report added successfully"}
    except:
        raise HTTPException(status_code=500, detail="Failed to add crime report")

# Update Crime Data (PUT)
@app.put("/crime")
async def update_crime_data(neighborhood: str, date: str, crime_type: str):
    result = crime_collection.update_one(
        {"neighborhood": neighborhood, "date": date},
        {"$set": {"crime_type": crime_type}}
    )
    if result.modified_count == 1:
        return {"message": "Crime data updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Crime data not found or no change made")

# Delete Crime Data (DELETE)
@app.delete("/crime")
async def delete_crime_data(neighborhood: str, date: str):
    result = crime_collection.delete_one({"neighborhood": neighborhood, "date": date})
    if result.deleted_count == 1:
        return {"message": "Crime data deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Crime data not found")

# Fetch all Sentiment Data
@app.get("/sentiment")
async def get_sentiment_data():
    data = list(sentiment_collection.find({}, {"_id": 0}))
    if not data:
        raise HTTPException(status_code=404, detail="No sentiment data found")
    return data

# Add new Sentiment Analysis (POST)
@app.post("/sentiment")
async def add_sentiment_data(sentiment: SentimentAnalysis):
    try:
        sentiment_collection.insert_one(sentiment.dict())
        return {"message": "Sentiment data added successfully"}
    except:
        raise HTTPException(status_code=500, detail="Failed to add sentiment data")

# Update Sentiment Data (PUT)
@app.put("/sentiment")
async def update_sentiment_data(date: str, text: str, sentiment: str):
    result = sentiment_collection.update_one(
        {"date": date},
        {"$set": {"text": text, "sentiment": sentiment}}
    )
    if result.modified_count == 1:
        return {"message": "Sentiment data updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Sentiment data not found or no change made")

# Delete Sentiment Data (DELETE)
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
