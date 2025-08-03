from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = ('cursoemvideo.txt')
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver pessoa cadastrada', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        nome = str(input('Nome: '))
        age = leiaInt('Age: ')
        register(arquivo, nome, age)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO. Digite uma opção válida.\033[m')
    sleep(1)

