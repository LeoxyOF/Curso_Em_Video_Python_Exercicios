km = int(input('Qual é a distância da sua viagem? '))
print(f'Você esta prestes a começar uma viagem de {km} Kilõmetros de distância')
pre = km*0.50 if km <= 200 else km*0.45
print(f'O valor da viagem será {pre:.2f} R$')