num = int(input('\033[1;31mDigite um número inteiro: '))
print('''
\033[1;33m[1]\033[1;35m Converter para \033[1;36mBINÁRIO\033[m
\033[1;33m[2]\033[1;35m Converter para \033[1;36mOCTAL\033[m
\033[1;33m[3]\033[1;35m Converter para \033[1;36mHEXADECIMAL\033[m
''')
opcao = int(input('\033[1;33mSua escolha >> '))
print('')
if opcao == 1:
    print(f'\033[1;33m"{num}"\033[1;31m convertido para \033[1;36mBINÁRIO\033[1;31m é igual á \033[1;33m"{bin(num)[2:]}"')
elif opcao == 2:
    print(f'\033[1;33m"{num}"\033[1;31m convertido para \033[1;36mOCTAL\033[1;31m é igual á \033[1;33m"{oct(num)[2:]}"')
elif opcao == 2:
    print(f'\033[1;33m"{num}"\033[1;31m convertido para \033[1;36mHEXADECIMAL\033[1;31m é igual á \033[1;33m"{hex(num)[2:]}"')
else:
    print('\033[1;31mOpção Inválida')
