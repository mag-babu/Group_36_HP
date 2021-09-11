import os
import pickle

# import numpy as np # linear algebra
# import pandas as pd # data processing
        
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# function to process data and return it in correct format

def process_data(data):
        
    processed = [
        {
            
            # "petal_width": d.petal_width,
            # "flower_class": d.flower_class,
            
            "Id": d.Id,
            "MSSubClass": d.MSSubClass,
            "MSZoning": d.MSZoning,
            "LotFrontage": d.LotFrontage,
            "LotArea": d.LotArea,
            "Street": d.Street,
            "Alley": d.Alley,
            "LotShape": d.LotShape,
            "LandContour": d.LandContour,
            "Utilities": d.Utilities,
            "LotConfig": d.LotConfig,
            "LandSlope": d.LandSlope,
            "Neighborhood": d.Neighborhood,
            "Condition1": d.Condition1,
            "Condition2": d.Condition2,
            "BldgType": d.BldgType,
            "HouseStyle": d.HouseStyle,
            "OverallQual": d.OverallQual,
            "OverallCond": d.OverallCond,
            "YearBuilt": d.YearBuilt,
            "YearRemodAdd": d.YearRemodAdd,
            "RoofStyle": d.RoofStyle,
            "RoofMatl": d.RoofMatl,
            "Exterior1st": d.Exterior1st,
            "Exterior2nd": d.Exterior2nd,
            "MasVnrType": d.MasVnrType,
            "MasVnrArea": d.MasVnrArea,
            "ExterQual": d.ExterQual,
            "ExterCond": d.ExterCond,
            "Foundation": d.Foundation,
            "BsmtQual": d.BsmtQual,
            "BsmtCond": d.BsmtCond,
            "BsmtExposure": d.BsmtExposure,
            "BsmtFinType1": d.BsmtFinType1,
            "BsmtFinSF1": d.BsmtFinSF1,
            "BsmtFinType2": d.BsmtFinType2,
            "BsmtFinSF2": d.BsmtFinSF2,
            "BsmtUnfSF": d.BsmtUnfSF,
            "TotalBsmtSF": d.TotalBsmtSF,
            "Heating": d.Heating,
            "HeatingQC": d.HeatingQC,
            "CentralAir": d.CentralAir,
            "Electrical": d.Electrical,
            "fstFlrSF": d.fstFlrSF,
            "sndFlrSF": d.sndFlrSF,
            "LowQualFinSF": d.LowQualFinSF,
            "GrLivArea": d.GrLivArea,
            "BsmtFullBath": d.BsmtFullBath,
            "BsmtHalfBath": d.BsmtHalfBath,
            "FullBath": d.FullBath,
            "HalfBath": d.HalfBath,
            "BedroomAbvGr": d.BedroomAbvGr,
            "KitchenAbvGr": d.KitchenAbvGr,
            "KitchenQual": d.KitchenQual,
            "TotRmsAbvGrd": d.TotRmsAbvGrd,
            "Functional": d.Functional,
            "Fireplaces": d.Fireplaces,
            "FireplaceQu": d.FireplaceQu,
            "GarageType": d.GarageType,
            "GarageYrBlt": d.GarageYrBlt,
            "GarageFinish": d.GarageFinish,
            "GarageCars": d.GarageCars,
            "GarageArea": d.GarageArea,
            "GarageQual": d.GarageQual,
            "GarageCond": d.GarageCond,
            "PavedDrive": d.PavedDrive,
            "WoodDeckSF": d.WoodDeckSF,
            "OpenPorchSF": d.OpenPorchSF,
            "EnclosedPorch": d.EnclosedPorch,
            "tSsnPorch": d.tSsnPorch,
            "ScreenPorch": d.ScreenPorch,
            "PoolArea": d.PoolArea,
            "PoolQC": d.PoolQC,
            "Fence": d.Fence,
            "MiscFeature": d. MiscFeature,
            "MiscVal": d.MiscVal,
            "MoSold": d.MoSold,
            "YrSold": d.YrSold,
            "SaleType": d.SaleType,
            "SaleCondition": d.SaleCondition,
            "SalePrice": d.SalePrice,
 
        }
        for d in data
    ]

    return processed
