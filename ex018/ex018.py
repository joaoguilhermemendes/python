print('-=-=- Seno, Cosseno e Tangente -=-=-')

import math

angulo = int(input('Digite um ângulo que você deseja: '))

print(f'O ângulo de {angulo} tem o SENO {math.sin(math.radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO {math.cos(math.radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE {math.tan(math.radians(angulo)):.2f}')