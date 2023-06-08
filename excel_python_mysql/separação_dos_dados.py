import pandas as pd
import mysql.connector
x = pd.read_excel(r'C:\Users\Win-10\Documents\PRODUTOS.xlsx')
conexao = mysql.connector.connect (host = '**********',
                                   user = '********',
                                   password = '**************',
                                   database = '**************')
cursor = conexao.cursor()
for i in range(0, 35):
    lista = []
    codigo = str(x['SKU'][i])
    for p in range(len(x['DESCRITOR'][i])):
        if x['DESCRITOR'][i][p] == '-':
            lista.append(p)
    print(lista)
    marca = x['DESCRITOR'][i]
    marca = marca[:marca.find('-')]
    tamanho = x['DESCRITOR'][i]
    tamanho = tamanho[tamanho.find('-') + 1: lista[1]]
    sabor = x['DESCRITOR'][i]
    sabor = sabor[lista[1] + 1:]
    embalagem = x['EMBALAGEM'][i]
    preco = str(x['PREÇO'][i])
    preco = preco.replace(',', '.')
    preco = float(preco)
    comando = f'INSERT INTO SELECIONAR (CODIGO, MARCA, TAMANHO, SABOR, EMBALAGEM, PREÇO) VALUES ("{codigo}", "{marca}", "{tamanho}", "{sabor}", "{embalagem}", {preco})'
    cursor.execute(comando)
    conexao.commit()
cursor.close()
conexao.close()