print('------ DESAFIO 71 ------')

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dessesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))

    if 0 <= num <= 20:
        break
    print('Tente novamente.',end='')
print(f'Você digitou o número {cont[num]}')