def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
           return n

def linha(tam=42):
    return '=' * tam

def cabecalho(msg):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('\033[040mMENU PRINCIPAL\033[m')
    c = 1
    for items in lista:
        print(f'\033[33m{c} - \033[34m{items}\033[m')
        c += 1
    print(linha())
    opcao = leiaInt('\033[32mSua opção: \033[m')
        return opcao



