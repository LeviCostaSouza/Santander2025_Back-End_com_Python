arquivo = open(
    "C:/Users/Levy Costa/Documents/GitHub/Vivo-Python-AI-Backend-Developer/Manipulando Arquivos em Python/lorem.txt", "r"
)
print(arquivo.read()) # Ler o arquivo inteiro
print(arquivo.readline()) # Ler linha a linha do arquivo
print(arquivo.readlines()) # Ler todas as linhas do arquivo, em lista
arquivo.close()