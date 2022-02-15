# Exercício 2
''' Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.'''
nome = input('Qual o seu nome? ')
print('Que nome feio,', nome, '!')

nome = input('Qual o seu nome? ') # podemos usar a variável dentro da string de texto sem usar ,
print('Que nome feio, {}!'.format(nome)) # usando {} e vinculando a variável com o .format(variável)
print('{}... Que nome feio!'.format(nome))

