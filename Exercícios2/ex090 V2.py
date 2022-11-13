dici = dict()
dici['Nome'] = str(input('Nome: ')).strip()
dici['Média'] = float(input(f'Média de {dici["Nome"]}: '))
dici['Status'] = 'Aprovado' if dici['Média'] >= 7 else 'Reprovado' if 7 > dici['Média'] <= 5 else 'Recuperação'
for key, valor in dici.items():
    print(f'{key} = {valor}')
