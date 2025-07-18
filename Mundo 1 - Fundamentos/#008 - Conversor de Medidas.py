medida = float(input('Digite uma distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 0.001
cm = medida * 100
mm = medida * 1000
print(f'{medida:.0f} metros\n')
print(f'{km:.0f} quilometros')
print(f'{hm:.0f} hectometros')
print(f'{dam:.0f} decâmetros')
print(f'{dm:.0f} decímetros')
print(f'{cm:.0f} centímetros')
print(f'{mm:.0f} milímetros')
