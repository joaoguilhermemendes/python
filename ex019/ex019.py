print('-=-=- Sorteando item na lista -=-=-')

from random import choice

aluno1 = str(input('Digite o nome de um aluno: '))
aluno2 = str(input('Digite o nome de um aluno: '))
aluno3 = str(input('Digite o nome de um aluno: '))
aluno4 = str(input('Digite o nome de um aluno: '))

lista = (aluno1, aluno2, aluno3, aluno4)

print(f'O estudante sorteado foi --> {choice(lista)}')