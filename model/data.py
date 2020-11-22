import pandas as pd
import numpy as np
import datetime

class Data:
    # recent_contact_date --> %Y-%m-%d
    def __init__(self, complex_name, supply_area, address, recent_price, recent_contact_date, floor, sell_date):
        self.pyeong_complex_df = pd.read_csv('./pyeong_complex.csv', index_col='idx')

        self.complex = self.pyeong_complex_df[(self.pyeong_complex_df['complexName'] == complex_name)
                                        & (self.pyeong_complex_df['supplyArea'] == supply_area)
                                        & (self.pyeong_complex_df['address'] == address)]

        if len(self.complex) == 0:
            self.complex = None

        self.floor = floor
        self.floor_rate = float(floor / (self.complex['highFloor'].iloc[0] + self.complex['lowFloor'].iloc[0]) * 0.8)
        self.contact_day = self.convert_date(recent_contact_date)
        self.recent_price = recent_price
        self.recent_contact_day = self.convert_date(sell_date)
        self.recent_floor_rate = self.floor_rate

    def make_child_input_data(self):
        if len(self.complex) != 0:
            # drop complexName
            self.complex.drop(['complexName'], axis=1, inplace=True)

            # drop address
            self.complex.drop(['address'], axis=1, inplace=True)
            
            # add contactDate
            self.complex['contactDay'] = self.contact_day

            # add floor
            self.complex['floor'] = self.floor

            # add floorRate
            self.complex['floorRate'] = self.floor_rate
        
            self.complex = self.complex[['supplyArea', 'householdCountByPyeong', 'exclusiveRate', 'roomCnt', 'bathroomCnt', 'latitude', 'longitude', 'highFloor', 'lowFloor', 'constructYear', 'totalDongCount', 'maxSupplyArea', 'minSupplyArea', '서울시 강남구 대치동', '서울시 서초구 잠원동', '서울시 강남구 압구정동', '서울시 관악구 봉천동', '서울시 강남구 도곡동', '서울시 노원구 중계동', '서울시 마포구 상암동', '서울시 강남구 개포동', '서울시 서초구 반포동', '서울시 강남구 청담동', '서울시 서초구 방배동', '서울시 강남구 삼성동', '서울시 성동구 성수동1가', '서울시 용산구 이촌동', '서울시 종로구 내수동', '서울시 양천구 목동', '서울시 종로구 사직동', '서울시 성북구 길음동', '서울시 서초구 서초동', '서울시 영등포구 여의도동', '서울시 중구 장충동1가', '서울시 종로구 명륜2가', '우성', '동양고속', '기타', '대림산업', '계룡산업', '삼성물산', '롯데', '현대', '한양', '대우', '현대산업개발', '선경', '한신공영', '쌍용', '복도식', '계단식', '복합식', 'HF001', 'HF002', 'HT001', 'HT002', 'HT005', 'A01', 'A03', 'volume', 'contactDay', 'floor', 'floorRate', 'distHangang', 'distStation', 'distHospital']]

            return self.complex
        else:
            return None

    def make_meta_input_data(self, rf, dt, xgb):
        meta_data = {
            'recentContactDay' : [self.recent_contact_day],
            'recentFloorRate' : [self.recent_floor_rate],
            'recentPrice' : [self.recent_price],
            'contactDay' : [self.contact_day],
            'floorRate' : [self.floor_rate],
            'rf' : [rf],
            'dt' : [dt],
            'xgb' : [xgb]
            }

        meta_input_data = pd.DataFrame(meta_data)

        meta_input_data['recentPrice'] = np.log2(meta_input_data['recentPrice'])
        meta_input_data['rf'] = np.log2(meta_input_data['rf'])
        meta_input_data['dt'] = np.log2(meta_input_data['dt'])
        meta_input_data['xgb'] = np.log2(meta_input_data['xgb'])
        
        return meta_input_data
        
    def make_result(self, input):
        return int(np.exp2(input)[0])


    def convert_date(self, date):
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        critia_date = datetime.datetime(2000, 1, 1)
        return (date - critia_date).days

