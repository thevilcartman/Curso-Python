# Exercício 8
''' Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''
m = float(input('Digite a metragem: '))
c = m * 100
mi = m * 1000
print('{} metros equivale a {:.0f} centimetros e {:.0f} milimetros.'.format(m, c, mi))
print('{} metros equivale a {} centimentros e {} milimetros.'.format(m, m * 100, m * 1000))

