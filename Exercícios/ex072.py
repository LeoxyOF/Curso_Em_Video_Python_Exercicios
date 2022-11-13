num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
       'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
       'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
perg = 0
while True:
    perg = int(input('\033[36mEscreva um número de 0 á 20: \033[36m'))
    if perg <= 20 >= 0:
        break
    else:
        print('\033[31mResposta Inválida!\033[m')
print(f'\033[33m{num[perg]}')
