# Desafio 3
# Crie um programa que leia dois números e mostre a soma entre eles
# Aula 6

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma é {}!'.format(s))

# Desafio extra: a mensagem deve ser "A soma entre n1 e n2 é x"
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))
