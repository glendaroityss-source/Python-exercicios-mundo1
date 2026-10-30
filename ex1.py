Pergunta=input('Digite algo: ')
e_numero=Pergunta.isnumeric()
e_letra=Pergunta.isalpha()
if e_numero== True:
    print('O que foi digitado é um número.')
if e_letra== True:
    print('O que foi digitado é uma Palavra')
if ' ' in Pergunta:
    print('O que foi digitado é uma Palavra')
if ' ' and e_numero and e_letra:
    print('O que foi digitado é palavra e número misturado')








