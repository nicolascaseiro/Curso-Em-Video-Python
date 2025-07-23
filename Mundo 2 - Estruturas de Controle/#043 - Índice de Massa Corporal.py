peso = float(input('Informe o seu peso em KG: '))
altura = float(input('Informe a sua altura em M: '))
imc = peso / (altura ** altura)
print(f'O IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal')
elif 18.5 <= imc < 25:
    print('Você está na faixa de peso IDEAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA')
