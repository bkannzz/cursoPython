print('------ DESAFIO 38 ------')

print('Alistamento Militar')

nascimento = int(input('Digite sua data de nascimento: '))

idade = 2024 - nascimento

if idade < 17:
    menor = 17 - idade
    print('Você tem {} anos ainda vai se alistar!'.format(idade))
    print('Faltam mais {} anos pra conseguir se alistar!'.format(menor))

elif idade == 17 and idade == 18:
    print('Você tem {} anos já pode se alistar!'.format(idade))
    
elif idade > 18:
    maior = idade - 18
    print('Você tem {} anos já passou do tempo de se alistar!'.format(idade))
    print('Já faz {} anos que já passou o prazo.'.format(maior))