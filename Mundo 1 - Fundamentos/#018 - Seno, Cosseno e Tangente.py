from math import radians, sin, cos, tan
angulo = float(input('Informe o ângulo: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo}º tem o SENO de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo}º tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo}º tem a TANGENTE de {tangente:.2f}')
