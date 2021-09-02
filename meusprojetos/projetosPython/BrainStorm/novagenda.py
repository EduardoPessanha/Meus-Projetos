# -*- coding: utf-8 -*-
"""
    Agenda de Telefone e endereço
"""

from tkinter import *
from tkinter import ttk
from libagenda import *


''' Definindo a tela: '''
tela = Tk()
tela.title('Minha Agenda')
tela.configure(padx=5, pady=10, borderwidth=4, relief='groove',
               background='#cccccc')
tela.geometry('1100x540')

"""
    -Definindo os elementos da tela:
"""
# _ Elementos do formulário:

# * Elemento LabelFrame:

frame1 = LabelFrame(tela, text='Contatos', font=(
    'Ebrima', 10, 'bold'), width=1050, height=260)
frame2 = LabelFrame(tela, text='Novos Contatos',
                    font=('Ebrima', 10, 'bold'), width=1050, height=80)
frame3 = LabelFrame(tela, text='Pesquisar Contatos', font=(
    'Ebrima', 10, 'bold'), width=1050, height=80)

# * Posicionando os LabelFrames:

frame1.grid(column=0, row=0, padx=10, pady=5, sticky='w')
frame2.grid(column=0, row=1, padx=10, pady=5, sticky='w')
frame3.grid(column=0, row=2, padx=10, pady=5, sticky='w')

# > Elemento Treeview - LabelFrame -> frame1:

colunas = ['id', 'nome', 'telefone', 'e-mail',
           'endereco', 'cidade', 'estado', 'observacao']
treev = ttk.Treeview(frame1, columns=colunas, show='headings')

# > Definindo uma barra de rolagem vertical(Scrollbar):

scrollbarv = ttk.Scrollbar(frame1, orient='vertical', command=treev.yview)
treev.configure(yscroll=scrollbarv.set)

# > ***** Definindo o tamanho das colunas *****

treev.column('id', width=35, minwidth=10, stretch=True, anchor=CENTER)
treev.column('nome', width=170, minwidth=0, stretch=True)
treev.column('telefone', width=115, minwidth=0, stretch=True)
treev.column('e-mail', width=150, minwidth=0, stretch=True)
treev.column('endereco', width=200, minwidth=0, stretch=True)
treev.column('cidade', width=100, minwidth=0, stretch=True)
treev.column('estado', width=35, minwidth=0, stretch=True, anchor=CENTER)
treev.column('observacao', width=235, minwidth=0, stretch=True)

# > ****** Definindo os cabeçalhos das colunas ******

treev.heading('id', text='ID')
treev.heading('nome', text='Nome')
treev.heading('telefone', text='Telefone')
treev.heading('e-mail', text='Email')
treev.heading('endereco', text='Endereço')
treev.heading('cidade', text='Cidade')
treev.heading('estado', text='UF')
treev.heading('observacao', text='Nota')

# > ****** Posicionando o elemento Treeview: ******

treev.grid(column=0, row=1, padx=True, pady=True)
scrollbarv.grid(column=1, row=1, sticky='ns')

# _ Elementos label e texto (Entry) do LabelFrame frame2:

# _ Elemento label do frame2:

lblnome = Label(frame2, text='Nome: ', width=8, anchor='w')  # , bg='#0ff'
lblfone = Label(frame2, text='Telefone: ', width=8, anchor='w')
lblmail = Label(frame2, text='E-mail: ', width=8, anchor='w')
lblend = Label(frame2, text='Endereço: ', width=8, anchor='w')
lblcid = Label(frame2, text='Cidade: ', width=8, anchor='w')
lbluf = Label(frame2, text='UF: ', width=8, anchor='w')
lblobs = Label(frame2, text='Nota: ', width=4, anchor='w')

# _ Elemento texto (Entry) do frame2:

txtnome = Entry(frame2, width=25, font=(
    'Ebrima', 12), bd=1, justify='left')
txtfone = Entry(frame2, width=15, font=(
    'Ebrima', 12), bd=1, justify='left')
txtmail = Entry(frame2, width=25, font=(
    'Ebrima', 12), bd=1, justify='left')
txtend = Entry(frame2, width=30, font=(
    'Ebrima', 12), bd=1, justify='left')
txtcid = Entry(frame2, width=20, font=(
    'Ebrima', 12), bd=1, justify='left')
txtuf = Entry(frame2, width=2, font=('Ebrima', 12), bd=1, justify='left')
txtobs = Text(frame2, width=29, height=4, font=('Ebrima', 12), bd=1)

reglist = [txtnome, txtfone, txtmail, txtend, txtcid, txtuf, txtobs]

# _ Elemento botão do LabelFrame frame2:

btninser = Button(frame2, text='Inserir', width=10, bg='#b8b1e0',
                  font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised', command=lambda: inserir(reglist))

# _ Posicionando os elementos dentro do frame2:

lblnome.grid(column=0, row=1)
txtnome.grid(column=1, row=1, padx=5, pady=2, sticky='w')
lblfone.grid(column=0, row=2)
txtfone.grid(column=1, row=2, padx=5, pady=2, sticky='w')
lblmail.grid(column=0, row=3)
txtmail.grid(column=1, row=3, padx=5, pady=2, sticky='w')
lblend.grid(column=2, row=1)
txtend.grid(column=3, row=1, padx=5, pady=2, sticky='w')
lblcid.grid(column=2, row=2)
txtcid.grid(column=3, row=2, padx=5, pady=2, sticky='w')
lbluf.grid(column=2, row=3)
txtuf.grid(column=3, row=3, padx=5, pady=2, sticky='w')
lblobs.grid(column=4, row=1)
txtobs.grid(column=5, row=1, padx=5, pady=2, sticky='wn', rowspan=3)
btninser.grid(column=3, row=4, pady=10)

# -* Elementos label e texto (Entry) do LabelFrame frame3:
# -* Elemento label

lblnome1 = Label(frame3, text='Nome: ', width=5, anchor='w')

# -* Elemento texto (Entry) do LabelFrame frame3:

txtnome1 = Entry(frame3, width=30, font=('Ebrima, 12'), justify='left')

# -* Elemento botão do LabelFrame frame3:

btnpesq = Button(frame3, text='Pesquisar', width=10, bg='#b8b1e0',
                 font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised', command=lambda: pesquisa(treev, txtnome1))
btntudo = Button(frame3, text='Mostrar Tudo', width=10, bg='#b8b1e0',
                 font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised', command=lambda: tudo(treev))  # _ flat, groove, raised, ridge, solid, or sunken
btnedita = Button(frame3, text='Editar', width=10, bg='#b8b1e0',
                  font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised', command=editar)
btnexclui = Button(frame3, text='Excluir', width=10, bg='#b8b1e0',
                   font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised', command=excluir)
btnsair = Button(frame3, text='Sair', width=10, bg='#b8b1e0',
                 font=('', '10', 'bold'), cursor='hand1', border=3, relief='raised', command=sair)

# -* Posicionando os elementos dentro do frame3:

lblnome1.grid(column=0, row=0, padx=5)
txtnome1.grid(column=1, row=0, padx=5, sticky='w')
btnpesq.grid(column=2, row=0, padx=10, pady=10)
btntudo.grid(column=3, row=0, padx=5, pady=10)
btnedita.grid(column=4, row=0, padx=10, pady=10)
btnexclui.grid(column=5, row=0, padx=5, pady=10)
btnsair.grid(column=6, row=0, padx=10, pady=10)

# - Exibindo a tela:
tela.mainloop()
