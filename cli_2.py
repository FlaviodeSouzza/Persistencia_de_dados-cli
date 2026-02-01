"""
Aplicação CLI para registrar lucro diário
e persistir os dados em arquivo CSV.
"""

import os
from datetime import date

# ========================
# Configurações do arquivo
# ========================
NOME_ARQUIVO = 'historico_lucro_certo.csv'
CABECALHO = 'data,entradas,saidas,lucro\n'

# ========================
# Persistência
# ========================
def garantir_arquivo_csv():
    """
    Verifica se o arquivo CSV existe.
    Caso não exista, cria o arquivo com cabeçalho.
    """
    if not os.path.exists(NOME_ARQUIVO):
        with open(NOME_ARQUIVO, 'w', encoding= 'utf-8') as arquivo:
            arquivo.write(CABECALHO)


def salvar_registros(entradas, saidas, resultado):
    """
    Salva um registro diário no arquivo CSV.
    """
    data_hoje = date.today().isoformat()

    linha = f'{data_hoje},{entradas},{saidas},{resultado}\n'

    with open(NOME_ARQUIVO, 'a', encoding= 'utf-8') as arquivo:
        arquivo.write(linha)


# ========================
# Entrada e validação
# ========================
def solicitar_valor(mensagem):
    """
    Solicita um valor numérico não negativo ao usuário.
    """
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0 :
                print('Digite um valor maior ou igual a zero.\n')
                continue
            return valor
        except ValueError:
            print('Valor inválido!')


# ========================
# Execução do programa
# ========================
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
