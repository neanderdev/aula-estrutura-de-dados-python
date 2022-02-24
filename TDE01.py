a = float(input("Digite o 1º Número: "))
b = float(input("Digite o 2º Número: "))
c = float(input("Digite o 3º Número: "))
print("a: {}, b: {}, c: {}".format(a,b,c))

delta = (b * b) - 4 * a * c
print("Delta = {}² - 4 . {} . {} = {}".format(b,a,c, (b * b) - 4 * a * c))

deltaRaiz = pow(delta,0.5)

if delta == 0 :
  print("Delta é igual a 0.")
else :
  x1 = ((-b + deltaRaiz) / (2 * a))
  x2 = ((-b - deltaRaiz) / (2 * a))
  print("X1 = {:.2f}".format(x1))
  print("X2 = {:.2f}".format(x2))