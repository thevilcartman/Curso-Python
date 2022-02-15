# Exercício 4
''' Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.'''
i = input('Digite algo: ')
print('O tipo primitivo da informação é ', type(i))
# a condição .isxxx é usada para testar uma variável e responder com condições booleana
print('A informação é alfanúmerica? {}'.format(i.isalnum()))
print('A informação é apenas número? {}'.format(i.isnumeric()))
print('A informação é apenas alfabética?', i.isalpha())
print('A informação é imprimível?', i.isprintable())
print('Está em letras maiuscúlas?', i.isupper())
print('Está em letras minuscúlas?', i.islower())
print('Está capitalizada?', i.istitle()) # a primeira letra maiscúla e o resto minuscúla
