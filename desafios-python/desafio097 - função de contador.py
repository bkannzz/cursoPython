print('------ DESAFIO 97 ------')

from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i + 1
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

# PROGRAMA PRINCIPAL
contador(0, 10, 1)
print('-' * 30)
contador(10, 0, 2)
