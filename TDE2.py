import numpy as np

qtd = int(input('Informe o ordem da matriz: '))
matriz = np.empty([qtd, qtd], dtype=float)

for x in range(0, qtd):
    for y in range(0, qtd):
        matriz[x][y] = float(input(f"Digite um valor para [{x}, {y}]: "))
print("---------------------------------")

for x in range(0, qtd):
    for y in range(0, qtd):
        print(f"[{matriz[x][y]}]", end="")
    print("\n---------------------------------")

resultadoDeterminante = np.linalg.det(matriz)
print("A determinante é: {:.2f}".format(resultadoDeterminante))