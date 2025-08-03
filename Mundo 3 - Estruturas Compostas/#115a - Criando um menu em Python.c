from ex115.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoa cadastrada', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO. Digite uma opção válida.\033[m')
    sleep(2)
