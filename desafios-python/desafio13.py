print('------ DESAFIO 13 ------')

valor = float(input('Digite o seu salário: '))

aumento = (30 / 100) + 1
salario = aumento * valor

print('Seu novo salário será R${:.2f} com 15% de aumento'.format(salario))