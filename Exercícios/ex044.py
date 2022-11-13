print('\033[1;40m============ Carrefour ============\033[m')
preco = float(input('\033[1;33mPreço dos produtos: '))
print('\033[1;31m------Opções------\n\033[1;35m[1] Á vista dinheiro/cheque: 10% de desconto\n\033[1;34m[2] Á vista no cartão: 5% de desconto')
print('\033[1;31m[3] Em até 2x no cartão: Preço Normal\n\033[1;32m[4] 3x ou mais no cartão: 12% de juros\n')
forpa = str(input('\033[1;33mQual a forma de pagamento? ')).strip().lower()
#Á vista dinheiro/cheque: 10% de desconto
if forpa == '1':
    a = preco*0.10
    b = preco - a
    print(f'\033[1;35mVocê irá pagar R${b:.2f} com um desconto de 10% aplicado\033[m')
#Á vista no cartão: 5% de desconto
elif forpa == '2':
    a = preco*0.05
    b = preco - a
    print(f'\033[1;34mVocê irá pagar R${b:.2f} com um desconto de 5% aplicado\033[m')
#Em até 2x no cartão: Preço Normal
elif forpa == '3':
    print(f'\033[1;31mVocê irá pagar uma parcela de R${preco / 2:.2f} e outra de R${preco / 2:.2f} sem nenhum desconto aplicado')
#3x ou mais no cartão: 20% de juros
elif forpa == '4':
    total = preco + (preco * 12 / 100)
    a = int(input('Quantas parcelas? '))
    parc = total / a
    print(f'\033[1;32mSua compra será parcelada em {a}x de R${parc:.2f} com juros, \033[1;34mNo final sua compra de R${preco:.2f} vai custar R${total:.2f}')