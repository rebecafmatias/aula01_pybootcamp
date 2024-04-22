# """ Criar um programa que o usuário digite o seu nome e retorne o número de caracteres """

# nome = input('Digite seu nome: ')
# len_nome = len(nome)

# print(f'Seu nome tem {len_nome} caracteres, {nome}.')

# """ Criar um programa onde o usuário digite dois valores e apareça a soma """

# num1 = float(input('Primeiro valor: '))
# num2 = float(input('Segundo valor: '))

# resultado = num1 + num2

# print(f'Resultado: {resultado}')

""" Cálculo de Bônus com Entrada do Usuário """

nome = input('Digite seu nome: ')

salario = None
pct_bonus = None

while salario == None:
    try:
        salario = float(input('Digite seu salário: '))
    except ValueError:
        print(' \nVocê digitou um número inválido. Digite apenas números para salário! \nExemplo: Salário: 2500.50 \n')
        salario = None
while pct_bonus == None:
    try:
        pct_bonus = float(input('Qual o percentual do seu bônus? '))
    except ValueError:
        print(' \nVocê digitou um número inválido. Digite apenas números para percentual de bônus! \nExemplo: Percentual: 2.50 \n')
        pct_bonus = None

valor_base = 1000

bonus = valor_base + (salario*pct_bonus)

print(f'Olá {nome}, o seu valor bônus foi de {bonus}.')
