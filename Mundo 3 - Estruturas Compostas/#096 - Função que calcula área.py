def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de m².')

print('Controle de Terrenos')
print('-' * 20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
