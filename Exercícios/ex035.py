print('\033[1;34m-='*20)
print('\033[1;31;47mAnalisador de Triângulos\033[m')
print('\033[1;34m-='*20)
r1 = float(input('\033[mPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos Acima PODEM FORMAR Triângulos')
else:
    print('Os Segmentos Acima NAO PODEM FORMAR Triângulos')
