"""
Funciones para trabajar con polinomios
"""

def polyval(pol, x):
    ''' 
    Función para evaluar un polinomio
    
    Parameters
    ----------
    pol: list
        Polinomio
    x: float
        Abscisa

    Returns
    -------
    float
        Valor del polinomio en la abscisa x
    Example
    -------
    >>> print(polyval([2, 5, 3, 1], 2.1))
    47.872
    '''
    y = 0
    orden = len(pol) - 1
    for i, coef in enumerate(pol):
        y += coef*x**(orden-i)
    return y


def polyder(pol):
    '''
    Devuelve el polinomio derivada.
    Parameters
    ----------
    pol: list
        Polinomio a derivar.

    Returns
    -------
    list
        Lista con los coeficientes del polinomio derivada.
    Example
    -------
    >>> print(polyder([2, 5, 3, 1]))
    [6, 10, 3]
    '''

    der = list(pol)
    der.pop()
    orden = len(der)
    for i, a in enumerate(der):
        der[i] *= orden - i
    return der


def polyconv(pol1, pol2):
    '''
    Devuelve lista con convolución de dos polinomios

    Parameters
    ----------
    pol1: list
        Polinomio 1.
    pol2: list
        Polinomio 2.

    Returns
    -------
    list
        Polinomio convolución
    Example
    -------
    >>> print(polyconv([2, 5, 3, 6], [2, 4]))
    [4, 18, 26, 24, 24]

    '''
    orden1, orden2 = len(pol1) - 1, len(pol2) - 1
    if orden1 < 0 or orden2 < 0:
        producto = None
    else:
        orden = orden1 + orden2
        producto = [0]*(orden + 1)
        for i, elem1 in enumerate(pol1):
            for j, elem2 in enumerate(pol2):
                producto[i + j] += elem1*elem2
    return producto


if __name__ == '__main__':
    pol = [4, 3, 2, 1]
    assert polyder(pol) == [12, 6, 2]
    print('Test -> polyder(pol) == [12, 6, 2]\nOk')
    assert polyval(pol, 0.) == 1.
    print('Test -> polyval(pol, 0.) == 1.\nOk')
    assert polyval(pol, 1.) == 10.
    print('Test -> polyval(pol, 1.) == 10.\nOk')
    assert polyval(pol, 2.) == 49.
    print('Test -> polyval(pol, 2.) == 49.\nOk')
    assert polyconv(pol, pol) == [16, 24, 25, 20, 10, 4, 1]
    print('Test -> polyconv(pol, pol) == [16, 24, 25, 20, 10, 4, 1]\nOk')