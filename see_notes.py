def see_notes(config):
    from configs import load_notes
    from os import system

    #carregando o JSON
    lista = load_notes(config)

    defauts = [' ', ' x', -1, False]
    show_notes(lista, defauts)

'''    while True:
        pesquisar = input('Pesquisar: ')
        system('cls')
        print('#', pesquisar.upper())
        pesquisador(pesquisar, lista, defauts)'''


def show_notes(lista, defauts):
    for c in lista:
        if c['Concluido'] == False or defauts[2] == 'conc':
            print(f'{c["Nome"]}')
            print(f'  *Detalhes: {c["Detalhes"]}')
            print(f'  *Categoria: {c["Categoria"]}')
            print(f'  *Subcategoria: {c["Subcategoria"]}')
            if c["Importante"]:
                defauts[0] = 'x'
                defauts[1] = ' '
            elif c["Importante"] == False:
                defauts[0] = ' '
                defauts[1] = 'x'
            print(f'  *Importante:  [{defauts[0]}]SIM / [{defauts[1]}]NÃO')
            if c['Data Limite'] != None:
                print(f'  *Data Limite: {c["Data Limite"]}')
            print(f'  *Data: {c["Data"]["dia"]} ás {c["Data"]["hora"]}')

            # coluna de concluido:
            if defauts[2] == 'conc':
                if c["Concluido"]:
                    defauts[0] = 'x'
                    defauts[1] = ' '
                elif not c["Concluido"]:
                    defauts[0] = ' '
                    defauts[1] = 'x'
                print(f'  *Concluido:  [{defauts[0]}]SIM / [{defauts[1]}]NÃO')

            print('\n')
            print('==' * 50)

def pesquisador(pesquisar, lista, defauts):
    count = -1
    for c in lista:
        count += 1
        if (pesquisar in c['Nome'] or pesquisar in c['Detalhes'] or pesquisar in c['Data']) and defauts[2] != 'conc' or (pesquisar in c['Nome'] and defauts[2] == 'conc'):
            if defauts is list:
                dados = [lista[count]]
                show_notes(dados, defauts)
            elif defauts[2] == 'conc':
                return lista[count]


'''from configs import load_configs
see_notes(load_configs())'''
