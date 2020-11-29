import os
import sys
from PyQt5.QtWidgets import *
import pickle
from os.path import dirname
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
sys.path.append("..")
from modules.analyzer import Analyzer
plt.rcParams['font.family'] = 'D2Coding'

class AnalyzerWindow(QWidget):
    def __init__(self): 
        super().__init__()
        with open(dirname(__file__) + "/completers.pkl", "rb") as f:
            self.complexCompleter = pickle.load(f)
            self.brandCompleter = pickle.load(f)
            self.regionCompleter = pickle.load(f)
            self.yearItems = pickle.load(f)
        self.setUI()
        self.analyzer = Analyzer()

    def setUI(self):
        # leftLayout : canvas
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        # form : 연도
        formGroupBox1 = QGroupBox("주변 시설과의 거리에 따른 가격")
        formLayout = QFormLayout()
        self.year = QComboBox()
        self.year.addItems(list(map(str, self.yearItems)))
        self.stationButton = QPushButton("지하철 거리")
        self.hospitalButton = QPushButton("병원 거리")
        self.hangangButton = QPushButton("한강 거리")
        self.stationButton.clicked.connect(self.showStationPrice)
        self.hospitalButton.clicked.connect(self.showHospitalPrice)
        self.hangangButton.clicked.connect(self.showHangangPrice)
        formLayout.addRow(QLabel("연도:"), self.year)
        formLayout.addRow(self.stationButton)
        formLayout.addRow(self.hospitalButton)
        formLayout.addRow(self.hangangButton)
        formGroupBox1.setLayout(formLayout)

        # form : 지역별
        formGroupBox2 = QGroupBox("지역 별 가격 추이")
        formLayout = QFormLayout()
        self.regionName = QLineEdit()
        self.regionName.setCompleter(QCompleter(self.regionCompleter))
        self.regionButton = QPushButton("가격 추이")
        self.regionButton.clicked.connect(self.showRegionPrice)
        formLayout.addRow(QLabel("지역명:"), self.regionName)
        formLayout.addRow(self.regionButton)
        formGroupBox2.setLayout(formLayout)

        # form : 단지별
        formGroupBox3 = QGroupBox("단지 별 가격 추이")
        formLayout = QFormLayout()
        self.complexName = QLineEdit()
        self.complexName.setCompleter(QCompleter(self.complexCompleter))
        self.complexButton = QPushButton("가격 추이")
        self.complexButton.clicked.connect(self.showComplexPrice)
        formLayout.addRow(QLabel("단지명:"), self.complexName)
        formLayout.addRow(self.complexButton)
        formGroupBox3.setLayout(formLayout)

        # form : 건설사별
        formGroupBox4 = QGroupBox("건설사 별 가격 추이")
        formLayout = QFormLayout()
        self.brandName = QLineEdit()
        self.brandName.setCompleter(QCompleter(self.brandCompleter))
        self.brandButton = QPushButton("가격 추이")
        self.brandButton.clicked.connect(self.showBrandPrice)
        formLayout.addRow(QLabel("건설사명:"), self.brandName)
        formLayout.addRow(self.brandButton)
        formGroupBox4.setLayout(formLayout)

        # rightLayout : forms
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(formGroupBox1)
        rightLayout.addWidget(formGroupBox2)
        rightLayout.addWidget(formGroupBox3)
        rightLayout.addWidget(formGroupBox4)
        rightLayout.setStretchFactor(formGroupBox1, 2)
        rightLayout.setStretchFactor(formGroupBox2, 1)
        rightLayout.setStretchFactor(formGroupBox3, 1)
        rightLayout.setStretchFactor(formGroupBox4, 1)

        # Merge leftLayout and rightLayout (3: 1)
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 7)
        layout.setStretchFactor(rightLayout, 2)

        self.setLayout(layout)

    def showRegionPrice(self):
        regionName = self.regionName.text()
        year, price = self.analyzer.region_price[regionName]
        self.fig.clear()
        ax1 = self.fig.add_subplot(1, 1, 1)
        ax1.grid(b=True, ls=':')
        ax1.bar(year, price, color='#c02323')
        ax1.set_title(regionName, fontsize=18)
        ax1.set_xticks(year)
        ax1.set_xlabel('연도', fontsize=14)
        ax1.set_ylabel('평당 가격', fontsize=14)
        ax1.ticklabel_format(style='plain', useLocale=True)
        self.canvas.draw()

    def showStationPrice(self):
        year = int(self.year.currentText())
        dist, price = self.analyzer.station_price[year]
        self.fig.clear()
        ax1 = self.fig.add_subplot(1, 1, 1)
        ax1.scatter(dist, price, alpha=0.1)
        ax1.set_title(year)
        ax1.ticklabel_format(style='plain', useLocale=True)
        self.canvas.draw()

    def showHospitalPrice(self):
        year = int(self.year.currentText())
        dist, price = self.analyzer.hospital_price[year]
        self.fig.clear()
        ax1 = self.fig.add_subplot(1, 1, 1)
        ax1.scatter(dist, price, alpha=0.1)
        ax1.set_title(year)
        ax1.ticklabel_format(style='plain', useLocale=True)
        self.canvas.draw()

    def showHangangPrice(self):
        year = int(self.year.currentText())
        dist, price = self.analyzer.hangang_price[year]
        self.fig.clear()
        ax1 = self.fig.add_subplot(1, 1, 1)
        ax1.scatter(dist, price, alpha=0.1)
        ax1.set_title(year)
        ax1.ticklabel_format(style='plain', useLocale=True)
        self.canvas.draw()

    def showComplexPrice(self):
        complexName = self.complexName.text()
        year, price = self.analyzer.complex_price[complexName]
        self.fig.clear()
        ax1 = self.fig.add_subplot(1, 1, 1)
        ax1.grid(b=True, ls=':')
        ax1.plot(year, price, color='#c02323')
        ax1.set_title(complexName, fontsize=18)
        ax1.set_xticks(year)
        ax1.set_xlabel('연도', fontsize=14)
        ax1.set_ylabel('평당 가격', fontsize=14)
        ax1.ticklabel_format(style='plain', useLocale=True)
        self.canvas.draw()

    def showBrandPrice(self):
        brandName = self.brandName.text()
        year, price = self.analyzer.brand_price[brandName]
        self.fig.clear()
        ax1 = self.fig.add_subplot(1, 1, 1)
        ax1.grid(b=True, ls=':')
        ax1.plot(year, price, color='#c02323')
        ax1.set_title(brandName, fontsize=18)
        ax1.set_xticks(year)
        ax1.set_xlabel('연도', fontsize=14)
        ax1.set_ylabel('평당 가격', fontsize=14)
        ax1.ticklabel_format(style='plain', useLocale=True)
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AnalyzerWindow()
    ex.setWindowTitle('House Selling Price Recommendation Service(analyzer)')
    ex.setGeometry(200, 200, 1000, 600)
    ex.show()
    app.exec_()