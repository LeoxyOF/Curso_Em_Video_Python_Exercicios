try:
    # operação
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    # se der errado
    print(f'Deu errado :( o erro foi {erro.__class__}')
else:
    # se der certo
    print(f'O resultado é {r:.1f}')
finally:
    # aparece mesmo se der certo ou se der errado
    print('Volte sempre :)')


'------------------------------------------------------------------------------------------------------------------------------'


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre :)')
