from time import sleep
print('\033[1:35mNúmeros Pares de 0 á 50!\033[m')
for n in range(0, 50+1, 2):
    print('\033[1;33m',n, end="")
    sleep(0.1)