print('======Boletim Escolar======')
A1 =float(input('Digite uma Nota: '))
A2 =float(input('Digite outra Nota: '))
r = A1 + A2
e = r / 2
print(f'A média das provas foram: "{e:.1f}"')
from math import ceil, floor
'Sistema de Arredondamento  que fiz'
print(f'Arredondando Este valor para cima fica: {ceil(e)}')
print(f'Arredondando Este valor para baixo fica: {floor(e)}')