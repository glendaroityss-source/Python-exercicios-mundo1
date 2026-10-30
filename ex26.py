frase = str(input('Digite uma frase:')).lower().strip()
frase_filtrada = frase.count('a')
if frase_filtrada < 2:
    print(f'Na sua frase a letra "a" aparece {frase.count('a')} vez')
else:
    print(f'Na sua frase a letra "a" aparece {frase_filtrada} vezes')
print(f'A letra "a" aparece primeiro na posição {frase.find('a')+1}')
print(f'E a última vez aparece na posição {frase.rfind('a')+1}')