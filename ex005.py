# Exercício 5
''' Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.'''
n = int(input('Digite um número inteiro: '))
su = n + 1
an = n - 1
print('O sucessor é {} e o antecessor é {}'.format(su, an))
print('O antecessor é {} e o sucessor é {}'.format(n - 1, n + 1))
# podemos fazer o print tanto usando variáveis como colocando a função aritmética no format

