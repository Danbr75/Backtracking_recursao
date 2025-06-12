# Jogo do Labirinto - Caminho mais curto com Busca em Largura (BFS)

Este projeto é um pequeno programa em Python que encontra o **caminho mais curto** entre um ponto inicial (`I`) e um ponto final (`F`) dentro de um tabuleiro com obstáculos (`X`), utilizando o algoritmo **BFS (Busca em Largura)**. O código ainda mostra uma animação simples do percurso no terminal, passo a passo.

---

## Como funciona?

- O tabuleiro é representado por uma matriz 2D, onde:
  - `'I'` é o ponto inicial (de onde começa a busca)
  - `'F'` é o ponto final (onde queremos chegar)
  - `'X'` são obstáculos que não podem ser atravessados
  - `' '` (espaço em branco) são as posições livres onde podemos andar
- O programa usa o algoritmo BFS para garantir que o caminho encontrado seja o mais curto possível.
- Conforme o caminho vai sendo mostrado, o trajeto é marcado com `*` no terminal para você visualizar o passo a passo.

---

## Estrutura do Código

- **tabuleiro**: matriz que representa o mapa.
- **encontrar_inicio()**: procura a posição inicial no tabuleiro.
- **posicao_valida()**: verifica se uma posição é válida para se mover (dentro do tabuleiro, não é obstáculo nem visitada).
- **encontrar_caminho_mais_curto()**: implementa o BFS para achar o menor caminho do `I` até o `F`.
- **mostrar_tabuleiro_com_caminho()**: imprime o tabuleiro no terminal, marcando o caminho encontrado até o passo atual.
- **main()**: função principal que executa o programa e exibe a animação do caminho.
