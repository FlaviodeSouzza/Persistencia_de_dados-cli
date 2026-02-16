"""
Aplicação CLI para registrar lucro diário
e persistir os dados em arquivo CSV.
Fase 2 -> Persistencia e Leitura de dados.
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
        with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
            arquivo.write(CABECALHO)


def salvar_registros(entradas, saidas, resultado):
    """
    Salva um registro diário no arquivo CSV.
    """
    data_hoje = date.today().isoformat()
    linha = f'{data_hoje},{entradas},{saidas},{resultado}\n'

    with open(NOME_ARQUIVO, 'a', encoding='utf-8') as arquivo:
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
# Leitura de dados
# ========================
def leitura_csv():
    """
    Lê o arquivo CSV e retorna uma lista com os registros.
    """
    registros = []

    with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        next(arquivo)
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                valores = linha.split(",")
                registros.append(valores)

    return registros


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
    print(f'\nSeu resultado final no dia de hoje foi de \033[34mR$ {lucro:.2f}\033[0m!\n')
else:
    print(f'\nSeu resultado final no dia de hoje foi de \033[31mR$ {lucro:.2f}\033[0m!\n')

salvar_registros(entradas_totais,saidas_totais,lucro)

# Exibição do histórico completo
historico = leitura_csv()

print('\nHistórico completo:\n')
for registro in historico:
    print(f'Data: {registro[0]} | Entradas: R$ {registro[1]} | '
          f'Saídas: R$ {registro[2]} | Lucro: R$ {registro[3]}')

# Projeto finalizado na Fase 2:
# - Persistência em CSV
# - Leitura estruturada
# - Exibição formatada dos dados
