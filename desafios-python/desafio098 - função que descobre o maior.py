print('------ DESAFIO 98 ------')

from time import sleep

def maior(* num):
    cont = 0
    maior = 0

    print('\nAnalisando os valores passados...')
    
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)

        if cont == 0:
                maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(2, 9, 7, 3, 5, 4)
maior(7, 4, 8)
maior(1, 6, 7, 8, 9)