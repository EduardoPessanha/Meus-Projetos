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


def leiafloat():
    return