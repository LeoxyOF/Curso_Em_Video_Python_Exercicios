frase = str(input('Digite uma Frase: ')).strip().upper()
print(f'A Letra "A" Aparece {frase.count("A")} vezes na frase')
print(f'A primeira letra "A" aparece na posição "{frase.find("A")+1}"')
print(f'A última letra "A" aparece na posição "{frase.rfind("A") - frase.count(" ")+1}"')
#2
fras = str(input('Digite uma Frase: ')).strip().upper()
if "A" in fras:
    print(f'A Letra "A" Aparece {fras.count("A")} vezes na frase')
    print(f'A primeira letra "A" aparece na posição "{fras.find("A")+1}"')
    print(f'A última letra "A" aparece na posição "{fras.rfind("A") - fras.count(" ")+1}"')
else:
    print('Sua frase não tem A')
