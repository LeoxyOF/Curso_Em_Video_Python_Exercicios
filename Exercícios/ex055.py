maior = 0
menor = 0
for a in range(1, 5+1):
    peso = float(input(f'\033[1;36m[Pessoa Nª{a}] \033[1;33mQual é seu peso? '))
    if a == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'\033[1;32mO maior peso lido foi de {maior}Kg')
print(f'\033[1;31mO menor peso lido foi de {menor}Kg')