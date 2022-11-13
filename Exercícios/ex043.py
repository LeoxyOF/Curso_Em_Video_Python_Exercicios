from time import sleep
print('\033[1;33m----Calcular IMC----\033[m')
peso = float(input('\033[1;34mQual é seu peso? '))
altura = float(input('Qual é sua altura? \033[m'))
print('\033[1;33mAnalisando dados...')
sleep(1)
imc = peso / altura ** 2
print(f'\033[1;35mSeu IMC é {imc:.1f}\033[m')
sleep(0.5)
if imc < 18.5:
    print('\033[1;31mSua Categoria é \033[1;36mAbaixo do Peso\033[m')
elif 25 > imc > 18.5:
    print('\033[1;31mSua Categoria é \033[1;36mPeso Ideal\033[m')
elif 30 > imc > 25:
    print('\033[1;31mSua Categoria é \033[1;36mSobrepeso\033[m')
elif 40 > imc > 30:
    print('\033[1;31mSua Categoria é \033[1;36mObesidade\033[m')
elif imc > 40:
    print('\033[1;31mSua Categoria é \033[1;36mObesidade Mórbida\033[m')
