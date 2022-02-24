# Exemplo 1:
maior = 0
posicoes = int(input("Quantas notas serão digitadas: "))
numeros = list (range (posicoes))
i=0
while (i < posicoes):
    numeros[i] = int(input("Digite uma nota: "))
    if numeros[i] > maior:
        maior = numeros[i]
    i += 1
print ("A Maior Nota é: ",maior)


# Exemplo 2:
maior = 0
numeros = list (range (10))
for i in range(0,10):
    numeros[i] = int(input("Digite uma nota: "))
    if numeros[i] > maior:
        maior = numeros[i]
print ("A Maior Nota é: ",maior)