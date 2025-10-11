import random

def checar_espacos (tab):
    espacos_vazios = []
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == "":
                espacos_vazios.append([i][j])
    return espacos_vazios

def frutas(tab):
    
    if len(espacos) >= 5:
        espacos = checar_espacos(tabuleiro)
        fruta_boa = random.sample(espacos, 5)
        for i, j in fruta_boa:
            tab[i][j] = "O"
            
    if len(espacos) >= 5:
        espacos = checar_espacos(tabuleiro)
        fruta_ruim = random.sample(espacos, 5)
        for i, j in fruta_ruim:
            tab[i][j] = "X"  
  