import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


class VentanaInicio(QMainWindow):

    def __init__(self):
        super(VentanaInicio, self).__init__()



if __name__ == '__main__':
    # Hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # creamos un objeto tipo VentanaInicio con el nombre de Ventana Inicio
    VentanaInicio = VentanaInicio()

    # hacer que el objeto VentanaLogin se vea
    VentanaInicio.show()

    # para terminar la aplicacion
    sys.exit(app.exec_())

