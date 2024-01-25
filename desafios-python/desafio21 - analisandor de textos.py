print('------ DESAFIO 21 ------')

nome = str(input(' Digite seu nome completo: '))    

maiuscula = nome.upper()
minuscula = nome.lower()
quantidade = len(nome) - nome.count(' ')
primeiro = nome.split()
mostrar = primeiro[0]
primeiroo = len(mostrar)

print(' Nome em maiusculo: {}\n Nome em minusculo: {}\n Quantas letras tem seu nome: {}\n Quantas letras tem seu primeiro nome:{}'.format(maiuscula, minuscula, quantidade, primeiroo))