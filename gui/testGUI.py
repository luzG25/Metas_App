from PyQt5 import uic, QtWidgets

def aplicar_conf():
    print('aplicar')
    if menu[0].criptografia.isChecked():
        print('checked')


def mudar_password():
    print('mudar password')


app = QtWidgets.QApplication([])

menu = [0]
menu[0] = uic.loadUi('configs.ui')
menu[0].setWindowTitle('Configurações')

menu[0].local_guardar_notas.setText('local')
menu[0].local_backup.setText('local')
menu[0].aplicar.clicked.connect(aplicar_conf)
menu[0].mudar_password.clicked.connect(mudar_password)

menu[0].criptografia.setChecked(True)

menu[0].show()

app.exec()

