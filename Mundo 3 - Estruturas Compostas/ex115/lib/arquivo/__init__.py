from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for p in a:
            data = p.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<35}{data[1]:^3} years')
    finally:
        a.close()


def register(file, nome='unknow', age=0):
    try:
        a = open(file, 'at')
    except:
        print('Error while attempting to read file.')
    else:
        try:
            a.write(f'{nome};{age}\n')
        except:
            print('There was an error while writing the data.')
        else:
            print(f'New person registered: {nome}')
            a.close()




