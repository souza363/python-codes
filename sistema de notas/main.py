turma = []
notaN1 = []
notaN2 = []
valorMedia = []
situacao = []

def cadastro():
    nome = input("\nDigite o nome do aluno: ").capitalize().strip()

    while True:
        nota1 = float(input("\nInforme a primeira nota (0 a 10): ").strip())

        if nota1 >= 0 and nota1 <= 10:
            print("\nNota registrada.")
            break
        else:
            print("Informe um valor válido!")

    while True:

        nota2 = float(input("\nInforme a segunda nota (0 a 10): ").strip())

        if nota2 >= 0 and nota2 <= 10:
            print("\nNota registrada.\n")
            break
        else:
            print("\nInforme um valor válido!")

    media = calculoMedia(nota1, nota2)
    media2 = resultMedia(nota1, nota2)

    turma.append(nome)
    notaN1.append(nota1)
    notaN2.append(nota2)
    situacao.append(media)
    valorMedia.append(media2)

def calculoMedia(nota1, nota2):
    if (nota1 + nota2) / 2 >= 7:
        return "Aprovado!"
    elif (nota1 + nota2) / 2 <= 6 and (nota1 + nota2) / 2 >= 4:
        return "Recuperação!"
    else:
        return "Reprovado"

def resultMedia(nota1, nota2):
    return (nota1 + nota2) / 2

def listaAlunos():
    if len(turma) == 0:
        print("\nNão há alunos cadastrados!")
        return
    else:
        for i in turma:
            print(f"\nNome: {turma}")
            print(f"Nota 1: {notaN1}")
            print(f"Nota 2: {notaN2}")
            print(f"Situação: {situacao}")

def maiorMedia():
    numero_maior = max(valorMedia)
    posicao = valorMedia.index(numero_maior)
    print(posicao)

    print(f"\nNome: {turma[posicao]}")
    print(f"Nota 1: {notaN1[posicao]}")
    print(f"Nota 2: {notaN2[posicao]}")
    print(f"Situação: {situacao[posicao]}\n")

def mediaGeral():
    return sum(valorMedia) / len(valorMedia)

'''while True:
    opcao = input("Escolha: ").strip()

    if opcao == "1":
        cadastro()
    elif opcao == "2":
        maiorMedia()
    elif opcao == "3":
        print(f"A média geral da turma é: {mediaGeral()}")
    else:
        break'''
