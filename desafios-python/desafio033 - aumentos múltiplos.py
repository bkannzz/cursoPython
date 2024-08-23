print('------ DESAFIO 33 ------')

salario = float(input('Digite o valor de um salário: '))

valor1 = (10 / 100) + 1
valor2 = (15 / 100) + 1

if salario > 1250:
    salario1 = valor1 * salario
    print('seu salário recebeu um aumento de 10%, é ficou igual a {:.2f}R$'.format(salario1))
    
else: 
    salario2 = valor2 * salario
    print('seu salário recebeu um aumento de 10%, é ficou igual a {:.2f}R$'.format(salario2))
    