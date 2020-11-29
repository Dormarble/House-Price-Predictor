from data import Data
from model import Model

class Predictor:
    def __init__(self):
        self.model = Model()

    def predict(self, complex_name, supply_area, address, recent_price, recent_contact_date, floor, sell_date):
        data = Data(complex_name, supply_area, address, recent_price, recent_contact_date, floor, sell_date)

        child_input_data = data.make_child_input_data()
        rf, dt, xgb = self.model.predict_child_model(child_input_data)

        
        meta_input_data = data.make_meta_input_data(rf, dt, xgb)
        
        raw_result = self.model.predict_meta_model(meta_input_data)

        result = data.make_result(raw_result)
        
        return result


predictor = Predictor()
print(predictor.predict("현대", 82.29, "서울시 성동구 성수동1가", 10000000, '2020-01-01', 10, '2020-12-31'))