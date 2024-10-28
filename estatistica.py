def estatistica(config):
    from configs import load_notes, save_notes
    from time import localtime

    #carregar json:
    lista = load_notes(config)[0]

    time = localtime()
    data_atual = data_to_(time)


    num_total_obj = len(lista)
    num_obj_ativos = 0
    num_obj_conc = 0
    num_obj_imp = 0
    obj_conc_tmp = 0
    obj_not_conc_tmp = 0
    obj_conc_semana = 0
    obj_conc_semana_ant = None


    for c in lista:
        # numero de objetivo ativos e concluidos:
        if c['Concluido']:
            num_obj_conc += 1
            data = data_atual.copy()
            data_calculos(7, data, 'dia')
            if  data_to_(c['Data de Conclusão']) - data_to_(data) >= 0:
                obj_conc_semana += 1


        else:
            num_obj_ativos += 1

        # numero de objetivos importantes:
        if c['Importante']:
            num_obj_imp += 1

            if c['Concluido'] and not c['Data Limite'] == None:
                data_conc = data_to_(c['Data de Conclusão'])
                data_lim = data_to_(c['Data Limite'])
                if (data_lim - data_conc) >= 0:
                    obj_conc_tmp += 1
                else:
                    obj_not_conc_tmp += 1

    dados = {'Total de Objetivos': num_total_obj, 'Objetivos ativos': num_obj_ativos, 'Concluidos': num_obj_conc,
             'Importantes': num_obj_imp, 'Concluidos a tempo': obj_conc_tmp, 'Não concluidos a tempo': obj_not_conc_tmp,
             'Objetivos concluidos na semana': obj_conc_semana, 'Objetivos concluidos da semana anterior': obj_conc_semana_ant}

    statistic_handler(dados)

    lista = load_notes(config)
    lista[2] = [dados]
    save_notes(config, lista)
    return dados

def statistic_handler(dados):
    per_conc_semana = 100
    try:
        if not dados['Objetivos concluidos da semana anterior'] == None:
            per_conc_semana = dados['Objetivos concluidos da semana'] / dados['Objetivos concluidos da semana anterior'] * 100
        per_obj_conc_tmp = dados['Concluidos a tempo'] / dados['Não concluidos a tempo'] * 100
        per_obj_ativo = dados['Objetivos ativos'] / dados['Total de Objetivos'] * 100
    except:
        per_obj_conc_tmp = 100
        per_obj_ativo = 100

    dados['% Objetivos concluidos da semana'] = per_conc_semana
    dados['% Objetivos ativos'] = per_obj_ativo
    dados['% Objetivos concluidos a tempo'] = per_obj_conc_tmp



def data_calculos(data1, data2, mod='data'):
    mon = [1, 3, 5, 7, 8, 10, 12] # meses com 31 dias
    if mod == 'dia':
        # data - dia
        data2[2] -= data1
        if data2[2] <= 0:
            data2[1] -= 1
            if data2[1] <= 0:
                data2[0] -= 1
                data2[1] = 12
            data = -data2[2]

            data2[2] = 30
            if data2[1] in mon: # meses com 31 dias
                data2[2] = 31
            elif data2[1] == 2:
                data2[2] = 28
                if (not data2[0] % 4 == 0 and data2[0] % 400 == 0) or (data2[0] % 4 == 0 and not data2[0] % 100 == 0):
                    # ano bissexto
                    data2[2] = 29
            data_calculos(data, data2, 'dia')

    else:
        # data - data:
        anos = data2[0] - data1[0]
        data = 0
        for c in range(1, anos):
            ano = data2[0] - c
            if (not ano % 4 == 0 and ano % 400 == 0) or (ano % 4 == 0 and not ano % 100 == 0):
                data += 366
            else:
                data += 365
            for c in range(1, data1[1] + 1):
                if c in mon:  # meses com 31 dias
                    data += 31
                elif c == 2:  # mes com 28 dia
                    if (not data1[0] % 4 == 0 and data1[0] % 400 == 0) or (
                            data1[0] % 4 == 0 and not data1[0] % 100 == 0):
                        # ano bissexto
                        data += 29
                    else:
                        data += 28
                else:
                    data += 30

def data_to_(data, mode='int'):
    c = ['', '', '', '']
    if data[1] < 10:
        c[0] = 0
    if data[2] < 10:
        c[1] = 0
    d = (f'{data[0]}{c[2]}{c[0]}{data[1]}{c[3]}{c[1]}{data[2]}')

    if mode == 'str':
        c[2], c[3] = '/', '/'
        return d
    else:
        return int(d)
