num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
       'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
       'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
perg = 0
while True:
    perg = int(input('\033[36mEscreva um número de 0 á 20: \033[36m'))
    if perg <= 20 >= 0:
        print(f'\033[33mO número é \033[1;39m{num[perg]}')
        resp = str(input('\033[35mQuer continuar? [\033[32mS\033[35m/\033[31mN\033[35m] ')).strip().upper()[0]
        if resp == 'N':
            break
    else:
        print('\033[31mResposta Inválida!\033[m')
