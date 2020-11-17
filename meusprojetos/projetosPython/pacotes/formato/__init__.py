def titulo(msg):
    """
    Exibe uma mensagem formatada.
    :param msg: texto a ser exibido
    """
    c = len(msg) + 8
    print(corletra('az'))
    print('*' * c)
    texto = f'\033[3:4m{corfundo("az")}{msg}{corfundo()}{corletra("az")}'
    print(f'*   {texto}   *')
    print('*' * c)
    print(corletra())


def corfundo(tipo=''):
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


def corletra(tipo=''):
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


def cab(msg, cor='zr'):
    """
    -> Formata um texto centralizado entre duas linhas
    :param msg:
    Texto a ser exibido
    :param cor:
    Cor de fundo do texto, caso a cor não seja
    informada, será usada a cor padrão do sistema.
    :return:
    Sem retorno
    """
    c = len(msg)
    print(corfundo(cor), end='')
    print('*' * (c + 4))
    print(f'* {msg} *')
    print('*' * (c + 4))
    print(corfundo(''), end='')


def centro(n):
    return f'^{n}'
