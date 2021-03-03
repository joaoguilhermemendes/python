print('-=-=- Cateto e hipotenusa -=-=-')

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

a = co**2 + ca**2
b = a**0.5

print(f'A hipotenusa vai medir {b:.2f}')
