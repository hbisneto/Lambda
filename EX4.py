# 4. Faça um programa que solicite 5 números ao usuário, depois disso,
# exiba apenas os número maiores do que 10.
# Utilize a função filter() para isso.

Matriz = []

for i in range(5):
    Nx = int(input("Digite um número: "))
    Matriz.append(Nx)

MaiorQueDez = filter(lambda valor: valor > 10, Matriz)

for Maiores in MaiorQueDez:
    print(Maiores)
