nome = str(input('Qual é seu nome completo? ')).strip().upper()
a = 'SILVA' in nome
if a:
    print('Seu nome tem Silva')
elif not a:
    print('Seu nome não tem Silva')
# 2
nom = str(input('Qual é seu nome completo? ')).strip().upper()
if 'SILVA' in nom:
    print('Seu nome tem Silva')
else:
    print('Seu nome não tem Silva')
