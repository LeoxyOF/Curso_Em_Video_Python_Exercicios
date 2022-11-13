from math import sin, cos, tan, radians
an = float(input('ÂNGULO: '))
seno = sin(radians(an))
print(f'O ângulo de {an}° tem o SENO de "{seno:.2f}" ')
cos = cos(radians(an))
print(f'O COSSENO de "{cos:.2f}" ')
tan = tan(radians(an))
print(f'E a TANGENTE de "{tan:.2f}" ')