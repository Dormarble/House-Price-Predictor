import pandas as pd
import numpy as np
from os.path import dirname
data = pd.read_csv(dirname(__file__) + '/csv/trade_data_additional.csv', thousands = ',')

class Analyzer():
    def __init__(self):
        self.region_price = self.getRegionPrice()
        self.station_price = self.getStationPrice()
        self.hospital_price = self.getHospitalPrice()
        self.hangang_price = self.getHangangPrice()
        self.complex_price = self.getComplexPrice()
        self.brand_price = self.getBrandPrice()

    def getRegionPrice(self):
        data_region = {}  # { 지역(구): (거래연도, 평당가격) }
        for x in data[['address', 'price', 'contactDate', 'supplyArea']].values:
            region = x[0].split(' ')[1]
            price = float(x[1])
            year = int(x[2].split('-')[0])
            supplyArea = float(x[3])
            if (region, year) in data_region:
                data_region[(region, year)].append(price / supplyArea)
            else:
                data_region[(region, year)] = [price / supplyArea]
        # 평당 평균값으로 값 전환
        for k, p in data_region.items():
            p_avg = sum(p) / len(p)
            data_region[k] = p_avg
        data_region_list = sorted(list(data_region.items()))
        region_price = {}  # { '지역명': [[x(연도)], [y(평당 평균가)]] }
        for d in data_region_list:
            if d[0][0] in region_price:
                region_price[d[0][0]][0].append(d[0][1])
                region_price[d[0][0]][1].append(d[1])
            else:  # 구 이름      거래연도    가격
                region_price[d[0][0]] = [[d[0][1]], [d[1]]]
        return region_price

    def getStationPrice(self):
        data_station = {}  # data_station { 거래연도: (역까지의 거리, 평당가격) }
        for x in data[['distStation', 'price', 'contactDate', 'supplyArea']].values:
            distStation = float(x[0])
            price = float(x[1])
            year = int(x[2].split('-')[0])
            supplyArea = float(x[3])
            if year in data_station:
                data_station[year].append((distStation, price / supplyArea))
            else:
                data_station[year] = [(distStation, price / supplyArea)]
        for y, d in data_station.items():
            data_station[y] = sorted(d)

        data_station_list = sorted(list(data_station.items()))
        station_price = {}  # { '거래연도': [[x(역까지의 거리)], [y(평당 평균가)]] }
        for d in data_station_list:
            station_price[d[0]] = [[], []]
            for dps in d[1]:
                station_price[d[0]][0].append(dps[0])  # 역까지의 거리
                station_price[d[0]][1].append(dps[1])  # 평당 평균가
        return station_price

    def getHospitalPrice(self):
        data_hospital = {}  # data_hospital { 거래연도: (병원까지의 거리, 평당가격) }
        for x in data[['distHospital', 'price', 'contactDate', 'supplyArea']].values:
            distHospital = float(x[0])
            price = float(x[1])
            year = int(x[2].split('-')[0])
            supplyArea = float(x[3])
            if year in data_hospital:
                data_hospital[year].append((distHospital, price / supplyArea))
            else:
                data_hospital[year] = [(distHospital, price / supplyArea)]
        for y, d in data_hospital.items():
            data_hospital[y] = sorted(d)
        data_hospital_list = sorted(list(data_hospital.items()))
        hospital_price = {}  # { '거래연도': [[x(역까지의 거리)], [y(평당 평균가)]] }
        for d in data_hospital_list:
            hospital_price[d[0]] = [[], []]
            for dps in d[1]:
                hospital_price[d[0]][0].append(dps[0])  # 역까지의 거리
                hospital_price[d[0]][1].append(dps[1])  # 평당 평균가
        return hospital_price

    def getHangangPrice(self):
        data_hangang = {}  # data_hangang { 거래연도: (한강까지의 거리, 평당가격) }
        for x in data[['distHangangTopBottom', 'price', 'contactDate', 'supplyArea']].values:
            distHangang = float(x[0])
            price = float(x[1])
            year = int(x[2].split('-')[0])
            supplyArea = float(x[3])
            if year in data_hangang:
                data_hangang[year].append((distHangang, price / supplyArea))
            else:
                data_hangang[year] = [(distHangang, price / supplyArea)]
        for y, d in data_hangang.items():
            data_hangang[y] = sorted(d)
        data_hangang_list = sorted(list(data_hangang.items()))
        hangang_price = {}  # { '거래연도': [[x(역까지의 거리)], [y(평당 평균가)]] }
        for d in data_hangang_list:
            hangang_price[d[0]] = [[], []]
            for dps in d[1]:
                hangang_price[d[0]][0].append(dps[0])  # 역까지의 거리
                hangang_price[d[0]][1].append(dps[1])  # 평당 평균가
        return hangang_price

    def getComplexPrice(self):
        data_complex = {}  # data_region { 지역(구): (거래연도, 평당가격) }
        for x in data[['complexName', 'price', 'contactDate', 'supplyArea']].values:
            complexName = x[0]
            price = float(x[1])
            year = int(x[2].split('-')[0])
            supplyArea = float(x[3])
            if (complexName, year) in data_complex:
                data_complex[(complexName, year)].append(price / supplyArea)
            else:
                data_complex[(complexName, year)] = [price / supplyArea]
        for k, p in data_complex.items():
            p_avg = sum(p) / len(p)
            data_complex[k] = p_avg
        data_complex_list = sorted(list(data_complex.items()))
        complex_price = {}  # { '지역명': [[x(연도)], [y(평당 평균가)]] }
        for d in data_complex_list:
            if d[0][0] in complex_price:
                complex_price[d[0][0]][0].append(d[0][1])
                complex_price[d[0][0]][1].append(d[1])
            else:  # 구 이름      거래연도    가격
                complex_price[d[0][0]] = [[d[0][1]], [d[1]]]
        return complex_price

    def getBrandPrice(self):
        data_brand = {}  # data_brand { 건설사: (거래연도, 평당가격) }
        for x in data[['constructionCompanyName', 'price', 'contactDate', 'supplyArea']].values:
            brand = str(x[0])
            price = float(x[1])
            year = int(x[2].split('-')[0])
            supplyArea = float(x[3])
            if (brand, year) in data_brand:
                data_brand[(brand, year)].append(price / supplyArea)
            else:
                data_brand[(brand, year)] = [price / supplyArea]
        for k, p in data_brand.items():
            p_avg = sum(p) / len(p)
            data_brand[k] = p_avg
        data_brand_list = sorted(list(data_brand.items()))
        brand_price = {}  # { '브랜드명': [[x(연도)], [y(평당 평균가)]] }
        for d in data_brand_list:
            if d[0][0] in brand_price:
                brand_price[d[0][0]][0].append(d[0][1])
                brand_price[d[0][0]][1].append(d[1])
            else:  # 구 이름      거래연도    가격
                brand_price[d[0][0]] = [[d[0][1]], [d[1]]]
        return brand_price