# 6. Faça um programa que solicite um número ao usuário, depois disso, exiba
# o dobro do número inserido, obtendo o valor da multiplicação através de uma
# função usando lambda.

N1 = float(input("Insira um número: "))

def Multiplicador(N2):
    return lambda N1: N1 * N2

Dobro = Multiplicador(2)

print(Dobro(N1))
