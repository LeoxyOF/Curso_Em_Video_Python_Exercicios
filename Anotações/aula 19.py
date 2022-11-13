dict = {
    'Nome': 'Pedro',
    'Idade': 25
}
print(dict['Idade'])
print(dict['Nome'])

# adicionar elemento ao dicionário

dict['Sexo'] = 'M'

print(dict["Sexo"])

# apagar elemento

del dict["Sexo"]

# mostrar valores da lista (os armazenados nas variáveis)
print(dict.values())

# mostrar keys, variáveis responsáveis pelos valores

print(dict.keys())

# mostrar tudo

print(dict.items())

# exemplo usando o for

filmes = {
    'Titulo': "Star Wars",
    'Ano': 1977,
    'Diretor': 'George Lucas'
}

print(filmes.items())

for k, v in filmes.items():
    print(f'O {k} é {v}')

# outro exemplo usando a lista com o dicionário

Star = {
    'Titulo': "Star Wars",
    'Ano': 1977,
    'Diretor': 'George Lucas'
}

Avengers = {
    'Titulo': "Avengers",
    'Ano': 2012,
    'Diretor': 'Joss Whedon'
}

Matrix = {
    'Titulo': "Matrix",
    'Ano': 1999,
    'Diretor': 'Wachowski'
}
locadora = [Star, Avengers, Matrix]
print(locadora[0]['Ano'])
print(locadora[2]['Titulo'])

# como fazer cópia de dicionárip para lista
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for pos, val in e.items():
        print(f'O campo {pos} tem valor {val}')

# outra opção

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()