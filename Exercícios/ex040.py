nota1 = float(input('\033[1;34mPrimeira nota: '))
nota2 = float(input('\033[1;34mSegunda nota: '))
media = (nota1 + nota2) / 2
print(f'\033[1;35mUm aluno que tirou notas de {nota1} e {nota2} nas provas, tem uma média de {media}')
if media < 5.0:
    print('\033[1;31mESTÁ REPROVADO!')
elif 7.0 > media >= 5.0:
    print('\033[1;33mESTÁ DE RECUPERAÇÃO!')
elif media >= 7.0:
    print('\033[1;32mESTÁ APROVADO!')
