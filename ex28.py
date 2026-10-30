import random
import time
aleatorio = random.randint(1, 5)
print('Vamos jogar, tente adivinhar qual número eu vou colocar na tela de 1 a 5')
n_usuario = int(input('Pense e digite aqui:'))
print('PROCESSANDO...')
time.sleep(3)
print(f'Eu pensei em {aleatorio}')
if n_usuario == aleatorio:
    print('Você ganhou, PARABÉNS!')
else:
    print('Você perdeu... Tente novamente!')

