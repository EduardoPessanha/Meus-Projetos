# -*- coding: utf-8 -*-
"""
    Módulo que contém as funções (rotinas) da minhagenda
"""

import os
import sqlite3
from sqlite3 import Error
from tkinter import messagebox
from tkinter import *


# -* Definindo o caminho e o nome do banco de dados:
dirdb = os.path.dirname(__file__)
nomedb = dirdb + '/Agenda0.db'

#  -* Conectatando o banco de dados:


def sair():
    """ 
    Encerra o aplicativo
    """
    os.system('clear')
    exit()
    return


def conectadb(bdados: str):
    """
        Estabelece a conexão com um banco de dados

        :param bdados: contém o caminho e o nome do banco de dados
    """
    con = None
    try:
        con = sqlite3.connect(nomedb)
    except Error as err:
        messagebox.showerror('ATENÇÃO ERRO', err)
    return con


def limpatv(par):
    """
        Função para limpar a tela da TreeView antes de mostrar os dados
    """
    tv = par
    tv.delete(*tv.get_children())
    """
    * OU:
    for i in tv.get_children():
        tv.delete(i)
    """


def tudo(inf):
    """
        Abre um banco de dados, seleciona todos os registros
        e exibe os registros tela da TreeView
    """
    vcon = conectadb(nomedb)  # - Abrindo o banco de dados
    # - Limpando a tela da TreeView antes de mostrar os dados:
    tv = inf
    limpatv(inf)
    try:
        c = vcon.cursor()    # criar um cursor para receber a conexão
        # execução da consulta (query) pelo cursor
        c.execute('select * from tb_contatos')
        res = c.fetchall()    # criar um resultado com o retorno da consulta do cursor
        vcon.close()    # fechar a conexão
        # >Etapa 3: Inserir os dados do banco de dados no Treeview
        for i in res:
            item = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
            tv.insert('', 'end', values=item)
        vcon.close()
    except Error as err:
        messagebox.showerror('ATENÇÃO ERRO', err)


"""
def consulta(conect, sql):
    res = None
    po = conect.cursor()
    try:
        po.execute(sql)
        res = po.fetchall()
    except Error as err:
        print(f"ATENÇÃO, ocorreu um ERRO: f{err}")
    return res
"""


def pesquisa(inf, txt):
    """
        Executa uma pesquisa no banco de dados por um nome, e mostra na TreeView
    """
    tv = inf
    txtnome1 = txt

    # > Conectando o banco de dados:
    vcon = conectadb(nomedb)
    po = vcon.cursor()
    vnome = txtnome1.get()
    try:
        # Conulta por nome
        if vnome == '':
            messagebox.showerror(
                'ATENÇÃO ERRO', 'Informe um nome para pesquisar')
        else:
            vsql = 'SELECT * FROM tb_contatos WHERE t_nome LIKE "%'+vnome+'%"'
            po.execute(vsql)
            vreg = po.fetchall()
            # - Limpar os dados da TreeView:
            limpatv(inf)
            for i in vreg:
                reg = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                tv.insert('', 'end', values=reg)
    except Error as err:
        messagebox.showerror('ATENÇÃO ERRO', err)
    finally:
        # > Limpando a caixa de texto e fechando o banco de dados:
        txtnome1.delete(0, END)
        vcon.close
    return


'''
def inserir(conexao: str, sql: str):
    """
    Função para inserir um novo registro em uma tabela

    :param conexao: informa qual o banco de dados conectado
    :param sql: informa os dados do registro a ser inserido
    """
'''


def inserir(val: list):
    """
        Função para inserir um novo registro na tabela do banco de dados
    """

    txtnome = val[0]
    txtfone = val[1]
    txtmail = val[2]
    txtend = val[3]
    txtcid = val[4]
    txtuf = val[5]
    txtobs = val[6]

    # 1- Estabelecer a conexão com o banco de dados
    vcon = conectadb(nomedb)  # -* Abre o banco de dados
    po = vcon.cursor()        # -* Definindo o cursor
    # 2- Verificar se foram digitados os dados no formulário
    try:
        if txtnome.get() == '' or txtfone.get() == '' or txtmail.get() == '':
            # ** O formulário está em branco
            messagebox.showerror(
                'ATENÇÃO ERRO', 'Não foram informados os valores!')
        else:
            # 3- Ler os dados inseridos do formulário
            reg = "INSERT INTO tb_contatos (t_nome, t_fone, t_email, t_endereco, t_cidade, t_uf, t_obs)VALUES('"+txtnome.get()+"', '"+txtfone.get(
            )+"', '"+txtmail.get()+"', '"+txtend.get()+"', '"+txtcid.get()+"', '"+txtuf.get()+"', '"+txtobs.get(1.0, END)+"' )"
            # 4- Inserir os dados do formulário na tabela do banco de dados e fazer o commit (atualizar o banco de dados)
            po.execute(reg)
            vcon.commit()
            messagebox.showinfo('AVISO', 'Registro inserido com sucesso!')
    except Error as err:
        messagebox.showerror('ATENÇÃO ERRO', err)
    finally:
        # > 5- Limpando os dados do formulário e fechando o banco de dados
        txtnome.delete(0, END)
        txtfone.delete(0, END)
        txtmail.delete(0, END)
        txtend.delete(0, END)
        txtcid.delete(0, END)
        txtuf.delete(0, END)
        txtobs.delete(1.0, END)
        txtnome.focus()

        vcon.close()
    return


"""
* Sintaxe do comando INSERT: INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...)
Para usar o INSERT devemos escrever INSERT INTO e o nome da tabela. Depois colocar em parênteses as colunas que terão um valor inseridos, escrever VALUES e escrever em outro parênteses os valores que serão inseridos nas colunas.

> vsql = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, t_EMAILCONTATO) VALUES ('"+nome+ "', '"+fone+"', '"+email+"')"
"""


def editar():
    pass
    return


def excluir():
    # ** Passo 1: Identificar qual registro deverá ser excluído!

    # ** Passo 2: Confirmar a exclusão:
    res = messagebox.askquestion('CONFIRMAR', 'Deseja continuar?')
    if res == 'yes':
        # ** Exclusão confirmada
        print(res + ' => Confirmado')
        # ** Passo 3: Excluir o registro
        # vid = input('Digite a ID do registro a ser excluído: ')
        # vsql = 'DELETE FROM tb_contatos WHERE n_idcontato =' + vid
        # quest(vcon, vsql)
    return
