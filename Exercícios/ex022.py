nome = str(input('Qual é Seu Nome Completo? ')).strip()
print('Analisando seu Nome.....')
print(f'Seu Nome em Minúsculo: "{nome.lower()}"')
print(f'Seu Nome em Maiúsculo: "{nome.upper()}"')
print(f'Seu nome ao Todo tem "{len(nome) - nome.count(" ")}" Letras')
'Alternativa 1'
print(f'Seu primeiro nome tem "{nome.find(" ")}"')
'Alternativa 2'
separa = nome.split()
print(f'Seu primeiro nome é "{separa[0]}" e ele tem "{len(separa[0])}" Letras ')
