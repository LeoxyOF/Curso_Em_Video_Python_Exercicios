import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[1;31mO site não está acessível :(')
else:
    print('\033[1;32mO site está acessível! :)')