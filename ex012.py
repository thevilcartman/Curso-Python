# Exercício 12
''' Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''
v = float(input('Qual o valor do produto? R$'))
d = int(input('Qual a porcetagem de desconto? '))
vf = v * (d / 100)
df = v - vf
print('O valor com o desconto é de {:.2f}!'.format(df))
# novo = v - (v * d / 100)
