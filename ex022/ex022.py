print('-=-=- Analisando de Textos -=-=-')

nome = str(input('Digite seu nome aqui: ')).strip()

print(f'Seu nome em letra maiúscula é {nome.upper()}')
print(f'Seu nome em letras minúsculas é {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print(f'Seu primeiro nome é {} e ele tem [{}] letras')