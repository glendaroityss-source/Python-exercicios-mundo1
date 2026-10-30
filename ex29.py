velocidade = int(input('Qual é a velocidade do carro?'))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Boa viagem e mantenha essa velocidade!')
else:
    print(f'Você ultrapassou a velocidade permitida, sua multa será de R${multa}')