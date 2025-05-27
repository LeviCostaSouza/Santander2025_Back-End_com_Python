import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH/'usuarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id','nome'])
        escritor.writerow(['1','João'])
        escritor.writerow(['2', 'Maria'])
except IOError as exc:
    print(f"Erro ao criar o arquivo: {exc}")

try:
    with open(ROOT_PATH/'usuarios.csv', 'r', newline='', encoding='utf-8')as arquivo:
        leitor = csv.reader(arquivo)
        for idx, linha in enumerate(leitor):
            if idx == 0:
                continue
            print(f"ID: {linha[0]}, Nome: {linha[1]}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")

#try:
#    with open(ROOT_PATH/'usuarios.csv', 'w', newline='') as csvfile:
#        reader = csv.DictReader(csvfile)
#        for linha in reader:
#            print(f'ID: {linha['id']}')
#            print(f'Nome: {linha['nome']}')
#except IOError as exc:
#    print(f"Erro ao abrir o arquivo: {exc}")