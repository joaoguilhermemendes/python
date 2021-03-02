print('-=-=- Conversor de medidas -=-=-')

num = int(input('Digite uma distância em metros: '))

km = num/1000
hm = num/100
dam = num/10
dm = num*10
cm = num*100
mm = num*1000

print(f'A medida de {num} equivale a: ')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm}dm')
print(f'{cm}cm')
print(f'{mm}mm')




