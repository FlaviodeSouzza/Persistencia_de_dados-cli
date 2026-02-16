# Persistência de Dados em CSV (CLI em Python)

Aplicação CLI desenvolvida em Python com foco em persistência local de dados, criada como evolução técnica do projeto Calculadora de Lucro e como base estrutural para o sistema *_LucroCerto_*.

## Descrição

O projeto implementa uma aplicação de linha de comando capaz de registrar dados fornecidos pelo usuário, persistí-los em um arquivo CSV e realizar a leitura estruturada do histórico salvo.

O sistema cria automaticamente o arquivo de dados, define um cabeçalho fixo (contrato de dados) e adiciona novos registros de forma incremental, sem sobrescrever informações anteriores.

## Funcionalidades

* Criação automática do arquivo CSV, caso não exista

* Definição de cabeçalho fixo para organização dos dados

* Inserção de dados via terminal

* Validação de entradas do usuário

* Registro incremental de dados (append)

* Geração automática da data do registro

* Leitura estruturada dos dados persistidos

* Exibição formatada do histórico completo no terminal

## Estrutura de Persistência

* Tipo: Arquivo local

* Formato: CSV (Comma-Separated Values)

* Nome do arquivo: historico_lucro_certo.csv (nome fixo no estágio atual)

## Cabeçalho do CSV

```data,entradas,saidas,lucro```


Cada linha do arquivo representa um registro único, seguindo rigorosamente a ordem definida no cabeçalho.

## Como executar

* Certifique-se de ter o Python 3 instalado.

* No terminal, execute:

``` * python cli_2.py```

## Objetivo do Projeto

Praticar e consolidar conceitos fundamentais de desenvolvimento em Python, com foco em:

* Manipulação de arquivos

* Persistência de dados sem uso de banco de dados

* Validação robusta de entrada do usuário

* Separação de responsabilidades no código

* Escrita de código limpo, legível e reutilizável

* Leitura e interpretação de dados persistidos


## Lições Aprendidas

* Criação e verificação automática de arquivos

* Uso do modo append para preservação de histórico

* Definição de contrato de dados através de cabeçalho CSV

* Validação de strings e dados numéricos

* Uso de funções com responsabilidade única

* Organização e evolução incremental de um projeto CLI

* Leitura de arquivos CSV ignorando cabeçalho

* Conversão de linhas em estruturas manipuláveis (listas)

* Exibição formatada de dados persistidos

### Observações Importantes

>O separador utilizado no CSV é a vírgula (,), conforme o padrão internacional

>Em configurações regionais do Excel (ex: Brasil), pode ser necessário importar o arquivo manualmente para visualização correta das colunas

>O projeto não utiliza frameworks ou bibliotecas externas

### Próximos Passos

* Implementar menu interativo para controle de fluxo

* Permitir consulta filtrada por data

* Evoluir estrutura para versão modular (Projeto 3)

### Status do Projeto

🟢 Concluído – Fase 2: Persistência e Leitura de Dados
📌 Próxima fase: implementação de menu e controle de fluxo (Projeto 3)
