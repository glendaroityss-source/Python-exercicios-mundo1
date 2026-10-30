import random
lista_nomes = input('Digite o nome dos alunos a serem sorteados ').split()
sorteio = random.choice(lista_nomes)
print(f'O aluno(a) sorteado é {sorteio}')

