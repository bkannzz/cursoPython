print('------ DESAFIO 61 ------')

print('Gerador de PA')
print('=-=' * 5)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
contador = 1
total = 0 
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='') 

        termo += razao
        contador += 1

    print('PAUSA')

    mais = int(input('\nQuantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos mostrados.'.format(total))