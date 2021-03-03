print('-=-=- Aluguel de carros -=-=-')

dias = int(input('Quantos dias usou o veículo? '))
kms = int(input('Quantos Kms rodou? '))

print(f'O valor a ser pago é de --> R${(60*dias) + (0.15*kms)}')