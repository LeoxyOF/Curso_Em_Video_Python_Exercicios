dici = dict()
dici['nome'] = str(input('Nome: ')).strip()
dici['media'] = float(input(f'Média de {dici["nome"]}: '))
if dici['media'] >= 7:
    dici['Sts'] = 'Aprovado!'
else:
    dici['Sts'] = 'Reprovado!'
print(f'Nome é igual a {dici["nome"]}\nMédia é igual á {dici["media"]}\n'
      f'Situação é igual á \033[1;33m{dici["Sts"]}')
