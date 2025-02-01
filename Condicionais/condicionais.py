

nota1 = float(input("Diite a nota de Portugês! "))
nota2 = float(input("Diite a nota de Matemática! "))
nota3 = float(input("Diite a nota de História! " ))
nota4 = float(input("Diite a nota de Geografia! "))
nota5 = float(input("Diite a nota de Biologia! "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) /5

if media >= 7:
    print("Aprovado! Sua média é: ", media)
else:
    print("Reprovado! Sua média é: ", media)