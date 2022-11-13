from time import sleep
print('\033[1;33m======== Tabuada ========')
resp = int(input('Digite o valor: '))
for a in range(1, 10+1):
    print(f'\033[1;35m{resp}x{a} = {resp * a}')
    sleep(0.5)

