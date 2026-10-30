lista_n = []
n1 = int(input('Escreva o primeiro número: '))
n2 = int(input('O segundo: '))
n3 = int(input('E por fim, o terceiro: '))
lista_n.append(n1)
lista_n.append(n2)
lista_n.append(n3)
print(f'O menor valor é {min(lista_n)}')
print(f'O maior valor é {max(lista_n)}')
