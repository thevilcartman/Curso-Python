# Exercício 6
''' Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''
n = int(input('Digite um número inteiro: '))
do = n * 2
tri = n * 3
raiz = n ** (1/2)
raiz2 = pow(n, (1/2)) # outra maneira de fazer raiz quadrada
print('O dobro de {} é {}, o triplo é {} e a raiz é {:.2f}'.format(n, do, tri, raiz))
print('O dobro de {} é {}, o triplo é {} e a raiz é {}'.format(n, (n * 2), (n * 3), (n ** (1/2))))
print(raiz2)


