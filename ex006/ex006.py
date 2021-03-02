print('-=-=- Dobro, triplo e raiz quadrada -=-=-')

import math

num = int(input('Digite uma valor: '))

dobro = num * 2
triplo = num * 3
rq = num ** (1/2)
#rq =  pow(num, (1/2))

print(f'O número [{num}] tem como dobro --> [{dobro}]')
print(f'O número [{num}] tem como triplo --> [{triplo}]')
print(f'O número [{num}] tem como raiz quadrada --> [{rq}]')

#print(f'O número tem como (DOBRO --> {num*2})   (TRIPLO --> {num*3})   (RAIZ QUADRADA --> {num**(1/2)})')