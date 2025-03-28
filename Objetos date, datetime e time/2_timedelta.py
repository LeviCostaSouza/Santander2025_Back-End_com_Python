from datetime import datetime, timedelta, date, time

tempo_pequeno = 30

tempo_medio = 60

tempo_grande = 120

data_atual = datetime.now()


tipo_carro = input('Qual o porte do seu carro?\nP - Pequeno\nM - Médio\nG - Grande\nDigite a opção desejada:').upper()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'Estimativa de retirada do carro: {data_estimada.strftime("%d/%m/%Y %H:%M:%S")}')

elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'Estimativa de retirada do carro: {data_estimada.strftime("%d/%m/%Y %H:%M:%S")}')

else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'Estimativa de retirada do carro: {data_estimada.strftime("%d/%m/%Y %H:%M:%S")}')


#TESTES COM DATE,DATETIME E TIMEDELTA

resultado = datetime(2025,7,28) - timedelta(hours=1)
print(resultado.time())
