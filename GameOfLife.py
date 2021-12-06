# Game of life - Logica UFRJ
# Alunos: Miguel Lima Tavares - 119161571
#         Luiz Bernardo Levenhagen - 111212116
import time
import os
import random
import sys

def limpaTela():

    # limpa a tela no windows
    if sys.platform.startswith('win'):
        os.system("cls")

    #limpa tela no linux
    elif sys.platform.startswith('linux'):
        os.system("clear")



def geraGrid(linhas, colunas):

    #cria lista aleatoria com 0s e 1s para representar as celulas

    grid = []

    for linha in range(linhas):
        gridLinhas = []
        for coluna in range(colunas):
            # gera numero aleatoria para definir a celula
            if random.randint(0,7) == 0:
                gridLinhas += [1]
            else:
                gridLinhas += [0]
        grid += [gridLinhas]
    return grid



def geraProxGrid(linhas, colunas, grid, proxGrid):

    for linha in range(linhas):
        for coluna in range(colunas):
            vizinhosAlive = getVizinhosAlive(linha, coluna, linhas, colunas, grid)

            if vizinhosAlive < 2 or vizinhosAlive > 3:
                proxGrid[linha][coluna] = 0
            elif (vizinhosAlive == 3) and (grid[linha][coluna] == 0):
                proxGrid[linha][coluna] = 1
            else:
                proxGrid[linha][coluna] = grid[linha][coluna]
            



def getVizinhosAlive(linha, coluna, linhas, colunas, grid):

    lifeSoma = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i ==0 and j == 0):
                lifeSoma += grid[((linha + i) % linhas)][((coluna + j) % colunas)]
    
    return lifeSoma




def verificaGrid(linhas, colunas, grid, proxGrid):

    # verifica se a geracao atual e a mesma que a proxima

    for linha in range(linhas):
        for coluna in range(colunas):

            if not grid[linha][coluna] == proxGrid[linha][coluna]:
                return True

    return False



def printGrid(linhas, colunas, grid, geracao):

    limpaTela()

    out = ""
    out += "Geracao {0} - Pra sair pressione <Ctrl-C>\n\r".format(geracao)
    for linha in range(linhas):
        for coluna in range(colunas):
            if grid[linha][coluna] == 0:
                out += ". "
            else:
                out += "@ "
        out += "\n\r"
    print(out, end=" ")


def recebeInteiro(mensagem, limInf, limSup):

    #valida inteiro digitado pelo usuario

    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("Valor digitado não é válido.")
            continue
        if (valor < limInf) or (valor > limSup):
            print("Valor fora dos parâmetros")
        else:
            break

    return valor






def main():
    
    #loop do jogo principal
    while True:

        limpaTela()

        #numero de geracoes
        geracoes = 1000

        linhas = recebeInteiro("Digite o número de linhas (10-60): ", 10, 60)
        limpaTela()
        colunas = recebeInteiro("Digite o número de colunas (10-118): ", 10, 118)

        # verifica modo aleatorio ou input do usuário
        tipo = recebeInteiro("Digite <1> para marcação e <2> para aleatório: ", 0, 2)

        if tipo == 1: # input do usuario
            geracaoAtual = [[0 for coluna in range(colunas)] for linha in range(linhas)]
            proxGeracao = geraGrid(linhas, colunas)
            comando = "continuar"
            while comando.lower() != "sair":
                linha = recebeInteiro("Digite a linha a ser alterada: ", 1, linhas)
                coluna = recebeInteiro("Digite a coluna a ser alterada: ", 1, colunas)
                geracaoAtual[linha - 1][coluna - 1] = 1
                comando = input("digite <SAIR> para terminar a alteração e <ENTER> para continuar: ")
        else:# modo aleatorio
            geracaoAtual = geraGrid(linhas, colunas)
            proxGeracao = geraGrid(linhas, colunas)

        gen = 1

        for gen in range(1, geracoes + 1):
            if not verificaGrid(linhas, colunas, geracaoAtual, proxGeracao):
                break
        
            printGrid(linhas, colunas, geracaoAtual, gen)
            geraProxGrid(linhas, colunas, geracaoAtual, proxGeracao)
            time.sleep(1/5.0)
            geracaoAtual, proxGeracao = proxGeracao, geracaoAtual

        printGrid(linhas, colunas, geracaoAtual, gen)
        input("<Enter> para continua a jogar, <CTRL + C> para sair")



main()
