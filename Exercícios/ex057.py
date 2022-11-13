dado = str(input('\033[36mQual é seu sexo? [\033[33mM\033[36m/\033[31mF\033[36m] ')).upper()[0].strip()
sexo = ''
if dado != 'M' and dado != 'F':
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('\033[31mDados Incorretos!, \033[33mpor favor, \033[36mInforme seu sexo [\033[33mM\033[36m/\033[31mF\033[36m] ')).upper()[0].strip()
else:
    if dado in 'MF':
        print(f'\033[1;32mSexo {dado} Registrado!')
if sexo == 'M' or sexo == 'F':
    print(f'\033[1;33mSexo {sexo} Registrado!')