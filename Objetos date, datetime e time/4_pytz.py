import pytz
from datetime import datetime

data_oslo = datetime.now(pytz.timezone('Europe/Oslo'))
data_sao_paulo = datetime.now(pytz.timezone('America/Sao_Paulo'))

print(f'Data e hora em Onslo: {data_oslo}')

print(f'Data e hora em São Paulo: {data_sao_paulo}')