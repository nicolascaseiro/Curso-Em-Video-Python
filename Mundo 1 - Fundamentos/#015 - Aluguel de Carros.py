dias = int(input('Informe a quantidade de dias alugados: '))
km = float(input('Informe a quantidade de km rodados: '))
pago = (dias * 60) + (km * 0.15)
print(f'O total a pagas é de R${pago:.2f}')
