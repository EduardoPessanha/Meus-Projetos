# from pacotes.numeros import fatorial, dobro
import pacotes.numeros
import pacotes.utilitarios

num = int(input('Digite um valor: '))
fat = pacotes.numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {pacotes.numeros.dobro(num)}')


pacotes.utilitarios.pyhelp()
