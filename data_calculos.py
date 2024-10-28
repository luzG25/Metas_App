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


