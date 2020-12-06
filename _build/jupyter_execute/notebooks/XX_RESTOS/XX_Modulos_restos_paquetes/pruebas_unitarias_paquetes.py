#!/usr/bin/env python
# coding: utf-8

# # Pruebas unitarias y paquetes
# **Autores**: Rogelio Mazaeda Echevarría, Félix Miguel Trespaderne.  

# ## Contenidos
# [Pruebas unitarias (unit_tests)](#Unit_tests)<br>
# [Biblioteca estándar y paquetes](#Biblioteca)

# ***
# <a id='Introducción'></a>

# ## Pruebas unitarias (Unit tests)
# 
# Una **buena práctica de programación** exige que comprobemos que el funcionamiento de nuestro código es el correcto, realizando **tests** que nos permitan asegurar, por ejemplo, que las **funciones** diseñadas cumplan con todos los requerimientos, y funcionen de forma correcta para todos los casos, incluidos los casos límite.
# 
# Si bien estos  **tests** son siempre necesarios, lo son aún más en el caso de los módulos que se supone contienen **funciones** y otros objetos programados de forma general, para formar parte de **bibliotecas** que van a ser utilizadas, una y otra vez, conformando diferentes programas. Un error en una función de este tipo de módulos compromete la fiabilidad de todos los programas que la utilizan.
# 
# Se recomienda entonces, que junto con el código de cada función, se diseñe e implemente también el código con aquellas llamadas que realizan los tests sobre esa función.
# 
# El mecanismo que ofrece la variable o atributo `__name__` para chequear mediante una sentencia condicional si un fichero fuente (`.py`) ha sido  ejecutado directamente o no, resulta muy apropiado para programar estos **test o pruebas unitarias** (**Unit Tests**).

# In[1]:


"""
Funciones para trabajar con polinomios
"""
def polyval(pol,x):
    y = 0
    for i, a in enumerate(pol):
        y += a*x**i
    return y

def polyder(pol):
    der = list(pol)
    der.pop()
    orden = len(der)
    for i, a in enumerate(der):
        der[i] *= orden - i
    return der

def conv(pol1,pol2):
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
            
                  
if __name__ == '__main__':
    pol = [5, 2, 1,0]
    der = polyder(pol)
    print('Polinomio {} evaluado en 1.0 da {}'.format(pol,polyval(pol,1)))
    print('derivada ', pol,der)
    print('convolución de {}*{} es {} '.format( pol, der, conv(pol,der)))


# En la celda anterior se muestra un fragmento del módulo `polinomios` que previamente ha sido introducido. 
# 
# Observe que aparecen definiciones de las funciones `conv()`, `polyder()` y `polyval()` para determinar la convolución (producto), la derivada y para evaluar un polinomio en un punto, respectivamente
# 
# La definición de estas funciones es el próposito fundamental de la existencia del módulo. En el caso de que el mismo sea importado por un guión u otro módulo, el código de estas definiciones sería ejecutado para crear los respectivos objetos. Sin embargo, en ese caso, como `__name__` tendría un valor diferente de `'__main__'` el código en el cuerpo del `if` no se ejecutaría.
# 
# Sin embargo, cuando el fichero que implementa el módulo es ejecutado directamente, entonces si se cumpliría la condición del `if` con lo cuál sería ejecutadas las llamadas a las funciones previamente definidas en el módulo, ofreciendo de esta forma la oportunidad ideal, para programar en este punto una serie de llamadas a las funciones del módulo, que sirva como **tests unitarios**, que demuestren, mediante ejemplos, la _corrección_ de las mismas.

# ## Paquetes (_Packages_)
# 
# A diferencia de los módulos, que están consituidos simplemente por un fichero con las funciones y clases que se exportan, los paquetes (_packages_) están compuestos por un conjuntos de ficheros .py que están organizados en un árbol de sub-directorios o carpetas en el disco duro del ordenador.
# 
# Los **paquetes** entonces imponen una determinada jerarquía a las objetos exportados, y constituyen el formato adecuado para distribuir librerías complejas.
# 
# Cada uno de los sub-directorios que conforman el **paquete** constituye un espacio de nombres (_**namesapace**_) concreto.
# 
# En cada uno de los directorios que contienen el **paquete**, debe existir un fichero de Python llamdado **__init__.py** con código que se ejecutará cuando se importe el espacio de nombres definido en dicho sub-directorio.
# 
# En este curso, no profundizaremos mucho más en este concepto. Simplemente mencionar su existencia, y comentar que mucho software disponible escrito para Python es ditribuido en forma de estos **paquetes**.

# ![numpy.jpg](attachment:numpy.jpg)

# **SciPy** es un ecosistema mediante el cual se distribuyen un conjunto de **paquetes** en los que se implementan algoritmos muy útiles para el con las matemáticas, la ingeniería y las ciencias en general.
# 
# [Enlace a SciPy web](https://www.scipy.org/)
# 
# Incluye los **paquetes**:
# - **numpy**: trabajo con matrices
# - **simpy**: matemática simbólica
# - **matplotlib**: gráficos
# - **scipy**: computación cientifica
# - **pandas**: estructuras y análisis de datos
# 
# En el esquema de la celda previa, se muesta una visión muy parcial del árbol de directorios de los paquetes: **matplotlib**, **numpy** y **scipy**. 
# 
# La intención es ilustrar la estructura jerarquíca que conforman cada uno de estos **paquetes**, mostrando solamente unos pocos de los muchos subdirectorios y fichero **.py** que contienen.
# 
# Ya se visto algunos programas que utilizan **matplotlib**, en el resto del curso veremos algunos temas de interés relacionados con el uso de algunos de los restantes **paquetes**
