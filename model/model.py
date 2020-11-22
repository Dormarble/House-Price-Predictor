import numpy as np 
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor
import pickle
from sklearn.externals import joblib

class Model:
    def __init__(self):
        self.random_forest_regressor = joblib.load('./random_forest_regressor.pkl') 
        self.decision_tree_regressor = joblib.load('./decision_tree_regressor.pkl')
        self.xgboost_regressor = joblib.load('./xgboost_regressor.pkl')
        self.meta_regressor = joblib.load('./meta_model.pkl')
    
    def predict_child_model(self, input):
        rf = self.random_forest_regressor.predict(input)
        dt = self.decision_tree_regressor.predict(input)
        xgb = self.xgboost_regressor.predict(input)

        return int(rf), int(dt), int(xgb)

    def predict_meta_model(self, input):
        result = self.meta_regressor.predict(input)
        
        return result

