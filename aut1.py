import pandas as pd
import openpyxl
from datetime import date

def DataAtual():
    dataAtual = date.today()
    dataAtual = dataAtual.strftime('%d-%m-%Y')
    return dataAtual
    #print(f'\n{type(dataAtual)}\n{dataAtual}\n')


def separador():
    return '\n----------------------------------------------------------------------------------------------\n'

def Alterador():

    tabela = pd.read_excel("Produtos.xlsx")

    print(tabela)

    print(separador())

    tabela.loc[tabela['Tipo']=='Serviço', 'Multiplicador Imposto'] = 1.5

    print(tabela)

    print(separador())

    tabela['Preço Base Reais'] = tabela['Multiplicador Imposto'] * tabela['Preço Base Original']

    print(tabela)

    dataAtual = DataAtual()

    nameSpace = "Produtos-" + dataAtual + ".xlsx"


    tabela.to_excel(nameSpace, index=False)
Alterador()

print(f'\nArquivo Criado com sucesso\n')

