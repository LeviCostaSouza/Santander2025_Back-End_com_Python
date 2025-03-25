def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar a funcao')
        funcao(*args, **kwargs)
        print('Faz algo depois de executar a funcao')

    return envelope

@meu_decorador
def ola_mundo(nome, qualquer_coisa):
    print(f'Olá Mundo {nome}!')

ola_mundo("Joao", 1000)