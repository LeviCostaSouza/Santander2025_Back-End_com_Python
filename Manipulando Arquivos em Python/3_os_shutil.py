import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH / 'novo-diretorio') # Cria um novo diretório

arquivo = open(ROOT_PATH / 'novo.txt', 'w') # Abre um arquivo em modo escrita
arquivo.close()

os.rename(ROOT_PATH / 'novo.txt', ROOT_PATH / 'alterado.txt') # Renomeia um arquivo

os.remove(ROOT_PATH / 'alterado.txt')

shutil.move(ROOT_PATH / 'novo.txt', ROOT_PATH / 'novo-diretorio') # Move um arquivo para um diretório