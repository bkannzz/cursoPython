print('------ DESAFIO 104 ------')

def notas(*n, sit=False):
    """
    
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não ser adicionar a situação.
    :return: dicionário com várias informações sobre a situção da turma.
    
    """

    aluno = dict()
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['média'] = sum(n) / len(n)
    
    if sit:
        if aluno['média'] >= 7:
            aluno['situação'] = 'BOA'

        elif aluno['média'] >= 5:
            aluno['situação'] = 'RAZOÁVEL'

        else:
            aluno['situação'] = 'RUIM'

    return aluno
        

resp = notas(0, 0, 0, sit=True)
print(resp)