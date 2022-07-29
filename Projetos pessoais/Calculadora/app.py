import sys
from calc_design import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from math import pi, sqrt, sin, cos, tan, factorial, log, log10


class Calculadora(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
    
        self.btn_0.clicked.connect(lambda: self.action('0'))
        self.btn_1.clicked.connect(lambda: self.action('1'))
        self.btn_2.clicked.connect(lambda: self.action('2'))
        self.btn_3.clicked.connect(lambda: self.action('3'))
        self.btn_4.clicked.connect(lambda: self.action('4'))
        self.btn_5.clicked.connect(lambda: self.action('5'))
        self.btn_6.clicked.connect(lambda: self.action('6'))
        self.btn_7.clicked.connect(lambda: self.action('7'))
        self.btn_8.clicked.connect(lambda: self.action('8'))
        self.btn_9.clicked.connect(lambda: self.action('9'))
        self.btn_dot.clicked.connect(lambda: self.action('.'))
        self.btn_open.clicked.connect(lambda: self.action('('))
        self.btn_close.clicked.connect(lambda: self.action(')'))
        self.btn_plus.clicked.connect(lambda: self.action('+'))
        self.btn_min.clicked.connect(lambda: self.action('-'))
        self.btn_mult.clicked.connect(lambda: self.action('*'))
        self.btn_div.clicked.connect(lambda: self.action('/'))
        self.btn_squared.clicked.connect(lambda: self.action('**2'))
        self.btn_cub.clicked.connect(lambda: self.action('**3'))
        self.btn_pi.clicked.connect(lambda: self.action(f'{round(pi, 8)}'))
        self.btn_sqrt.clicked.connect(lambda: self.action('sqrt('))
        self.btn_sin.clicked.connect(lambda: self.action('sin('))
        self.btn_cos.clicked.connect(lambda: self.action('cos('))
        self.btn_tan.clicked.connect(lambda: self.action('tan('))
        self.btn_fact.clicked.connect(lambda: self.action('factorial('))
        self.btn_ln.clicked.connect(lambda: self.action('log('))
        self.btn_log.clicked.connect(lambda: self.action('log10('))
        self.btn_eq.clicked.connect(lambda: self.evaluate())
        self.btn_dell.clicked.connect(lambda: self.display.setText(self.display.text()[:-1]))
        self.btn_clear.clicked.connect(lambda: self.display.setText(''))
        
    def action(self, btn):
        self.display.setText(self.display.text() + btn)
        
    def evaluate(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        
        except Exception as erro:
            self.display.setText('MATH ERROR')
        


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calculadora = Calculadora()
    calculadora.show()
    qt.exec_()
