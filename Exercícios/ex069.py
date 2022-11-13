resp = ''
sexo = ''
cont18 = 0
conthomem = 0
contmulher = 0
while resp != 'N':
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Resposta inválida!')
        while sexo != 'M' and sexo != 'F':
            sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'M':
        conthomem += 1
    if idade > 18:
        cont18 += 1
    if sexo == 'F' and idade < 20:
        contmulher += 1
    resp = str(input('Quer continuar? '))[0].strip().upper()
if cont18 != 0:
    print(f'{cont18} pessoas tem mais de 18 anos')
if cont18 == 1:
    print('Apenas 1 pessoa tem mais que 18 anos')
if conthomem != 0:
    print(f'{conthomem} homens foram cadastrados')
if conthomem == 1:
    print('Apenas 1 homem foi cadastrado')
if contmulher != 0:
    print(f'{contmulher} mulheres tem menos de 20 anos')
if contmulher == 2:
    print('Apenas uma mulher foi cadastrada')