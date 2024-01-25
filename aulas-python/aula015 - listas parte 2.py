teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:]) # copia da lista

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:]) # copia da lista

print(galera)

print('-=' * 13)

pessoal = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

print(pessoal)
print(pessoal[2][1]) # posições na lista

for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos de idade.') 
    print('-=' * 15)

print('-=' * 13)

alguem = list()
dado = list()
totmai = totmen = 0

for c in range(0, 3): # ler os dados de cada pessoa e jogar pra lista 'alguem'
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))

    alguem.append(dado[:])
    dado.clear()

for p in alguem: # analisador de maior de idade
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1

    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')