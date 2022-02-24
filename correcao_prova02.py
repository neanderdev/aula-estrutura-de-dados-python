alunos = int(input("Quantos alunos existem na sala? "))
i = 0

while (i < alunos):
    SomaNota = 0;
    Media = 0;
    Notas = list(range(5))
    j = 0

    while(j < 5):
        Notas[j] = int(input("Digite a nota (de 0 a 10): "))
        j += 1

    for z in Notas:
        SomaNota += z;
        Media = SomaNota / 5

    print("Aluno",i+1," Média: ",Media);
    i += 1