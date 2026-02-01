"""
O projeto implementa uma aplicação de linha de comando capaz de registrar
dados fornecidos pelo usuário e persistí-los em um arquivo CSV.
"""

import os
from datetime import date

NOME_ARQUIVO = 'historico_lucro_certo.csv'
CABECALHO = 'data,entradas,saidas,lucro\n'

def garantir_arquivo_csv():
    '''Verifica a existencia do arquivo no diretório atual.'''
    if not os.path.exists(NOME_ARQUIVO):
        with open(NOME_ARQUIVO, 'w', encoding= 'utf-8') as arquivo:
            arquivo.write(CABECALHO)


def salvar_registros(entradas, saidas, resultado):
    '''Salva as entradas do usuario no doc csv.'''
    data_hoje = date.today().isoformat()

    linha = f'{data_hoje},{entradas},{saidas},{resultado}\n'

    with open(NOME_ARQUIVO, 'a', encoding= 'utf-8') as arquivo:
        arquivo.write(linha)


def solicitar_valor(mensagem):
    """Validação das variaveis de calculo"""
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0 :
                print('Digite um valor maior ou igual a zero.\n')
                continue
            return valor
        except ValueError:
            print('Valor inválido!')

#Execução principal:

garantir_arquivo_csv()

print('\nOlá! Vamos calcular seu resultado diário.')
print('----' * 15)

entradas_totais = solicitar_valor('\nQual o valor total de ENTRADAS no dia de hoje? R$ ')
saidas_totais = solicitar_valor('\nQual o valor total de SAÍDAS no dia de hoje? R$ ')
lucro = entradas_totais - saidas_totais

if lucro >= 0:
    print(f'\nSeu resultado final no dia de hoje foi de \033[34mR$ {lucro:.2f}\033[0m\n!')
else:
    print(f'\nSeu resultado final no dia de hoje foi de \033[31mR$ {lucro:.2f}\033[0m!\n')

salvar_registros(entradas_totais,saidas_totais,lucro)
