vetor = list(range(2))
i = 0;

while (i <= 1):
    vetor[i] = float(input("Digite um valor: "))
    i += 1

print("1 - Soma: ")
print("2 - Subtração: ")
print("3 - Multiplicação: ")
print("4 - Divisão: ")
operacao = int(input("Qual operação você deseja: "))
resultado = 0;

if operacao == 1:
    resultado = vetor[0] + vetor[1]
    print(resultado)
elif operacao == 2:
    resultado = vetor[0] - vetor[1]
    print(resultado)
elif operacao == 3:
    resultado = vetor[0] * vetor[1]
    print(resultado)
elif operacao == 4:
    resultado = vetor[0] / vetor[1]
    print(resultado)
else:
    print('Não foi possível realizar essa operação')