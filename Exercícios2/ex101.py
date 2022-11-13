def voto(nasc):
    from datetime import date
    idade = (nasc - date.today().year) * -1
    print(f'Com {idade} anos:', end=' ')
    if idade < 16:
        return '\033[1;33mVOTO NEGADO!'
    if 65 > idade >= 18:
        return '\033[1;31mVOTO OBRIGATÓRIO!'
    if idade >= 65 or 18 > idade >= 16:
        return '\033[1;32mVOTO OPCIONAL!'


print('_-' * 20)
print(voto(int(input('Em que ano você nasceu? '))))
print('_-' * 20)
