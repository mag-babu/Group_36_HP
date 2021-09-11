import uvicorn
import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from utils import init_model, train_model
from typing import List


# PREDICTR_ENDPOINT = os.getenv("PREDICTR_ENDPOINT")

PREDICTR_ENDPOINT = "http://predictr:9999"

# defining the main app

app = FastAPI(title="trainr", docs_url="/")

# calling the load_model during startup.
# this will train the model and keep it loaded for prediction.

app.add_event_handler("startup", init_model)

# class which is expected in the payload while training

class TrainIn(BaseModel):
    Id: float = 1
    MSSubClass: float = 60
    MSZoning: str = 'RL'
    LotFrontage: float = 65
    LotArea: float = 8450 
    Street: str = 'Pave'
    Alley: str = 'NA'
    LotShape: str = 'Reg'
    LandContour: str = 'Lvl'
    Utilities: str = 'AllPub'
    LotConfig: str = 'Inside'
    LandSlope: str = 'Gtl'
    Neighborhood: str = 'CollCr'
    Condition1: str = 'Norm'
    Condition2: str = 'Norm'
    BldgType: str = '1Fam'
    HouseStyle: str = '2Story'
    OverallQual: float = 7
    OverallCond: float = 5
    YearBuilt: float = 2003
    YearRemodAdd: float = 2003
    RoofStyle: str = 'Gable'
    RoofMatl: str = 'CompShg'
    Exterior1st: str = 'VinylSd'
    Exterior2nd: str = 'VinylSd'
    MasVnrType: str ='BrkFace'
    MasVnrArea: float = 196
    ExterQual: str = 'Gd'
    ExterCond: str = 'TA'   
    Foundation: str = 'PConc'
    BsmtQual: str = 'Gd'
    BsmtCond: str = 'TA'
    BsmtExposure: str = 'No'
    BsmtFinType1: str = 'GLQ'
    BsmtFinSF1: float = 706
    BsmtFinType2: str = 'Unf'
    BsmtFinSF2: float = 0
    BsmtUnfSF: float = 150
    TotalBsmtSF: float = 856
    Heating: str = 'GasA'
    HeatingQC: str = 'Ex'
    CentralAir: str = 'Y'
    Electrical: str = 'SBrkr'
    fstFlrSF: float = 856 
    sndFlrSF: float = 854
    LowQualFinSF: float = 0
    GrLivArea: float = 1710
    BsmtFullBath: float = 1
    BsmtHalfBath: float = 0
    FullBath: float = 2
    HalfBath: float = 1
    BedroomAbvGr: float = 3
    KitchenAbvGr: float = 1
    KitchenQual: str = 'Gd'
    TotRmsAbvGrd: float = 8
    Functional: str = 'Typ'
    Fireplaces: float = 0
    FireplaceQu: str = 'NA'
    GarageType: str = 'Attchd'
    GarageYrBlt: float = 2003
    GarageFinish: str = 'RFn'
    GarageCars: float = 2
    GarageArea: float = 548
    GarageQual: str  = 'TA'
    GarageCond: str = 'TA'
    PavedDrive: str = 'Y'
    WoodDeckSF: float = 0
    OpenPorchSF: float = 61
    EnclosedPorch: float = 0
    tSsnPorch: float = 0
    ScreenPorch: float = 0 
    PoolArea: float = 0
    PoolQC: str = 'NA'
    Fence: str = 'NA'
    MiscFeature: str = 'NA'
    MiscVal: float = 0
    MoSold: float = 2
    YrSold: float = 2008
    SaleType: str = 'WD'
    SaleCondition: str = 'Normal'
    SalePrice: float = 208500   
       
# Route definitions
@app.get("/ping")
# Healthcheck route to ensure that the API is up and running
def ping():
    return {"ping": "pong"}


@app.post("/train", status_code=200)

# Route to further train the model based on user input in form of feedback loop
# Payload: FeedbackIn containing the parameters and correct flower class
# Response: Dict with detail confirming success (200)

def train(data: List[TrainIn]):
    train_model(data)
    # tell predictr to reload the model
    response = requests.post(f"{PREDICTR_ENDPOINT}/reload_model")
    return {"detail": "Training successful"}


# Main function to start the app when main.py is called
if __name__ == "__main__":
    # Uvicorn is used to run the server and listen for incoming API requests on 0.0.0.0:8888
    uvicorn.run("main:app", host="0.0.0.0", port=7777, reload=True)
