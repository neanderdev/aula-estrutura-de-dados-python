## PROVA 1
value = 0
array = list (range (2))
i = 0

while (i <= 1):
    array[i] = int(input("Digite uma valor: "))
    i += 1

print("1 para soma: ")
print("2 para substração: ")
print("3 para multiplicação: ")
print("4 para divisão: ")

operacao = int(input("Qual operação você deseja: "))
resultado = 0;

if operacao == 1:
    resultado = array[0] + array[1]
    print(resultado)
elif operacao == 2:
    resultado = array[0] - array[1]
    print(resultado)
elif operacao == 3:
    resultado = array[0] * array[1]
    print(resultado)
elif operacao == 4:
    resultado = array[0] / array[1]
    print(resultado)
else:
    print('Não foi possível realizar essa operação :(')

## PROVA 2
qtdeAlunos = int(input("Quantos alunos existem na sala: "))
i = 0

while (i  < qtdeAlunos):
    resultadoSomaNota = 0
    resultadoMedia = 0
    arrayNotas = list(range(5))
    j = 0

    while(j  < 5):
        arrayNotas[j] = int(input("Digite a nota (de 0 a 10): "))
        j += 1

    for z in arrayNotas:
        resultadoSomaNota += z
    resultadoMedia = resultadoSomaNota / 5
    print("Aluno", i, "a média é", resultadoMedia)

    i += 1





