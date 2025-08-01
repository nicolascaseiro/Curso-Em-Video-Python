from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p, True))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p, True))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(p, 10, True))}')
