times = ('Cruzeiro', 'Flamengo', 'Palmeiras', 'Bragantino',
    'Botafogo', 'Bahia', 'Mirassol', 'Fluminense',
    'Atlético-MG', 'Internacional', 'Corinthians', 'Ceará SC',
    'Grêmio', 'São Paulo', 'EC Vitória', 'Vasco da Gama',
    'Santos', 'Juventude', 'Fortaleza', 'Sport Recife')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 6 primeiros são {times[0:6]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Botafogo está na {times.index('Botafogo')+1}ª posição')
