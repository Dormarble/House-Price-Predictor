import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
sys.path.append(os.path.dirname(__file__))
from windows.analyzerwindow import AnalyzerWindow
from windows.predictorwindow import PredictorWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setWindowTitle('House Selling Price Recommendation Service')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(200, 200, 1000, 600)

        tabs = QTabWidget()
        predictor_tab = PredictorWindow()
        analyzer_tab = AnalyzerWindow()

        tabs.addTab(predictor_tab, 'Predictor')
        tabs.addTab(analyzer_tab, 'Analyzer')

        layout = QVBoxLayout()
        layout.addWidget(tabs)
        self.setLayout(layout)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())