def new_obj(config, objet='0'):
    from time import localtime, sleep as sl
    from os import system
    from keyboard import is_pressed
    from menu import t_wait

    tempo = localtime()
    data_limite = [0, tempo[1], tempo[0], -1]

    imp = [' ', 'x']
    t_wait = t_wait()

    m1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    cont = -1
    if objet == '0':
        objet = obj()

    param(m1, imp, data_limite, objet)
    while True:
        if is_pressed('down') and data_limite[3] == -1:
            if cont == 6:
                cont = -1
                m1[6] = ' '
            cont = cont + 1
            m1[cont] = '*'
            m1[cont - 1] = ' '
            sl(t_wait)
            system('cls')
            param(m1, imp, data_limite, objet)

        elif is_pressed('up') and data_limite[3] == -1:
            cont = cont - 1
            if cont < 0:
                cont = 6
                m1[0] = ' '
            m1[cont] = '*'
            if cont < 6:
                m1[cont + 1] = ' '
            sl(t_wait)
            system('cls')
            param(m1, imp, data_limite, objet)



        #importancia
        elif is_pressed('right') and cont == 4:
            imp = [' ', 'x']
            sl(t_wait)
            system('cls')
            param(m1, imp, data_limite, objet)
        elif is_pressed('left') and cont == 4:
            imp = ['x', ' ']
            sl(t_wait)
            system('cls')
            param(m1, imp, data_limite, objet)

        #data limite
        elif is_pressed('right') and cont == 5:
            data_limite[3] += 1
            if data_limite[3] > 2:
                data_limite[3] = -1
            sl(t_wait)
        elif is_pressed('left') and cont == 5:
            data_limite[3] -= 1
            if data_limite[3] < -1:
                data_limite[3] = 2
            sl(t_wait)
        elif is_pressed('up') and str(data_limite[3]) in '012' and cont == 5:
            data_limite[data_limite[3]] += 1
            sl(t_wait)
            system('cls')
            param(m1, imp, data_limite, objet)

        elif is_pressed('down') and str(data_limite[3]) in '012' and cont == 5:
            data_limite[data_limite[3]] -= 1
            sl(t_wait)
            system('cls')
            param(m1, imp, data_limite, objet)

        # enter
        elif is_pressed('enter'):
            sl(t_wait)
            if cont == 0:
                input()
                system('cls')
                objet['Nome'] = input('Nome: ')
                system('cls')
                new_obj(config, objet)
            elif cont == 1:
                input()
                system('cls')
                objet['Detalhes'] = input('Detalhes: ')
                system('cls')
                new_obj(config, objet)
            elif cont == 2:
                input()
                system('cls')
                objet['Categoria'] = input('Categoria: ')
                system('cls')
                new_obj(config, objet)
            elif cont == 3:
                input()
                system('cls')
                objet['Subcategoria'] = input('Subcategoria: ')
                system('cls')
                new_obj(config, objet)
            elif cont == 6:
                input()
                system('cls')
                validador(tempo, data_limite, objet, imp, config)
                #print(objet)


def param(m1, imp, data_limite, obj):
    print('NOVO OBJETIVO:')
    print(f' {m1[0]}Nome: {obj["Nome"]}')
    print(f' {m1[1]}Detalhes: {obj["Detalhes"]}')
    print(f' {m1[2]}Categoria: {obj["Categoria"]}')
    print(f' {m1[3]}Subcategoria: {obj["Subcategoria"]}')
    print(f' {m1[4]}Importante: [{imp[0]}]SIM / [{imp[1]}]NÃO')
    print(f' {m1[5]}Data Limite (se houver): {data_limite[0]}/{data_limite[1]}/{data_limite[2]}')
    print(f' {m1[6]}Validar.')

def validador(tempo, data_limite, obj, imp, config):
    from configs import load_notes, save_notes
    if imp[0] == 'x':
        obj['Importante'] = True
        if data_limite[0] > 0:
            obj['Data Limite'] = f'{data_limite[0]}/{data_limite[1]}/{data_limite[2]}'
    obj['Data'] = {'dia': f'{tempo[2]}/{tempo[1]}/{tempo[0]}', 'hora': f'{tempo[3]}:{tempo[4]}'}

    # carregando o JSON:
    lista = load_notes(config)

    # adicionando os novos dados e gravando o JSON:
    lista.append(obj)
    save_notes(config, lista)


def obj():
    return {'Nome': '', 'Detalhes': '', 'Categoria': '', 'Subcategoria': '', 'Importante': False, 'Data Limite': None, 'Data': None, 'Concluido': False}

'''
from threading import Thread
from configs import load_configs
from time import sleep
t = Thread(target=new_obj, args=(load_configs(), obj())).start()
sleep(1000)
'''

