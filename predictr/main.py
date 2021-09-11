import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from utils import load_model, predict

# defining the main app
app = FastAPI(title="predictr", docs_url="/")

# class which is expected in the payload

class QueryIn(BaseModel):

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

 
# class which is returned in the response
class QueryOut(BaseModel):
    # flower_class: str
    SalePrice: float

# Route definitions
@app.get("/ping")
# Healthcheck route to ensure that the API is up and running
def ping():
    return {"ping": "pong"}


@app.post("/predict_saleprice", response_model=QueryOut, status_code=200)
# Route to do the prediction using the ML model defined.
# Payload: QueryIn containing the parameters
# Response: QueryOut containing the flower_class predicted (200)
def predict_saleprice(query_data: QueryIn):
    output = {"SalePrice": predict(query_data)}
    return output


@app.post("/reload_model", status_code=200)
# Route to reload the model from file
def reload_model():
    load_model()
    output = {"detail": "Model successfully loaded"}
    return output


# Main function to start the app when main.py is called
if __name__ == "__main__":
    # Uvicorn is used to run the server and listen for incoming API requests on 0.0.0.0:8888
    uvicorn.run("main:app", host="0.0.0.0", port=9999, reload=True)
