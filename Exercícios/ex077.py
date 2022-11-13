tupla = ('JavaScript', 'Php', 'Python', 'Aprender', 'Curso', 'Video', 'Pawn', 'Github')
vogais = 'AaEeIiUuOo'
for p in tupla:
    print(f'\nEm {p.upper()} temos:', end=' ')
    for letras in p:
        if letras in vogais:
            print(f'{letras}', end=' ')