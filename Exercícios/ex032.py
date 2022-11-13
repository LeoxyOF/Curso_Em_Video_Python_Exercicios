import calendar
from datetime import date
ano = int(input('Qual ano que analisar? Coloque 0 para analisar seu ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O Ano {ano} é BISSEXTO')
else:
    print(f'O Ano {ano} Não é BISSEXTO')
'Jeito Bem Mais Simples'
an = int(input('Digite o ano: '))
ano6 = calendar.isleap(an)
if ano6 is True:
    print(f'O ano de {an} é bissexto')
else:
    print(f'O ano de {an} não é bissexto')
