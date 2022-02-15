# Exercício 11
''' Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².'''
b = float(input('Digite o valor da base: '))
a = float(input('Digite o valor da altura: '))
mq = a * b
l = mq / 2
print('Você precisará de {} litros de tinta.'.format(l))
