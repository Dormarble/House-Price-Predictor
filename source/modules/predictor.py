from .data import Data
from .model import Model

class Predictor:
    def __init__(self):
        self.model = Model()

    def predict(self, complex_name, supply_area, address, recent_price, recent_contact_date, floor, sell_date):
        print(complex_name, supply_area, address, recent_price, recent_contact_date, floor, sell_date)
        self.data = Data(complex_name, supply_area, address, recent_price, recent_contact_date, floor, sell_date)

        child_input_data = self.data.make_child_input_data()
        rf, dt, xgb = self.model.predict_child_model(child_input_data)


        meta_input_data = self.data.make_meta_input_data(rf, dt, xgb)
        
        raw_result = self.model.predict_meta_model(meta_input_data)

        result = self.data.make_result(raw_result)
        
        return result

    def get_dist(self):
        return self.data.dist_station, self.data.dist_hospital, self.data.dist_hangang