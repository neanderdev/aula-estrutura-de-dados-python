print("Calculado de Matriz de Ordem 1, 2, 3")
print("--------------------------------------------")

print("Digite 1 - para Matriz de 1º Ordem")
print("Digite 2 - para Matriz de 2º Ordem")
print("Digite 3 - para Matriz de 3º Ordem")
print("--------------------------------------------")

opcao = int(input("Qual opção deseja: "))
print("--------------------------------------------")

if opcao == 1:
    print("A Matriz de 1º é formada assim: M = | a11 |")
    print("--------------------------------------------")

    a11 = float(input("Digite o valor do a11: "))
    print("M = | {:.2f} |".format(a11))
    print("--------------------------------------------")

    resultado = a11
    print("Resultado da Matriz de 1º Ordem é: {:.2f}".format(resultado))
elif opcao == 2:
    print("A Matriz de 2º é formada assim: M = | a11  a12 |")
    print("                                    | a21  a22 |")
    print("--------------------------------------------")

    a11 = float(input("Digite o valor do a11: "))
    a12 = float(input("Digite o valor do a12: "))
    print("--------------------------------------------")
    a21 = float(input("Digite o valor do a21: "))
    a22 = float(input("Digite o valor do a22: "))
    print("--------------------------------------------")
    print("M = | {:.2f}  {:.2f} |".format(a11, a12))
    print("    | {:.2f}  {:.2f} |".format(a21, a22))
    print("--------------------------------------------")

    resultado = (a11 * a22) - (a12 * a21)
    print("Resultado da Matriz de 2º Ordem é: {:.2f}".format(resultado))
elif opcao == 3:
    print("A Matriz de 2º é formada assim: M = | a11  a12  a13 |")
    print("                                    | a21  a22  a23 |")
    print("                                    | a31  a32  a33 |")
    print("--------------------------------------------")

    a11 = float(input("Digite o valor do a11: "))
    a12 = float(input("Digite o valor do a12: "))
    a13 = float(input("Digite o valor do a13: "))
    print("--------------------------------------------")
    a21 = float(input("Digite o valor do a21: "))
    a22 = float(input("Digite o valor do a22: "))
    a23 = float(input("Digite o valor do a23: "))
    print("--------------------------------------------")
    a31 = float(input("Digite o valor do a31: "))
    a32 = float(input("Digite o valor do a32: "))
    a33 = float(input("Digite o valor do a33: "))
    print("--------------------------------------------")
    print("M = | {:.2f}  {:.2f}  {:.2f} |".format(a11, a12, a13))
    print("    | {:.2f}  {:.2f}  {:.2f} |".format(a21, a22, a23))
    print("    | {:.2f}  {:.2f}  {:.2f} |".format(a31, a32, a33))
    print("--------------------------------------------")

    resultado = ((a11 * a22 * a33) + (a12 * a23 * a31) + (a13 * a21 * a32) - (a13 * a22 * a31) - (a11 * a23 * a32) - (a12 * a21 * a33))
    print("Resultado da Matriz de 3º Ordem é: {:.2f}".format(resultado))
else:
    print("Digite uma opção válida: ")
    print("--------------------------------------------")