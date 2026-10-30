import random
nomes = input('Digite o nome dos alunos: ' ).split()
random.shuffle(nomes)
print(f'A sequencia será {nomes}')
