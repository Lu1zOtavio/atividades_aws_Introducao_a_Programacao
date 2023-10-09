def elementos_abaixo_diagonal_secundaria(matriz):
    n = len(matriz)  # Tamanho da matriz (assumindo matriz quadrada)
    elementos = []

    for i in range(n):
        for j in range(n):
            if j > n - i -2:  # Verifica se está abaixo da diagonal secundária
                elementos.append(matriz[i][j])

    return elementos

# Exemplo de matriz
matriz_exemplo = [
    [00, 0,1, 0,2, 0,3],
    [10, 11, 12, 13],
    [20, 21, 22, 23],
    [30, 31, 32, 33]
]

elementos_abaixo_diagonal = elementos_abaixo_diagonal_secundaria(matriz_exemplo)
print(elementos_abaixo_diagonal)  # Saída: [8, 12, 16]
