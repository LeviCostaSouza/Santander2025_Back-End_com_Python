from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH/'lorem.txt', 'r') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f'Erro ao abrir arquivo: {exc}')


try:
    with open(ROOT_PATH/'arquivo-utf-8.txt', 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f'Erro ao abrir arquivo: {exc}')
except UnicodeDecodeError as exc:
    print(exc)