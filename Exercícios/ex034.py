sala = float(input('Digite o Salário: R$'))
if sala <= 1250:
    calc = (sala / 100)*15
else:
    calc = (sala / 100)*10
print(f'Quem ganhava {sala:.2f} R$ passa a ganhar {calc + sala:.2f} R$ com um aumento de {calc:.2f} R$')
