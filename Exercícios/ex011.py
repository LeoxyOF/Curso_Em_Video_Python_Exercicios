print('Faça um programa que leia a altura e a largura da parede')
print('em metros e calcule sua área e a quantidade de tinta necessária para')
print('pintá la sabendo a cada litro de tinta pinta uma área de 2m².')
lar =int(input("->Largura da Parede: "))
alt =int(input("->Altura da Parede: "))
Mult =lar*alt
Div =Mult/2
print(f'Será Necessário {Div:.0f} Litros de Tinta para Pintar a Parede.')
