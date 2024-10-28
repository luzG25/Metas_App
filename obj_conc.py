def obj_conc(config):
    from configs import load_notes, save_notes
    from see_notes import pesquisador, show_notes
    from os import system
    defauts = [None, None, 'conc', None]

    # carregar JSON:
    lista = load_notes(config)

    # procurar objetivo:
    print('Concluindo Objetivo')
    pesquisar = input('Nome do Objetivo:')
    system('cls')
    conc = pesquisador(pesquisar, lista, defauts)

    # assinalar objetivo como concluido:
    conc['Concluido'] = True
    system('cls')
    show_notes([conc], defauts)

    # print(lista)

    # guardando o JSON:
    save_notes(config, lista)


'''from configs import load_configs
obj_conc(load_configs())'''
