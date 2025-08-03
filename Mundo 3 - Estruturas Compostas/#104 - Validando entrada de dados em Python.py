def leiaInt(mensagem):
    ok = False
    valor = 0
    while True:
        n = int(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            ok = True
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digita o número {n}')
