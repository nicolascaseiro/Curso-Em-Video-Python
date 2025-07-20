preco = float(input('Informe o preço do produto: R$'))
novo_preco = preco - (preco * 0.05)
print(f'O produto que custava R${preco:.2f}, com 5% de desconto custará {novo_preco}')
