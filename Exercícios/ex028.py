import random

a = random.randint(0, 5)
print('\033[1;31;40m----Jogo da Adivinhação----\033[m')
print("\033[1;31;40mAdivinhe o Número que o computador escolheu de 0 á 5!\033[m")
resp = int(input('\033[1;36;40mDigite um Número:\033[m'))
print('\033[1;32;40mVocê Acertou!\033[m' if resp == a else '\033[1;31;40mVocê Errou!\033[m')
if resp != a:
    print(f'\033[1;36;40mO Número Escolhido foi "{a}"\033[m')
