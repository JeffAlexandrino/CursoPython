def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.
    
    :param n: O número a ser calculado o fatorial.
    :param show: (opcional) Mostrar ou não o processo de cálculo.
    :return: O valor do fatorial de n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f

# Exemplo de uso
print(fatorial(5, show=True))