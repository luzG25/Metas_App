from PyQt5 import uic, QtWidgets
from configs import dl, save_notes, save_config, load_configs, load_notes
from threading import Thread
from time import sleep
configs = load_configs()
notes = [load_notes(configs)]

def mudar_password():
    print('mudar password')

def configs_menu():

    def aplicar_conf():
        configs[0] = menu[0].local_guardar_notas.text()
        configs[1] = menu[0].local_backup.text()
        configs[2] = menu[0].backup.isChecked()
        configs[5] = menu[0].criptografia.isChecked()
        configs[6] = menu[0].password.isChecked()
        Thread(target=save_config, args=(configs,)).start()
        print(configs)
        main_menu()

    def cancelar_conf():
        main_menu()

    menu[0] = uic.loadUi('configs.ui')
    menu[0].setWindowTitle('Configurações')

    menu[0].local_guardar_notas.setText(configs[0])
    menu[0].local_backup.setText(configs[1])
    menu[0].aplicar.clicked.connect(aplicar_conf)
    menu[0].mudar_password.clicked.connect(mudar_password)

    if configs[5]:
        menu[0].criptografia.setChecked(True)
    if configs[2]:
        menu[0].backup.setChecked(True)
    if configs[6]:
        menu[0].password.setChecked(True)
    menu[0].cancelar.clicked.connect(cancelar_conf)

    menu[0].show()

def ver_notas():
    menu[0] = uic.loadUi('ver_notas.ui')
    menu[0].setWindowTitle('Notas')
    menu[0].show()


def aplicar():
    nome = menu[0].nome.text()
    detalhes = menu[0].detalhes.text()
    categ = menu[0].categoria.text()
    subcateg = menu[0].subcategoria.text()
    importante = menu[0].importante.isChecked()
    datalimite = str(menu[0].datalimite.date())
    note = {'Nome': nome, 'Detalhes': detalhes,
            'Categoria': categ, 'Subcategoria': subcateg,
            'Importante': importante, 'Data Limite': dl(datalimite),
            'Data': ' '}
    notes[0][0].append(note)
    print(notes[0][0])
    Thread(target=save_notes, args=(configs, notes[0][0],)).start()
    main_menu()

def new_obj():
    menu[0] = uic.loadUi('new_note.ui')
    menu[0].setWindowTitle('Adicionar nova Nota')

    # setar datalimite para o dia atual

    menu[0].aplicar.clicked.connect(aplicar)
    menu[0].show()

def main_menu():
    menu[0] = uic.loadUi('menu.ui')
    menu[0].setWindowTitle('Notas')
    '''menu.atingidosdasemana.setValue(10) # setar valor da barra de progresso'''
    menu[0].new_note.clicked.connect(new_obj)
    menu[0].configs.clicked.connect(configs_menu)
    menu[0].see_note.clicked.connect(ver_notas)

    menu[0].show()

app = QtWidgets.QApplication([])

menu = [0]
main_menu()

app.exec()



