'''import math
n1 = float(input('Digite o valor do primeiro cateto:'))
n2 = float(input('Digite o valor do segundo cateto:'))
resposta = math.hypot(n1, n2)
print(f'A hipotenusa dos catetos {n1} e {n2} é {resposta:.3f}')'''
'''import math
n1 = float(input('Digite o valor do cateto adjacente: '))
n2 = float(input('Digite o valor do cateto oposto: '))
hipotenusa = math.sqrt(n1**2 + n2**2)
print(f'a hipotenusa dos catetos {n1} e {n2} é {hipotenusa:.2f}')'''

n1 = float(input('Digite o valor do cateto adjacente: '))
n2 = float(input('Digite o valor do cateto oposto: '))
hipotenusa = (n1**2 + n2**2)**0.5
print(f'a hipotenusa dos catetos {n1} e {n2} é {hipotenusa:.2f}')



