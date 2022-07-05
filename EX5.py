# 5. Faça um programa que solicite 10 números ao usuário, depois disso, exiba
# todos os números pares e só então exiba os números ímpares.
# Utilize a função filter() para isso.

Matriz = []

for i in range(10):
    Nx = int(input("Digite um número: "))
    Matriz.append(Nx)

Pares = filter(lambda valor: valor % 2 == 0, Matriz)
Impares = filter(lambda valor: valor % 2 == 1, Matriz)

print("-" * 10, "Números Pares", "-" * 10)
for Par in Pares:
    print(Par)
print("-" * 10, "Números Pares", "-" * 10)

print()

print("-" * 10, "Números Impares", "-" * 10)
for Impar in Impares:
    print(Impar)
print("-" * 10, "Números Impares", "-" * 10)
