def linha(tam= 32):
    return '-' * tam

def cabeçlho(txt):
    print(linha())
    print(txt.center(32))
    print(linha())

cabeçlho('BEM VINDOS, A treinamentos!')