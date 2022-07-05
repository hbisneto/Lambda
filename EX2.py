# 2. Faça um programa que solicite o nome do usuário e a idade do usuário,
# depois disso exiba a mensagem: "{nome} possui {idade} anos."
# Esta mensagem deve ser escrita em uma função lambda.

Nome = str(input("Digite o seu nome: "))
Idade = int(input("Digite a sua idade: "))

Mensagem = lambda: print(f'{Nome} possui {Idade} anos.')
Mensagem()
