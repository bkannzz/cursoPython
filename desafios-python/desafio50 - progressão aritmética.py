print('------ DESAFIO 50 ------')

termo = int(input('primeiro termo: '))
numero = int(input('razão: '))

decimo = termo + (10 - 1) * numero

for c in range(termo, decimo + numero, numero):
        print(c, end=' -> ')
print('ACABOU')