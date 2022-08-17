import csv
Tabela = {}
arq = csv.reader(open('tabelaPeriodica.csv'), delimiter=';')

def carregartabela(): 
    for i, dadoLinha in enumerate(arq):
        if i == 0: 
            continue
        Dados = {}
        Dados['simbolo'] = dadoLinha[0] 
        Dados['nome'] = dadoLinha[1] 
        Dados['numeroAtomico'] = dadoLinha[2]
        Dados['linha'] = dadoLinha[3]
        Dados['coluna'] = dadoLinha[4] 
        Dados['estado'] = dadoLinha[5] 
        Tabela[Dados['simbolo']] = Dados
    print(Tabela)

def procurar(): 
    inputDados = input("Digite o simbolo do elemento: ").title()
    for i, dadoLinha in enumerate(arq):
        if i == 0: 
            continue
        Dados = {}
        Dados['simbolo'] = dadoLinha[0] 
        Dados['nome'] = dadoLinha[1] 
        Dados['numeroAtomico'] = dadoLinha[2]
        Dados['linha'] = dadoLinha[3]
        Dados['coluna'] = dadoLinha[4] 
        Dados['estado'] = dadoLinha[5] 
        Tabela[Dados['simbolo']] = Dados

    elemento = Tabela[inputDados]
    print("==========================================================")
    print('Simbolo selecionado foi:',elemento['simbolo'])
    print('O nome do elemento selecionado é:',elemento['nome'])
    print('O número atomico do elemento é:',elemento['numeroAtomico'])
    print('O elemento pertence à linha',elemento['linha'], "na tabela Periodica.")
    print('O elemento pertence à coluna',elemento['coluna'], "na tabela Periodica.")
    print("O elemento",elemento['nome'], "é:",elemento['estado'])
    print("==========================================================")


def verificaElemento():
    for i, dadoLinha in enumerate(arq):
        if i == 0: 
            continue
        Dados = {}
        Dados['simbolo'] = dadoLinha[0] 
        Dados['nome'] = dadoLinha[1] 
        Dados['numeroAtomico'] = dadoLinha[2]
        Dados['linha'] = dadoLinha[3]
        Dados['coluna'] = dadoLinha[4] 
        Dados['estado'] = dadoLinha[5] 
        Tabela[Dados['simbolo']] = Dados
        elemento = input("Digite o simbolo do elemento: ").title()
        dado = input(''' 
                  -> Digite o dado desejado <-
            [1] - Para procurar o nome do elemento.
            [2] - Para procurar o número atomico do elemento.
            [3] - Para procurar a linha do elemento.
            [4] - Para procurar a coluna do elemento.
            [5] - Para procurar o estado do elemento.
            \n''')
        for i in Tabela:
            if dado == '1':
                print(Tabela[elemento]['nome'])
            elif dado == '2':
                print(Tabela[elemento]['numeroAtomico'])
            elif dado == '3':
                print(Tabela[elemento]['linha'])
            elif dado == '4':
                print(Tabela[elemento]['coluna'])
            elif dado == '5':
                print(Tabela[elemento]['estado'])
            else:
                print('Dado não encontrado')
        break

    
    