print('------ DESAFIO 100 ------')

def voto(ano):
    f = 2024
    resultado = f - ano

    if resultado < 16:
        return f'Com {resultado} anos: NÃO VOTA.'
    
    elif 16 <= resultado < 18 or resultado > 65:
        return f'Com {resultado} anos: VOTO OPCIONAL.'
    
    else:
        return f'Com {resultado} anos: VOTO OBRIGATÓRIO.'

idade = int(input('Em que ano você nasceu? '))
print(voto(idade))
    