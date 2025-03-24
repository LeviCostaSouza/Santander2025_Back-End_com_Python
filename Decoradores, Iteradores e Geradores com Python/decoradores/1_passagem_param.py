def mensagem(nome):
    print ('Executando mensagem')
    return f'Olá {nome}!'

def mensagem_longa(nome):
    print ('Executando mensagem longa')
    return f'Olá {nome}, seja bem-vindo ao nosso sistema!'

def executar(funcao,nome):
    print ('Executando funcao')
    return funcao(nome)

print(executar(mensagem,'Levi'))
print(executar(mensagem_longa,'Levi'))