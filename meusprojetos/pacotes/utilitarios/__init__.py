from time import sleep


def lin():
    print('+=' * 24)


def lin1():
    print('\033[1;34m*=\033[m' * 26)


def titulo(msg):
    """
    Exibe uma mensagem formatada.
    :param msg: texto a ser exibido
    """
    c = len(msg) + 8
    print(corlinha('az'))
    print('*' * c)
    texto = f'\033[3:4m{fundo("az")}{msg}{fundo()}{corlinha("az")}'
    print(f'*   {texto}   *')
    print('*' * c)
    print(corlinha())


def leiaint(texto):
    """
    -> Lê uma string de entrada e faz a validação
    para aceitar apenas um valor numérico.
    :param texto: String a ser validada
    :return: n
    """
    while True:
        n = str(input(texto))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print(f'\033[1;31mERRO: Digite um número inteiro válido.\033[m')
    return n


def fundo(tipo=''):  # corfundo()
    """
    Altera a cor de fundo do texto:
    Cria um dicionário, que tem como chave as abreviaturas
    das cores e como valor o código referente a essas cores:
    br = branca, vm = vermelho, vd = verde, am = amarelo,
    az = azul, ma = magenta, ci = ciânico, cz = cinza.
    Se não for informado o parâmetro a função restaura as
    cores padrões do sistema.
    :param tipo: Opcional, quando não informado, restaura
    as cores padrões do sistema.
    :return: retorna o código da cor escolhida
    função criada por Eduardo A. M. Pessanha
    """
    cf = {'': '\033[m',  # - restaura cor padrão
          'br': '\033[1;7;30m',  # - fundo branco
          'vm': '\033[1;30;41m',  # - fundo vermelho
          'vd': '\033[1;30;42m',  # - fundo verde
          'am': '\033[1;30;42m',  # - fundo amarelo
          'az': '\033[1;30;44m',  # - fundo azul
          'mg': '\033[1;30;45m',  # - fundo magenta
          'ci': '\033[1;30;46m',  # - fundo ciânico
          'cz': '\033[1;30;47m'  # - fundo cinza
          }
    return cf[tipo]


def cortext(tipo):
    """
    Altera a cor do texto:
    br = branca, vm = vermelho, vd = verde, am = amarelo, az = azul
    ma = magenta, ci = ciânico, cz = cinza, 0 = restaura cor padrão
    :param tipo: indica qual a cor desejada:
    :return: retorna o código da cor escolhida
    função criada por Eduardo A. M. Pessanha
    """
    if tipo == 0:
        tipo = '\033[m'
    elif tipo == 'br':
        tipo = '\033[1;30m'
    elif tipo == 'vm':
        tipo = '\033[1;31m'
    elif tipo == 'vd':
        tipo = '\033[1;32m'
    elif tipo == 'am':
        tipo = '\033[1;33m'
    elif tipo == 'az':
        tipo = '\033[1;34m'
    elif tipo == 'mg':
        tipo = '\033[1;35m'
    elif tipo == 'ci':
        tipo = '\033[1;36m'
    elif tipo == 'cz':
        tipo = '\033[1;37m'
    return tipo


def cab(msg, cor='zr'):
    c = len(msg)
    print(fundo(cor), end='')
    print('*' * (c + 4))
    print(f'* {msg} *')
    print('*' * (c + 4))
    print(fundo(''), end='')


def corlinha(tipo=''): # corletra
    """
    Altera a cor do texto:
    Cria um dicionário, que tem como chave as abreviaturas
    das cores e como valor o código referente a essas cores:
    br = branca, vm = vermelho, vd = verde, am = amarelo,
    az = azul, ma = magenta, ci = ciânico, cz = cinza.
    Se não for informado o parâmetro a função restaura as
    cores padrões do sistema.
    :param tipo: Opcional, quando não informado, restaura
    as cores padrões do sistema.
    :return: retorna o código da cor escolhida
    função criada por Eduardo A. M. Pessanha
    """

    cl = {'': '\033[m',  # 0 - restaura cor padrão
          'br': '\033[1;30m',  # 1 - frente branco
          'vm': '\033[1;31m',  # 2 - frente vermelho
          'vd': '\033[1;32m',  # 3 - frente verde
          'am': '\033[1;33m',  # 4 - frente amarelo
          'az': '\033[1;34m',  # 5 - frente azul
          'mg': '\033[1;35m',  # 6 - frente magenta
          'ci': '\033[1;36m',  # 7 - frente ciânico
          'cz': '\033[1;37m'  # 8 - frente cinza
          }
    return cl[tipo]


def manual(func):
    cab(f"Acessando o manual do comando '{func}'", 'az')
    sleep(1)
    print(fundo('br'))
    help(func)
    print(fundo(), end='')
    sleep(6)


def pyhelp():
    while True:
        cab(' SISTEMA DE AJUDA PyHELP ', 'vd')
        nome = str(input('Função da biblioteca -> '))
        if nome.upper() == 'FIM':
            break
        manual(nome)
    cab(' ATÉ LOGO!', 'vm')
