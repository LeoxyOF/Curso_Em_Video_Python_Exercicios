# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# galera = [['João', 19], ['Ana', 33], ['Joaquim', 45], ['Maria', 13]]
# print(galera)
# for p in galera:
    # print(f"{p[0]:<10}{p[1]:>}")

galera = list()
dado = list()
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()
print(galera)
totmaior = totmenor = 0
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade!')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmenor += 1
print(f'{totmaior} pessoas são maiores de idade')
print(f'e {totmenor} pessoas são menores de idade')