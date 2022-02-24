# Software Apaixonados Por Carros

i = 1
while i != 0:
    print("Deseja utilizar o método de Vetores, Filas, Listas (1)")
    print("Deseja utilizar o método de Pilha (2)")
    print("Deseja utilizar o método de Árvore (3)")
    print("Deseja sair? (4)")
    o = int(input("Qual opção deseja escolher?\n"))

    if(o == 1):
        a = 0;
        vetor = list(range(20))
        while (a <= 19):
            vetor[a] = str(input("Marca de carro favorito: "))
            b = int(input("\nDeseja Continuar? 1 para sair"))
            if (b == 1):
                a = 20
            else:
                a += 1
        for vetor in vetor:
            print("\nSua marca de carro favoritas são: ", vetor)

    elif(o == 2):
        pilha = []
        c = 1
        while c != 0:
            print("Adicionar um carro na pilha de favorita (1)")
            print("Remover um carro da pilha de favorita (2)")
            b = int(input("Ver pilha(3)\n"))
            if(b == 1):
                numero = str(input("Digite sua marca de carro favorita para empilhar: "))
                pilha.append(numero)
                print("\nCarro inserido\n")
                c = int(input("\nContinuar? 0 para sair\n"))
            elif(b == 2):
                pilha.pop()
                print("\nCarro removido\n")
                c = int(input("\nContinuar? 0 para sair\n"))
            elif(b == 3):
                print("\nPilha: ", pilha)
                c = int(input("\nContinuar? 0 para sair\n"))
            else:
                print("\nNão temos essa opção :(\n")
                c = int(input("\nContinuar? 0 para sair\n"))

    elif(o == 3):
        from anytree import Node, RenderTree

        titu = Node("Marcas De Carro")
        d = 1
        while(d != 0):
            marcaCarro = str(input("Marca de Carro Favorita: "))
            marca = Node(marcaCarro, parent=titu)
            e = 1
            while(e != 0):
                carroEscolhida = str(input("Carro dessa marca favorita: "))
                carro = Node(carroEscolhida, parent=marca)
                e = int(input("Deseja colocar mais um carro nos favoritos? 0 para sair"))
            d = int(input("Deseja colocar mais uma marca nos favoritos? 0 para sair"))
        print(titu)
        Node('/macl')
        for pre, fill, node in RenderTree(titu):
            print("%s%s" % (pre, node.name))
    elif(o == 4):
        print("LOGOUT")
        i = 0
    else:
        print("\n\nOpção não existe :(")
        i = int(input("\nDeseja continuar? 0 para sair\n"))