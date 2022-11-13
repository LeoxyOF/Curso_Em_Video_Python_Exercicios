somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for peoples in range(1, 7):
    print(f'\033[1;35mPessoa Número \033[1;36m{peoples}')
    Nom = str(input('\033[1;31mSeu nome: ')).strip()
    Ida = int(input('\033[1;34mSua idade: '))
    print('\033[1;36m(M)\033[1;33m para masculino \033[1;35m(F)\033[1;33m para feminino')
    se = (input('\033[1;33mSexo: ')).lower().strip()
    print('\033[1;39m=-='* 5)
    somaidade = somaidade + Ida
    if peoples == 1 and 'm' in se:
        maioridadehomem = Ida
        nomevelho = Nom
    if "m" in se and Ida > maioridadehomem:
        maioridadehomem = Ida
        nomevelho = Nom
    if 'f' in se and Ida >= 20:
        totmulher20 += 1
mediaidade = somaidade / 6
print(f'\033[1;38mA Média da Idade é \033[1;31m{mediaidade:.2f}')
if 'm' in se:
    print(f'\033[1;36mO Homem mais velho é \033[1;31m{nomevelho} \033[1;36mcom \033[1;31m{maioridadehomem} Anos')
else:
    print(f'\033[1;31mNão tem nenhum homem')
if 'f' in se and Ida > 20:
    print(f'\033[1;32mUm total de \033[1;31m{totmulher20}\033[1;32m Mulheres tem mais de 20 anos')
a = 'f' in se
if 'f' in se and Ida < 20:
    print(f'\033[1;31mNenhuma mulher tem mais de 20 anos')
elif a == False:
    print('\033[1;31mNão tem nenhuma mulher')