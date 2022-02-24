# Crie uma aplicação que execute uma ação prática utilizando de Pilhas.
# App de pilha de filmes e series favoritas

pilhaFavorites = []
z = 1

while (z == 1):
    filmeSerieFavorito = str(input("Qual sua Série ou Filme favorita(o): "))
    pilhaFavorites.append(filmeSerieFavorito)

    print("Pilha de Filme/Série favorita: ", pilhaFavorites)

    z = int(input("\n Deseja digitar mais Filme/Série? \n Para continuar digite 1 e para sair digite 0: "))

x = 0
x = int(input("\n Deseja remover alguma Filme/Série da pilha de favorito? \n Para remover digite 0 e para não remover digite 1: "))

while (x == 0):
    pilhaFavorites.pop()
    print("Nova pilha de Filme/Série favorita: ", pilhaFavorites)

    x = int(input("\nDeseja remover mais alguma Filme/Série da pilha de favorito? \n Para remover digite 0 e para não remover digite 1: "))

print("\n Pilha de Filme/Série favorito: ", pilhaFavorites)
