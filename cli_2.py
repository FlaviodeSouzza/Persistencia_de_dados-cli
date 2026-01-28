"""
O projeto implementa uma aplicação de linha de comando capaz de registrar
dados fornecidos pelo usuário e persistí-los em um arquivo CSV, garantindo
organização, validação de entrada e histórico imutável.
"""

import os
from datetime import date

NOME_ARQUIVO = 'historico_lucro_ceerto.csv'
CABECALHO = 'data,entradas,saidas,lucro'

def garantir_arquivo_csv():
    #Verifica a existencia do arquivo no diretório atual.
    if not os.path.exists(NOME_ARQUIVO):
        with open(NOME_ARQUIVO, 'w', encoding= 'utf-8') as arquivo:
            arquivo.write(CABECALHO)


def salvar_registros(entradas,saidas,lucro):
    #Salva as entradas do usuario no doc csv.
    data_hoje = date.today().isoformat()

    linha = 'f{data_hoje},{entradas},{saidas},{lucro}\n'

    with open(NOME_ARQUIVO, 'a', encoding= 'utf-8') as arquivo:
        arquivo.write(linha)

