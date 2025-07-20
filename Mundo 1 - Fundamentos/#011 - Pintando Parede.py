largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = largura * altura
print(f'Sua parede de dimensão {largura}x{altura} tem a área de {area}')
tinta = area / 2
print(f'Para pintar essa parede, você precisará de {tinta} de tinta')
