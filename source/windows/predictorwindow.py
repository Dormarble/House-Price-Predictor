import os
import sys
import pickle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from os.path import dirname
sys.path.append("..")
from modules.predictor import Predictor
from modules.analyzer import Analyzer

class PredictorWindow(QWidget):
    def __init__(self):
        super().__init__()
        with open(dirname(__file__) + '/comboBoxItems.pkl', 'rb') as f:
            self.addressItems = pickle.load(f)
            self.complexNameItems = pickle.load(f)
            self.supplyAreaItems = pickle.load(f)
        self.setUI()
        self.predictor_model = Predictor()
        self.analyzer = Analyzer()

    def setUI(self):
        # canvas
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        # title label
        title_label = QLabel("🏠 예상 가격 🏠")
        title_label.setFont(QFont('맑은 고딕', 20))
        # result text
        self.result = QTextEdit()
        self.result.setReadOnly(True)
        self.result.setFont(QFont('맑은 고딕', 30))

        # left layout
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)
        leftLayout.addWidget(title_label)
        leftLayout.addWidget(self.result)

        # form
        formGroupBox = QGroupBox("House Information")
        formLayout = QFormLayout()
        # 주소(시, 구, 동)
        self.address = QComboBox()
        self.address.addItem("-")
        self.address.addItems(sorted(self.addressItems))
        self.address.currentTextChanged.connect(self.addressChanged)
        # 상세주소(단지)
        self.complexName = QComboBox()
        self.complexName.currentTextChanged.connect(self.complexNameChanged)
        self.supplyArea = QComboBox()           # 평 수
        self.floor = QSpinBox()                 # 층 수
        self.recent_price = QLineEdit()         # 매입가
        self.recent_contact_date = QLineEdit()  # 매입일
        self.sell_date = QLineEdit()            # 매매 예정일
        formLayout.addRow(QLabel("주소(시, 구, 동)"), self.address)
        formLayout.addRow(QLabel("상세주소(단지명)"), self.complexName)
        formLayout.addRow(QLabel("평 수:"), self.supplyArea)
        formLayout.addRow(QLabel("층 수:"), self.floor)
        formLayout.addRow(QLabel("매입가:"), self.recent_price)
        formLayout.addRow(QLabel("매입일:"), self.recent_contact_date)
        formLayout.addRow(QLabel("매매 예정일:"), self.sell_date)
        formGroupBox.setLayout(formLayout)

        self.predictButton = QPushButton("predict")
        self.predictButton.clicked.connect(self.predictButtonClicked)

        # frame
        img = QPixmap(dirname(__file__) + "/title_img.PNG")
        img = img.scaledToWidth(450)
        img = img.scaledToHeight(300)
        frame = QLabel()
        frame.setPixmap(img)

        # Right Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(frame)
        rightLayout.addWidget(formGroupBox)
        rightLayout.addWidget(self.predictButton)

        # Merge leftLayout and rightLayout (5: 4)
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 5)
        layout.setStretchFactor(rightLayout, 4)

        self.setLayout(layout)

    def predictButtonClicked(self):
        if self.updateResult():
            self.showComplexPrice()

    def updateResult(self):
        if self.address.currentText() == '-' or \
            self.complexName.currentText() == '-' or \
            self.supplyArea.currentText() == '-' or \
            self.floor.text() == "0" or \
            not self.recent_price.text() or\
            not self.recent_contact_date.text() or \
            not self.sell_date.text():
            return False

        p = self.predictor_model.predict(
            self.complexName.currentText(),
            float(self.supplyArea.currentText()),
            self.address.currentText(),
            int(self.recent_price.text()),
            self.recent_contact_date.text(),
            int(self.floor.text()),
            self.sell_date.text()
        )
        distStation, distHospital, distHangang = self.predictor_model.get_dist()
        self.result.setFont(QFont('맑은 고딕', 30))
        self.result.clear()
        ret = ""
        if distStation < 500:
            self.result.setFont(QFont('맑은 고딕', 15))
            ret = ret + "[역세권입니다.] "
        if distHangang < 1000:
            self.result.setFont(QFont('맑은 고딕', 15))
            ret = ret + "[한강에 가깝습니다.]"
        self.result.append(ret)
        p //= 10000
        if p // 10000:
            self.result.append(f'{p // 10000}억 {p % 10000}만원')
        else:
            self.result.append(f'{p}만원')
        return True

    def showComplexPrice(self):
        complexName = self.complexName.currentText()
        self.fig.clear()
        if complexName not in self.analyzer.complex_price:
            self.canvas.draw()
            return
        year, price = self.analyzer.complex_price[complexName]
        ax1 = self.fig.add_subplot(1, 1, 1)
        ax1.grid(b=True, ls=':')
        ax1.plot(year, price, color='#c02323')
        ax1.set_title(complexName, fontsize=18)
        ax1.set_xticks(year)
        ax1.set_xlabel('연도', fontsize=14)
        ax1.set_ylabel('평당 가격', fontsize=14)
        ax1.ticklabel_format(style='plain', useLocale=True)
        self.canvas.draw()

    def addressChanged(self):
        address = self.address.currentText()
        self.complexName.disconnect()
        self.complexName.clear()
        self.complexName.currentTextChanged.connect(self.complexNameChanged)
        self.supplyArea.clear()
        if address != "-":
            self.complexName.addItem("-")
            self.complexName.addItems(sorted(self.complexNameItems[address]))

    def complexNameChanged(self):
        complexName = self.complexName.currentText()
        address = self.address.currentText()
        self.supplyArea.clear()
        if complexName != "-":
            self.supplyArea.addItem("-")
            self.supplyArea.addItems(sorted(map(str, self.supplyAreaItems[(address, complexName)])))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PredictorWindow()
    ex.setWindowTitle('House Selling Price Recommendation Service(predictor)')
    ex.setGeometry(200, 200, 1000, 600)
    ex.show()
    app.exec_()