# Exercício 15
''' Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

dias = int(input('Número de dias do aluguel: '))
km = int(input('Quantos kilometros percorridos: '))
valor = (dias * 60) + (km * 0.15)
print('Você ficou {} dias com o carro e andou {} kilometros.'.format(dias, km))
print('Sua conta ficou no valor de R${:.2f}.'.format(valor))
