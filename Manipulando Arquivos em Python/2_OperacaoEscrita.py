arquivo = open(
    "/Users/Levy Costa/Documents/GitHub/Vivo-Python-AI-Backend-Developer/Manipulando Arquivos em Python/teste.txt","w"
)
arquivo.write("Olá, mundo!")
arquivo.writelines(['\n', 'Aprendendo ', 'Python ', 'é ', 'divertido!'])
arquivo.close()