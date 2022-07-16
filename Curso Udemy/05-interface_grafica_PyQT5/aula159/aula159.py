import sys
from design_code import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Redimensionar(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)
    
    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            'C:\\',
            options=QFileDialog.DontUseNativeDialog
        )
        
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))
    
    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.nova_img = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap(self.nova_img)
        self.inputLargura.setText(str(self.nova_img.width()))
        self.inputAltura.setText(str(self.nova_img.height()))
    
    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            'C:\\Users\\andre\\Desktop\\',
            options=QFileDialog.DontUseNativeDialog
        )
        self.nova_img.save(imagem, 'PNG')
        


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    redimensionar = Redimensionar()
    redimensionar.show()
    qt.exec_()
