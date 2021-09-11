import os
import pickle

from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# define the class encodings and reverse encodings
# classes = {0: "Iris Setosa", 1: "Iris Versicolour", 2: "Iris Virginica"}
# r_classes = {y: x for x, y in classes.items()}


# function to train and load the model during startup

def init_model():

    if not os.path.isfile("models/hp_xg.pkl"):
    
        # clf = GaussianNB()
        
        clf = XGBRegressor(n_estimators=2000,learning_rate=0.05)        
        
        pickle.dump(clf, open("models/hp_xg.pkl", "wb"))


# function to train and save the model as part of the feedback loop

def train_model(data):

    # load the model
    
    clf = pickle.load(open("models/hp_xg.pkl", "rb"))

    # pull out the relevant X and y from the FeedbackIn object
    
    X = [list(d.dict().values())[:-1] for d in data]   
    y = [list(d.dict().values())[-1] for d in data]
    
    # y = [r_classes[d.flower_class] for d in data]
    
    # fit again based on the new data obtained    
    clf.fit(X, y)
     
    # save the model    
    pickle.dump(clf, open("models/hp_xg.pkl", "wb"))
