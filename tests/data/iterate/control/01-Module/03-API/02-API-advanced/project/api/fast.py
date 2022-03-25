
from datetime import datetime
import pytz

import pandas as pd
import joblib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# http://127.0.0.1:8000/predict?pickup_datetime=2012-10-06 12:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2


@app.get("/predict_untyped")
def predict_untyped(pickup_datetime,        # 2013-07-06 17:18:00
                    pickup_longitude,       # -73.950655
                    pickup_latitude,        # 40.783282
                    dropoff_longitude,      # -73.984365
                    dropoff_latitude,       # 40.769802
                    passenger_count):       # 1

    return predict(
        pickup_datetime=pickup_datetime,
        pickup_longitude=float(pickup_longitude),
        pickup_latitude=float(pickup_latitude),
        dropoff_longitude=float(dropoff_longitude),
        dropoff_latitude=float(dropoff_latitude),
        passenger_count=int(passenger_count))


@app.get("/")
def root():
    return dict(greeting="hello")
