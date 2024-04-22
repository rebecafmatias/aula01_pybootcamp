""" Criar um programa que o usuário digite o seu nome e retorne o número de caracteres """

nome = input('Digite seu nome: ')
len_nome = len(nome)

print(f'Seu nome tem {len_nome} caracteres, {nome}.')

""" Criar um programa onde o usuário digite dois valores e apareça a soma """

num1 = float(input('Primeiro valor: '))
num2 = float(input('Segundo valor: '))

resultado = num1 + num2

print(f'Resultado: {resultado}')