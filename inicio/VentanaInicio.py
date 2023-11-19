import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QFormLayout, QHBoxLayout, QPushButton


class VentanaInicio(QMainWindow):

    def __init__(self):

        # Caracteristicas de la ventana principal
        super(VentanaInicio, self).__init__()
        self.setWindowTitle("Animal city")
        self.setWindowIcon(QtGui.QIcon('../imagenes/logo2.png'))
        self.setFixedSize(950, 550)

        self.fondo = QLabel(self)

        self.horizontal = QHBoxLayout()

        self.ladoIzquierdo = QFormLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Bienvenidos")
        self.letrero1.setStyleSheet("color: #000080;")
        self.ladoIzquierdo.addRow(self.letrero1)
        self.setLayout(self.horizontal)
        self.horizontal.addLayout(self.ladoIzquierdo)
        self.fondo.setLayout(self.horizontal)


        #self.horizontal.addWidget(QPushButton("left-Most"))
        #self.horizontal.addWidget(QPushButton("Center"), 1)
        #self.horizontal.addWidget(QPushButton("Right-Most"), 2)
        #self.lado1 = QFormLayout()
        #self.letrero = QLabel()
        #self.letrero.setText("Hola")
        #self.letrero.setStyleSheet("color: #000080;")
        #self.lado1.addRow(self.letrero)
        #self.setLayout(self.horizontal)
        #self.horizontal.addLayout(self.lado1)

        #self.fondo.setLayout(self.horizontal)



if __name__ == '__main__':
    # Hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # creamos un objeto tipo VentanaInicio con el nombre de Ventana Inicio
    VentanaInicio = VentanaInicio()

    # hacer que el objeto VentanaLogin se vea
    VentanaInicio.show()

    # para terminar la aplicacion
    sys.exit(app.exec_())

