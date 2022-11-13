from random import randint
cont = 0
pc = randint(1, 10)
resp = 0
print('\033[33mAdivinhe o número que o computador escolheu de 0 á 10!')
while resp != pc:
    resp = int(input('\033[36mNúmero >> '))
    if resp > 10:
        print('\033[31mO Limite é \033[33m10\033[31m!')
    elif resp < pc:
        print('\033[31mResposta incorreta! Tente novamente \033[39m(Mais \033[32m+\033[39m)')
    elif resp > pc:
        print('\033[31mResposta incorreta! Tente novamente \033[39m(Menos \033[31m-\033[39m)')
    cont += 1
if cont == 1:
    print(f'\033[1;32mVocê Acertou!\033[33m Foram Necessários Apenas {cont} Palpite!')
if cont > 1:
    print(f'\033[1;32mVocê Acertou!\033[33m Foram Necessários {cont} Palpites!')