#Decisões simples(apenas if), compostas(if e else) e encadeadas(if, elife e else)


nota1 = float(input("Digite a nota de Portugês! "))
nota2 = float(input("Digite a nota de Matemática! "))
nota3 = float(input("Digite a nota de História! " ))
nota4 = float(input("Digite a nota de Geografia! "))
nota5 = float(input("Digite a nota de Biologia! "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) /5

if media >= 7:
    print("Aprovado! Sua média é: ", media)
elif media >=6:
    print("Recuperação! Sua média é: ", media)
else:
    print("Reprovado! Sua média é: ", media)