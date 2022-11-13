from ex115guanabara import interface
from ex115guanabara import arquivos
from time import sleep

arq = 'pessoas.txt'

if not arquivos.arquivoExiste(arq):
    arquivos.criarArquivo(arq)

while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        arquivos.lerArquivo(arq)
    elif resposta == 2:
        interface.cabecalho("Novo cadastro")
        nome = str(input('Nome: ')).strip().title()
        idade = interface.lerint("Idade: ")
        arquivos.cadastrar(arq, nome, idade)
    elif resposta == 3:
        interface.cabecalho("Saindo do sistema...... Até logo!")
        break
    else:
        print("\033[1;31mERRO! Digite uma opção válida!\033[m")
        sleep(2)
