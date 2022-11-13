from datetime import date
from time import sleep
hoje = date.today().year
dici = {'Ano Atual': hoje, 'Nome': str(input('Nome: ')).strip(),
        'Idade': int(input('Ano de nascimento: ')),
        'CTPS': int(input("Carteira de Trabalho (0 é nulo): "))}
if dici['CTPS'] != 0:
    dici['Ano de contratação'] = int(input('Ano de contratação: '))
    a = float(input('Salário: R$'))
    dici['Salário'] = f'R${a}'
    dici['Aposentadoria'] = dici['Idade'] + ((dici['Ano de contratação'] + 35) - date.today().year)
else:
    dici['CTPS'] = 'Não Possui'
dici['Idade'] = (dici['Idade'] * -1) + hoje
print("-=" * 20)
print(dici)
for key, valor in dici.items():
    print(f'{key} = {valor}')
    sleep(0.5)
