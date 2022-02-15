# Exercício 14
''' Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''
temp = float(input('Por favor, digite sua temperatura: '))
fah = ((temp * 9) / 5) + 32
# fah = temp * 9 / 5 + 32 seguindo a ordem de precedência dos operadores e da esquerda para direita
# não é necessário usar os parenteses
print('A temperatura em fahrenheit é {}ºF.'.format(fah))