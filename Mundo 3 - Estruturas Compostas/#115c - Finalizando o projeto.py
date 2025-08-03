from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arquivo = 'cursoemvideo.txt'

if arquivoExiste(arquivo):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver pessoa cadastrada', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO. Digite uma opção válida.\033[m')
    sleep(2)
    
