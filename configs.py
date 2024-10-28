def load_configs():
    from cryptography.fernet import Fernet
    from json import loads
    dir = diretorio()

    count = -1
    while True:
        count += 1
        try:
            file = open(dir[count], 'rb')
            content = file.read()
            file.close()
            f = Fernet(app_key())
            content_d = f.decrypt(content)
            config = loads(content_d.decode())
            if count > 0:
                saver_opener(dir, content, 'wb')
            return config

        except:
            if count > 2:
                return defaut_configs(True)

def defaut_configs(keep_usage=False):
    from os import makedirs

    # configuração padrão:
    local_notes = 'notes.json'
    local_backup = 'backup_notes.json'
    backup = False
    dir_backup = None
    user = None
    cripto = False
    password = False


    # gravando as configurações
    try:
        makedirs('data/')
    except:
        None
    config = [local_notes, local_backup, backup, dir_backup, user, cripto, password]

    # salvar configurações:
    save_config(config)

    if keep_usage:
        return config

def save_config(config):
    from cryptography.fernet import Fernet
    from json import dumps
    dir = diretorio()

    # transformar json em string:
    content = dumps(config, ensure_ascii=False)

    # criptografar configs:
    f = Fernet(app_key())
    content = f.encrypt(content.encode())
    saver_opener(dir, content, 'wb')

def saver_opener(dir, content, mod):
    for c in range(0, 3):
        try:
            file = open(dir[c], mod)
            file.write(content)
            file.close()

        except:
            None


def app_key():
    key = b'DAAiGHm_M3nNyTeaIRKT72T9ogHw3WWwDS2FgBXfp5s='
    return key

def diretorio():
    return ['data/config.cf', 'data/config0.cf', 'data/config1.cf']

def submenu(m1, imp, obj):

    print('CONFIGURAÇÕES:')
    print(f' {m1[0]}Local para Guardar Notas: {obj[0]}')
    print(f' {m1[1]}Nome de Usuário: {obj[4]}')

    if imp[0] == 'x':
        obj[2] = True
    print(f' {m1[2]}Backup: [{imp[0]}]SIM / [{imp[1]}]NÃO')
    if imp[0] == 'x':
        print(f' {m1[3]}Local para Backup: {obj[1]}')

    if imp[2] == 'x':
        obj[5] = True
    print(f' {m1[4]}Criptografia: [{imp[2]}]SIM / [{imp[3]}]NÃO')

    if imp[4] == 'x':
        obj[6] = True
    print(f' {m1[5]}Password: [{imp[4]}]SIM / [{imp[5]}]NÃO')
    if imp[4] == 'x':
        print(f' {m1[6]}Mudar Password')

    print(f' {m1[7]}Aplicar.')

def mudar_password(config):
    from hashlib import sha256
    # verificar antiga palavra passe
    old_pass = input('Password atual: ')

    if len(config) < 8:
        config.append(old_pass)
    else:
        config[7] = old_pass

    pass_to_hash(config)
    notes = load_notes(config)

    # inserir nova palavra-passe:
    new_pass = input('Nova Password: ')
    config[7] = new_pass

    pass_to_hash(config)
    save_notes(config, notes)
    print('Password Mudada com Sucesso!')

def aplicar(config):
    if len(config) > 7:
        config.pop()

    save_config(config)
    print('Configurações Salvas')


