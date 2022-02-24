pilha = []
i = 1

while (i != 0):
    numero = int(input("Digite um número para empilhar: "))
    pilha.append(numero)
    i=int(input("Continuar? 0 para sair"))
    print("Inserindo um elemento: ", pilha)

pilha.pop()
print("Removendo um elemento: ", pilha)