produto = float(input('Qual o preço do produto? R$'))
desconto = produto - ((5*produto) / 100)
print(f'O produto que custava R${produto}, na promoção com 5% de desconto, custará {desconto:.2f}')


