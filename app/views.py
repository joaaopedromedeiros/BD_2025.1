from django.shortcuts import render

import pyodbc


def obter_conexao():
    # define os parametros de conexao
    driver   = '{ODBC Driver 17 for SQL Server}'
    servidor = '.\SQLEXPRESS'
    banco    = 'Aulas_DB'
    usuario  = 'sa'
    senha    = 'Senha@123' # poder ser também: "senha", "senha@123", "Senha@123"

    # realiza conexao com o BD
    string_conexao = f'Driver={driver};Server={servidor};Database={banco};UID={usuario};PWD={senha}'
    conexao = pyodbc.connect(string_conexao)
    
    # retorna a conexao  
    return conexao


def home(request):
    # define a página HTML (template) que deverá será carregada
    template = 'home.html'
    return render(request, template)

def exercicio_1(request):
    # define a página HTML (template) que deverá será carregada
    template = 'exercicio_1.html'
    try:
        # obtem a conexao com o BD
        conexao = obter_conexao()

        # define um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # define o comando SQL que será executado
        sql = '''
            SELECT  dep.nome as 'departamento',fun.nome, fun.telefones

            FROM Funcionario fun
            INNER JOIN Departamento dep ON dep.id = fun.departamento_id

            ORDER BY dep.nome, fun.nome
        '''
        
        # usa o cursor para executar o SQL
        cursor.execute(sql)
        # obtem todos os registros retornados
        registros = cursor.fetchall()

        # define a pagina a ser carregada, adicionando os registros das tabelas 
        return render(request, template, context={'registros': registros})
    
    # se ocorreu algunm erro, insere a mensagem para ser exibida no contexto da página 
    except Exception as err:
        return render(request, template, context={'ERRO': err})

def exercicio_2(request):
    # define a página HTML (template) que deverá será carregada
    template = 'exercicio_2.html'
    try:
        # obtem a conexao com o BD
        conexao = obter_conexao()

        # define um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # define o comando SQL que será executado
        sql = '''
            SELECT  turma.nome, Aluno.nome, Aluno.idade

            FROM Aluno
            INNER JOIN Turma on Turma.id = aluno.turma_id

            ORDER BY Turma.nome, Aluno.nome, Aluno.idade
        '''
        
        # usa o cursor para executar o SQL
        cursor.execute(sql)
        # obtem todos os registros retornados
        registros = cursor.fetchall()

        # define a pagina a ser carregada, adicionando os registros das tabelas 
        return render(request, template, context={'registros': registros})
    
    # se ocorreu algunm erro, insere a mensagem para ser exibida no contexto da página 
    except Exception as err:
        return render(request, template, context={'ERRO': err})

def exercicio_3(request):
    
    # define a página HTML (template) que deverá será carregada
    template = 'exercicio_3.html'
    try:
        # obtem a conexao com o BD
        conexao = obter_conexao()

        # define um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # define o comando SQL que será executado
        sql = '''
            SELECT  bairro.nome, cidade.nome, estado.nome

            FROM Bairro
            INNER JOIN Cidade on cidade.id = bairro.cidade_id
            INNER JOIN Estado on estado.sigla = cidade.estado_id

            ORDER BY Estado.nome, Cidade.nome, Bairro.nome
        '''

        #Juntar bairro com cidade
        # e depois juntar cidade com estado 
        
        # usa o cursor para executar o SQL
        cursor.execute(sql)
        # obtem todos os registros retornados
        registros = cursor.fetchall()

        # define a pagina a ser carregada, adicionando os registros das tabelas 
        return render(request, template, context={'registros': registros})
    
    # se ocorreu algunm erro, insere a mensagem para ser exibida no contexto da página 
    except Exception as err:
        return render(request, template, context={'ERRO': err})

def exercicio_4(request):
    
    # define a página HTML (template) que deverá será carregada
    template = 'exercicio_4.html'
    try:
        # obtem a conexao com o BD
        conexao = obter_conexao()

        # define um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # define o comando SQL que será executado
        sql = '''
           SELECT 
                fab.descricao AS Fabricante,
                mod.descricao AS Modelo,
                c.ano_fabricacao AS AnoFabricacao,
                c.cor AS Cor,
                c.placa AS Placa,
                c.preco AS Preco,
                cat.descricao AS Categoria

            FROM Carro c
            JOIN Modelo mod ON mod.id = c.modelo_id
            JOIN Fabricante fab ON fab.id = mod.fabricante_id
            JOIN Categoria cat ON cat.id = c.categoria_id
            ORDER BY fab.descricao, mod.descricao, c.ano_fabricacao;
        '''

        # Aqui em Join eu crio o apelido do Modelo --> mod para usar de forma simplificada em qualquer outra parte da consulta sql

        # usa o cursor para executar o SQL
        cursor.execute(sql)
        # obtem todos os registros retornados
        registros = cursor.fetchall()

        # define a pagina a ser carregada, adicionando os registros das tabelas 
        return render(request, template, context={'registros': registros})
    
    # se ocorreu algunm erro, insere a mensagem para ser exibida no contexto da página 
    except Exception as err:
        return render(request, template, context={'ERRO': err})
