distancia = int(input('Quantos km sua viagem terá? '))
km_45 = 0.45 * distancia
km_50 = 0.50 * distancia
if distancia <= 200:
    print(f'Sua viagem ficará no valor de R${km_50:.2f}')
else:
    print(f'Sua viagem ficará no valor de R${km_45:.2f} com nossa promoção!')