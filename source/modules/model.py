import numpy as np 
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor
import pickle
import joblib
from os.path import dirname

class Model:
    def __init__(self):
        self.random_forest_regressor = joblib.load(dirname(__file__) + '/model/random_forest_regressor.pkl')
        self.decision_tree_regressor = joblib.load(dirname(__file__) + '/model/decision_tree_regressor.pkl')
        self.xgboost_regressor = joblib.load(dirname(__file__) + '/model/xgboost_regressor.pkl')
        self.meta_regressor = joblib.load(dirname(__file__) + '/model/meta_model.pkl')
    
    def predict_child_model(self, input):
        rf = self.random_forest_regressor.predict(input)
        dt = self.decision_tree_regressor.predict(input)
        xgb = self.xgboost_regressor.predict(input)

        return int(rf), int(dt), int(xgb)

    def predict_meta_model(self, input):
        result = self.meta_regressor.predict(input)
        
        return result