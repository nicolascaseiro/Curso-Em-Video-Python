casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o salário do comprador: R$'))
anos = int(input('Informe quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 0.30
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos')
print(f' a prestação será de R${prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo CONCEDIDO')
else:
    print('Empréstimo NEGADO')
