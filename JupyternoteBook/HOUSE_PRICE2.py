#!/usr/bin/env python
# coding: utf-8


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
    
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

train_data = pd.read_csv('C:/Hackathon-2/Group-36/DATA_SET/train.csv', index_col='Id')

# below is sample test csv prepared in order to validate the modle derived for accuracy checking
# ( some rows are taken from training data set to make sure predictions made can be validated by us


test_data = pd.read_csv('C:/Hackathon-2/Group-36/DATA_SET/test.csv', index_col='Id')

train_data.head()
train_data.columns

train_col_null = train_data.columns[train_data.isnull().any() == True].tolist()
train_data[train_col_null].isnull().sum()

# test_data.head()

# test_data.columns

test_col_null = test_data.columns[test_data.isnull().any() == True].tolist()
test_data[test_col_null].isnull().sum()

X = train_data.dropna(axis=0, subset=['SalePrice'])

y = X.SalePrice

X.drop(['SalePrice'], axis=1, inplace=True)

X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

low_cardinality_cols = [cname for cname in X_train_full.columns if X_train_full[cname].nunique() < 10 and X_train_full[cname].dtype == 'object']

# low_cardinality_cols

numeric_col = [cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64', 'float64']]

# numeric_col

my_cols = low_cardinality_cols + numeric_col
X_train = X_train_full[my_cols].copy()
X_valid = X_valid_full[my_cols].copy()
X_test = test_data[my_cols].copy()

X_train = pd.get_dummies(X_train)
X_valid = pd.get_dummies(X_valid)
X_test = pd.get_dummies(X_test)

X_train, X_valid = X_train.align(X_valid, join='left', axis=1)

X_train, X_test = X_train.align(X_test, join='left', axis=1)

xgb = XGBRegressor(n_estimators=2000,learning_rate=0.05)

xgb.fit(X_train, y_train)

y_pred = xgb.predict(X_valid)

mae = mean_absolute_error(y_pred, y_valid)

print(mae)

prediction = xgb.predict(X_test)

output = pd.DataFrame({'Id': X_test.index,'SalePrice':prediction})

# change as per requirement

output.to_csv('C:/Hackathon-2/Group-36/SUB_T/HP_03_TES2.csv', index=False)

# output.head(50)