def configs(config):
    from menu import menu
    from keyboard import is_pressed as p
    from menu import t_wait
    from time import sleep as sl
    from os import system
    from threading import Thread
    m1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', -1, -1]
    imp = [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x']
    t_wait = t_wait()

    submenu(m1, imp, config)

    if config[2]:
        imp[0] = 'x'
        imp[1] = ' '
    if config[6]:
        imp[2] = 'x'
        imp[3] = ' '
    if config[6]:
        imp[4] = 'x'
        imp[5] = ' '

    terminar_conf = False
    cont = -1
    while True:
        if terminar_conf:
            break
        if p('down'):
            if cont == 7:
                m1[7] = ' '
                cont = -1
            cont = cont + 1
            m1[cont] = '*'
            m1[cont - 1] = ' '
            system('cls')
            submenu(m1, imp, config)
            sl(t_wait)

        elif p('up'):
            cont = cont - 1
            if cont < 0:
                cont = 7
                m1[0] = ' '
            m1[cont] = '*'
            if cont < 7:
                m1[cont + 1] = ' '
            system('cls')
            submenu(m1, imp, config)
            sl(t_wait)


        # enter
        elif p('enter'):
            sl(t_wait)
            if cont == 0:
                input()
                system('cls')
                config[0] = input('Local para guardar notas: ')
                t = config[0]
                config[3] = t[:t.find('.')-1] + '0' + t[t.find('.'):]
                print(config[3])
                del t
                configs(config)

            elif cont == 1:
                input()
                system('cls')
                config[4] = input('Nome do Usuário: ')
                configs(config)

            elif cont == 3:
                input()
                system('cls')
                config[1] = input('Local de backup: ')
                configs(config)

            elif cont == 6:
                input()
                system('cls')
                mudar_password(config)
                configs(config)

            elif cont == 7:
                input()
                system('cls')
                aplicar(config)



        #backup
        elif p('right') and cont == 2:
            imp[0] = ' '
            imp[1] = 'x'
            sl(t_wait)
            system('cls')
            submenu(m1, imp, config)

        elif p('left') and cont == 2:
            imp[0] = 'x'
            imp[1] = ' '
            sl(t_wait)
            system('cls')
            submenu(m1, imp, config)

        # criptografia
        elif p('right') and cont == 4:
            imp[2] = ' '
            imp[3] = 'x'
            sl(t_wait)
            system('cls')
            submenu(m1, imp, config)

        elif p('left') and cont == 4:
            imp[2] = 'x'
            imp[3] = ' '
            sl(t_wait)
            system('cls')
            submenu(m1, imp, config)

        # password
        elif p('right') and cont == 5:
            imp[4] = ' '
            imp[5] = 'x'
            sl(t_wait)
            system('cls')
            submenu(m1, imp, config)

        elif p('left') and cont == 5:
            imp[4] = 'x'
            imp[5] = ' '
            sl(t_wait)
            system('cls')
            submenu(m1, imp, config)

def load_notes(config):
    from cryptography.fernet import Fernet
    from json import loads, load

    # criptografia ativado e password:
    if config[5] and config[6]:
        try:
            # carregar e decodificar
            file = open(config[0], 'rb')
            content = file.read()
            file.close()
            f = Fernet(config[7].encode())
            content_d = f.decrypt(content)
            notas = loads(content_d.decode())

            return notas

        except:
            try:
                file = open(config[3], 'rb')
                content = file.read()
                file.close()
                f = Fernet(config[7].encode())
                content_d = f.decrypt(content)
                notas = loads(content_d.decode())

                return notas

            except:
                print('ficheiro corrompido!, ou não existente'.upper())
                return [[]]

     # criptografia ativado
    elif config[5]:
        try:
            # carregar e decodificar
            file = open(config[0], 'rb')
            content = file.read()
            file.close()
            f = Fernet(app_key())
            content_d = f.decrypt(content)
            notas = loads(content_d.decode())

            return notas

        except:
            try:
                file = open(config[3], 'rb')
                content = file.read()
                file.close()
                f = Fernet(app_key())
                content_d = f.decrypt(content)
                notas = loads(content_d.decode())

                return notas

            except:
                print('ficheiro corrompido, ou não existente!'.upper())
                return [[]]
    # criptografia desligado:
    else:
        try:
            file = open(config[0], 'r', encoding='utf-8')
            notas = load(file)
            file.close()
            return notas

        except:
            try:
                file = open(config[3], 'r', encoding='utf-8')
                notas = load(file)
                file.close()
                return notas
            except:
                print('Ficheiro corrompido, ou não existente!'.upper())
                return [[]]

def save_notes(config, notes):
    from cryptography.fernet import Fernet
    from json import dumps, dump



    # criptografia ativado e password:
    if config[5] and config[6]:
        content = dumps(notes, ensure_ascii=False)
        f = Fernet(config[7])
        content = f.encrypt(content.encode())
        saver_opener([config[0], config[3], config[1]], content, 'wb')
        return 'Notas salvas com sucesso'

    # criptografia ativado:
    elif config[5]:
        content = dumps(notes, ensure_ascii=False)
        f = Fernet(app_key())
        content = f.encrypt(content.encode())
        saver_opener([config[0], config[3], config[1]], content, 'wb')
        return 'Notas salvas com Sucesso!'

    # criptografia desativado:
    else:
        # print(config)
        try:
            dirs = [config[0], config[3], config[1]]
            for c in dirs:
                # print(c)
                file = open(c, 'w', encoding='utf-8')
                dump(notes, file)
                file.close()

            print('Notas salvas com Sucesso!')

        except:
            print('Erro em Guardar!')

def pass_to_hash(config):
    from hashlib import sha256

    # tranformar palavra em hash:
    hash = sha256(config[7].encode()).hexdigest()
    config[7] = (hash[:43] + '=').encode()


def dl(datalimite):
    dl = datalimite[datalimite.index('('):]
    dl1 = int(dl[1:dl.index(',')].strip())
    dl = dl[dl.index(',')+1:]
    dl2 = int(dl[:dl.index(',')].strip())
    dl = dl[dl.index(',')+1:]
    return [dl1, dl2, int(dl[:dl.index(')')].strip())]

#print(defaut_configs(True))
#configs(load_configs())

def saving_notes(configs, note):
    print(configs, '\n', note)
    notes = load_notes(configs)
    notes[0].append(note)
    save_notes(configs, notes)

