# -*- coding: utf-8 -*-
"""
Funciones para trabajar con polinomios
"""

def polyval(pol,x):
    

    ''' 
    Función para evaluar un polinomio
    
    Parameters
    ----------
    pol : LISTA
        POLINOMIO.
    x : FLOAT
        ABSCISA.

    Returns
    -------
    FLOAT.

    '''
    y = 0
    for i, a in enumerate(pol):
        y += a*x**i
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
    >>> print(polyder([2, 5, 3, 1))
    [6, 10, 3]
    '''
    
    der = list(pol)
    der.pop()
    orden = len(der)
    for i, a in enumerate(der):
        der[i] *= orden - i
    return der

def conv(pol1,pol2):
    '''
    Devuelve lista con convolución de dos polinomios

    Parameters
    ----------
    pol1 : LISTA
        POLINOMIO FACTOR 1.
    pol2 : LISTA
        POLINOMIO FACTOR 1.

    Returns
    -------
    POLINOMIO CONVOLUCIóN.

    '''
    orden1, orden2 = len(pol1) -1, len(pol2) - 1
    if orden1 < 0 or orden2 < 0:
        producto = None
    else:
        orden = orden1 + orden2
        producto = [0]*(orden + 1)
        for i, elem1 in enumerate(pol1):
            for j, elem2 in enumerate(pol2):
                producto[i + j] += elem1*elem2
    return producto
            
        
            
        
if __name__ == "__main__":
    pol = [5, 2, 1,0]
    der = polyder(pol)
    print('Polinomio {} evaluado en 1.0 da {}'.format(pol,polyval(pol,1)))
    print('derivada ', pol,der)
    print('convolución de {}*{} es {} '.format( pol, der, conv(pol,der)))