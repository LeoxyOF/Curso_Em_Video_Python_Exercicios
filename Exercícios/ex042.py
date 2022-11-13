print('\033[1;34m-='*20)
print('\033[1;31;m        Analisador de Triângulos\033[m')
print('\033[1;34m-='*20)
r1 = float(input('\033[1;33mPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: \033[m'))
if r1 == r2 == r3:
    print('\033[1;34mOs Segmentos Acima Podem Formar Um Triângulo \033[1;33mEQUILÁTERO\033[1;34m!')
elif r1 != r2 != r3 and r3 != r1:
    print('\033[1;35mOs Segmentos Acima Podem Formar Um Triângulo \033[1;31mESCALENO\033[1;35m!')
else:
    print('\033[1;37mOs Segmentos Acima Podem Formar Um Triângulo \033[1;31mISÓSCELES\033[1;37m!')
