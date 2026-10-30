import random
alunos = input('Digite o nome dos alunos: ').split()
sequencia = random.sample(alunos, k=len(alunos))
print(f'a sequencia será: {sequencia}')
