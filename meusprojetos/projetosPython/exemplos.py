"""
Este arquivo é para fazer testes de códigos, antes de incorpora-los as sua respectivas
rotinas.
"""
from pacotes.formato import centro
from pacotes.utilitarios import pyhelp



pyhelp()

# Example (Hello, World):
# import tkinter
# from tkinter.constants import *
# tk = tkinter.Tk()
# frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
# frame.pack(fill=BOTH,expand=1)
# label = tkinter.Label(frame, text="Hello, World")
# label.pack(fill=X, expand=1)
# button = tkinter.Button(frame,text="Exit",command=tk.destroy)
# button.pack(side=BOTTOM)
# tk.mainloop()

# Exception

# try:
#     a = 'division by zero'
#     a = len(a) / 0
#     # print(a[0:8])
# except ZeroDivisionError:  # Exception as erro:
#     print(f'Erro: ')
# else:
#     print('OK')
# finally:
#     print('Fim')
# def centro(n):
#     return f'^{n}'


print('='*30)
print(f'{"Este é um texto":{centro(30)}}')
print('*'*30)
