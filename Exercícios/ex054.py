from datetime import date
hoje = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 7+1):
    nasc = int(input(f'\033[1;35m[Pessoa Nª{c}] \033[1;36mEm que ano você nasceu? '))
    idade = hoje - nasc
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print(f'\033[1;32m{totmaior} Pessoas são maiores de idade')
print(f'\033[1;31m{totmenor} Pessoas são menores de idade')
