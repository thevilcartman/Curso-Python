# Exercício 13
''' Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''
s = float(input('Qual o salário atual? R$'))
a = int(input('Qual a porcetagem de aumento? '))
sf = s * (a / 100)
af = s + sf
print('O salário com o aumento de {}% é de {:.2f}!'.format(a, af))
# novo = s + (s * a /100)