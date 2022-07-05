# 3. Faça um programa que solicite 2 números ao usuário e exiba a
# multiplicação deles.
# A multiplicação deve ser calculada em uma função lambda.

N1 = float(input("Digite o primeiro número: "))
N2 = float(input("Digite o segundo número: "))

Calculo = lambda N1, N2: N1 * 2

print(Calculo(N1, N2))
