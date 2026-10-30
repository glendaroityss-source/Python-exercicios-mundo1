#salario superiores a 1250, terão o aumento de 10%, abaixo disso será 15%
salario_atual = float(input('Quanto é o seu salário atual? '))
salario_10 = (salario_atual * 0.10) + salario_atual
salario_15 = (salario_atual * 0.15) + salario_atual
if salario_atual <= 1250:
    print(f'Seu salário terá um reajuste de 15%, você passará a receber {salario_15:.2f}')
else:
    print(f'Seu salário terá um reajuste de 10%, você passará a receber {salario_10:2f}')