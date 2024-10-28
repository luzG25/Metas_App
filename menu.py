def menu(config):
    from os import system
    from keyboard import is_pressed
    from time import sleep as sl
    from see_notes import see_notes
    from configs import configs
    from new_obj import new_obj
    from obj_conc import obj_conc
    from threading import Thread
    m0 = [' ', ' ', ' ', ' ', ' ', ' ']
    pos0(m0)
    cont = -1
    terminar = False

    while True:
        if terminar:
            break
        if is_pressed('down'):
            if cont == 5:
                cont = -1
            cont = cont + 1
            m0[cont] = '*'
            m0[cont - 1] = ' '
            system('cls')
            pos0(m0)
            sl(t_wait())

        elif is_pressed('up'):
            cont = cont - 1
            if cont < 0:
                cont = 5
                m0[0] = ' '
            m0[cont] = '*'
            if cont < 5:
                m0[cont + 1] = ' '
            system('cls')
            pos0(m0)
            sl(t_wait())

        elif is_pressed('enter'):
            sl(t_wait())
            if cont == 0:
                system('cls')
                Thread(target=new_obj, args=(config,)).start()
                terminar = True
            elif cont == 1:
                system('cls')
                print('new_categ')
                terminar = True
            elif cont == 2:
                system('cls')
                Thread(target=see_notes, args=(config,)).start()
                terminar = True
            elif cont == 3:
                system('cls')
                print('see_all')
            elif cont == 4:
                system('cls')
                obj_conc(config)
                Thread(target=obj_conc, args=(config,)).start()
                terminar = True
            elif cont == 5:
                system('cls')
                configs(config)
                Thread(target=configs, args=(config,)).start()
                terminar = True

        elif is_pressed('1'):
            sl(t_wait())
            system('cls')
            Thread(target=new_obj, args=(config,)).start()
            terminar = True
        elif is_pressed('2'):
            sl(t_wait())
            system('cls')
            print('new_categ')
        elif is_pressed('3'):
            sl(t_wait())
            system('cls')
            Thread(target=see_notes, args=(config,)).start()
            terminar = True
        elif is_pressed('4'):
            sl(t_wait())
            system('cls')
            print('see_all')
        elif is_pressed('5'):
            sl(t_wait())
            system('cls')
            obj_conc(config)
            Thread(target=obj_conc, args=(config,)).start()
        elif is_pressed('6'):
            sl(t_wait())
            system('cls')
            Thread(target=configs, args=(config,)).start()
            terminar = True


def pos0(m0):
    print(f'{m0[0]} Adicionar novo objetivo [1]')
    print(f'{m0[1]} Adicionar nova categoria [2]')
    print(f'{m0[2]} Ver notas [3]')
    print(f'{m0[3]} Ver todas as notas [4]')
    print(f'{m0[4]} Conclusão [5]')
    print(f'{m0[5]} Configurações [6]')

def t_wait():
    return 0.2


'''
from threading import Thread
from time import sleep
from configs import load_configs
Thread(target=menu, args=(load_configs()))
sleep(1000)
'''
from configs import load_configs
menu(load_configs())
