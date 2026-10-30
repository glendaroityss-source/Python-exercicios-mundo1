dias = int(input('Por quantos dias você alugou o carro?'))
km = float(input('Quantos km você percorreu com o carro?'))
soma_dias = dias * 60
limite_km = 300
if km > limite_km:
     soma_dias += (km - limite_km) * 0.15
print(f'O total a ser pago é {soma_dias:.2f}')



