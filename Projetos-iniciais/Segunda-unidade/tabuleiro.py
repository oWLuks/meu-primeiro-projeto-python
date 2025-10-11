import os
import time
import gerar_frutas

def criar_tabuleiro ():

    tabuleiro = []
    for i in range(15):
        linha = []
        for j in range(15):
            linha.append("")
        tabuleiro.append(linha)
    return tabuleiro

def exibir_tabuleiro(tab):
    for linha in tab:
        print(" ".join(elemento if elemento != "" else "." for elemento in linha))

def limpar_terminal(limpar=0):
    if limpar > 0:
        time.sleep(limpar)
    os.system("cls" if os.name == 'nt' else "clear")

