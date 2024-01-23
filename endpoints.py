#Import
from fastapi import FastAPI, Request
import xgboost
import joblib
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import json

app = FastAPI()

# Load BST
bst = joblib.load("./model/rec_model.joblib")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
async def predict(request: Request):
    recieved = await request.json()
    print("Received JSON data:", recieved)
    # Pre-Processing

    # Convert to Pandas
    input = pd.DataFrame(recieved)

    # Add Census Data
    census = pd.read_csv("./data/checkfiles/censuscheck.csv")
    
    # Merge DF with Census Data
    #input = input.merge(census, left_on='postal_code', how='inner')
    print(input.shape)
    print(input.head())
    


    return {"result": "Prediction result"}
