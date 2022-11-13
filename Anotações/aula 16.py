# import time as tm
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# a = 'u' in lanche[1]
# for c in lanche:
    # print(c, end=' - ')
    # tm.sleep(1)
# if a:
    # print('Sim')
# tuplas são imutáveis
# print(lanche[0])

# for cont in range(0, len(lanche)):
    # print(f'vou comer {lanche[cont]} na posição {cont}')
# afp = 0
# for comida in lanche:
    # afp += 1
    # print(f'Vou comer {comida} na posição {afp}')
a = (4, 8, 2, 9, 2)
b = (7, 10, 14)
c = a + b
print(f'Os números são:{c}')
# print(f'Quantidade de números: {len(c)}')
print(f'{c.index(2, 2)}')