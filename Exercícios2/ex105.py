from time import sleep


def notas(*num, sit=False):
    """
    -> função para avaliar notas
    :param num: recebe várias notas(quantidade infinita)
    :param sit: (opcional) mostra se a situação está ruim, boa ou razoável
    :return: o dicionário com todas informações
    """
    maior = menor = soma = 0
    dic = {'Total': len(num)}
    for key, valor in enumerate(num):
        soma += valor
        if key == 0:
            maior = valor
        if valor > maior:
            maior = valor
        if key == 0:
            menor = valor
        if valor < menor:
            menor = valor
    dic['Maior'] = maior
    dic['Menor'] = menor
    dic['M'] = soma / len(num)
    dic['Média'] = f'{dic["M"]:.2f}'
    if sit:
        if dic['M'] >= 7:
            dic['Situação'] = 'Boa'
        elif 7 > dic['M'] >= 5:
            dic['Situação'] = 'Razoável'
        elif dic['M'] < 5:
            dic['Situação'] = 'Ruim'
    dic.pop('M')
    return dic


resp = notas(5.5, 2.5, 1.5, sit=True)
for k, v in resp.items():
    print(f'{k} = {v}')
    sleep(0.6)
help(notas)
