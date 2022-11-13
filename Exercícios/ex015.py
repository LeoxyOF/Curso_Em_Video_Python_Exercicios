dias = int(input('Quantos Dias Alugados? '))
km = float(input('Quantos Km Rodados? '))
calcdias = dias*60
calckm = km*0.15
print(f'O Total a Pagar é R$"{calcdias + calckm:.2f}"')
