# Exercício 10
''' Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.'''
r = float(input('Quantos reais para comprar doláres: '))
d = 5.35
c = r / d
print('Você pode comprar {:.2f} doláres \ncom {:.0f} reais.'.format(c, r))
