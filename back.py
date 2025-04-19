import os
import time
from collections import deque


tabuleiro = [
    ['I', ' ', ' ', 'X', ' ', ' ', ' '],
    ['X', 'X', ' ', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', ' ', ' ', 'X', ' '],
    [' ', 'X', 'X', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', 'F']
]

linhas = len(tabuleiro)
colunas = len(tabuleiro[0])

def encontrar_inicio():
    for i in range(linhas):   #percorrer todo o tabuleiro pra encontrar a letra "I" inicio) pra iniciar
        for j in range(colunas):
            if tabuleiro[i][j] == 'I':
                return i, j
    return None

def posicao_valida(linha, coluna, visitado):   #evita que o algoritmo tente ir pra fora do mapa ou fique preso em looping
    return (0 <= linha < linhas and            #pedi pra IA deixar o código mais limpo e ela fez uma comparação encadeada
            0 <= coluna < colunas and  #poderia ser escrita assim: (0 <= linha) and (linha < linhas)
            tabuleiro[linha][coluna] != 'X' and
            not visitado[linha][coluna])  #se não diferente de x e não foi visitado, é true, vai seguir o caminho

def encontrar_caminho_mais_curto(inicio):
    fila = deque()
    fila.append((inicio, [inicio]))
    visitado = [[False for _ in range(colunas)] for _ in range(linhas)]
    visitado[inicio[0]][inicio[1]] = True

    while fila:
        (linha, coluna), caminho = fila.popleft()
        if tabuleiro[linha][coluna] == 'F':
            return caminho
        for d_linha, d_coluna in [(-1,0), (1,0), (0,-1), (0,1)]:
            nova_linha = linha + d_linha
            nova_coluna = coluna + d_coluna
            if posicao_valida(nova_linha, nova_coluna, visitado):
                visitado[nova_linha][nova_coluna] = True
                fila.append(((nova_linha, nova_coluna), caminho + [(nova_linha, nova_coluna)]))
    return None

def mostrar_tabuleiro_com_caminho(caminho, passo):
    os.system('cls' if os.name == 'nt' else 'clear')
    copia = [linha[:] for linha in tabuleiro]
    for i in range(min(passo, len(caminho))):
        l, c = caminho[i]
        if copia[l][c] == ' ':
            copia[l][c] = '*'

    separador = '+' + '---+' * colunas
    for linha in copia:
        print(separador)
        linha_formatada = ''
        for celula in linha:
            linha_formatada += f'| {celula} '
        linha_formatada += '|'
        print(linha_formatada)
    print(separador)

def main():
    inicio = encontrar_inicio()
    if not inicio:
        print("Ponto 'I' não encontrado.")
        return
    caminho = encontrar_caminho_mais_curto(inicio)
    if caminho:
        print("Mostrando o caminho passo a passo...")
        passo = 0
        while passo <= len(caminho):
            mostrar_tabuleiro_com_caminho(caminho, passo)
            time.sleep(0.5)
            passo += 1
    else:
        print("Caminho impossível.")

if __name__ == "__main__":
    main()
