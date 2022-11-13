geral = []
nome = []
notas = []
media = []
while True:
    print('\033[1;34m-=' * 3, f'\033[1;39mAluno \033[1;34m{len(geral) + 1}', '-=' * 3)
    nome.append(str(input(f'\033[1;35mNome: ')))
    notas.append(float(input(f'\033[1;32m1º \033[1;34mNota: ')))
    notas.append(float(input(f'\033[1;32m2º \033[1;34mNota: ')))
    media.append((notas[0] + notas[1]) / 2)
    notas.sort()
    nome.append(notas[:])
    notas.clear()
    geral.append(nome[:])
    nome.clear()
    c = str(input('\033[1;39mQuer Continuar? [\033[1;32mS\033[1;39m/\033[1;31mN\033[1;39m]: ')).strip().upper()[0]
    if c == 'N':
        break
print(f'{"Pos.":<5} {"Nome":^10} { "Média":>10}')
print('-' * 30)
for a, b in enumerate(geral):
    print(f'{a+1:<5} {b[0]:^10} {media[a]:>10.1f}')
print('-' * 30)
while True:
    done = int(input('\033[1;39mNotas de qual aluno? \033[1;31m("999" interrompe)\033[1;39m: ')) - 1
    if done == 998:
        print('\033[1;31mPrograma Finalizado!')
        break
    else:
        if len(geral) - 1 >= done > 0:
            print('\033[1;39m-=' * 3, f'\033[1;33mAs notas de \033[1;35m{geral[done][0]}'
                                      f'\033[1;33m são', f'\033[1;35m{geral[done][1]}', '\033[1;39m-=' * 3)
        else:
            print('\033[1;31mResposta inválida!')