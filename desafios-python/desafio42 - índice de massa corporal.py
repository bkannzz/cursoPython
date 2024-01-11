print('------ DESAFIO 42 ------')

print('Calculador de IMC')

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / altura
final = imc / altura

if final <= 18.5:
    print('VOCÊ ESTÁ COM {:.2f} ABAIXO DO PESO'.format(final))
elif final > 18.5 and final <= 25:
    print('VOCÊ ESTÁ COM {:.2f} PESO IDEAL'.format(final))
elif final > 25 and final <= 30:
    print('VOCÊ ESTÁ COM {:.2f} SOBREPESO'.format(final))
elif final > 30 and final <= 40:
    print('VOCÊ ESTÁ COM {:.2f} OBESIDADE'.format(final))
else:
    print('VOCÊ ESTÁ COM {:.2f} OBESIDADE MÓRBIDA'.format(final))