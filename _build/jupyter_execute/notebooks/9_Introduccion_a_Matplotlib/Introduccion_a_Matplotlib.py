#!/usr/bin/env python
# coding: utf-8

# # Introducción a Matplotlib.
# **Autores**: Rogelio Mazaeda Echevarría, Félix Miguel Trespaderne.

# ## Contenidos
# [Introducción](#Introducción)<br>
# [Gráficos básicos](#Gráficos_básicos)<br>
# [Dibujando funciones de una variable](#Dibujando_funciones_de_una_variable)<br>
# [Título y etiquetas en ejes](#Título_y_etiquetas_en_ejes)<br>
# [La función `linspace()` del paquete Numpy](#La_función_linspace_del_paquete_Numpy)

# ***
# <a id='Introducción'></a>

# 
# ## Introducción
# 
# El paquete `matplotlib` es una extensa biblioteca de funciones para generar gráficos 2D y 3D.
# 
# Algunas de sus características son:
# 
# * Curva de aprendizaje suave: ofrece funcionalidades simples para usuarios ocasionales.
# * Todo tipo de ajustes *programables* de los elementos de una ventana gráfica. 
# * Gran variedad de formatos de exportación de las figuras.

# **Matplotlib** está construido sobre el paquete **Numpy** y trabaja de forma natural con los vectores y matrices (*arrays*) a ella asociados. Veremos más adelante las funcionalidades del paquete **Numpy**. Pero, por ahora, trabajaremos con las **listas nativas** de **Python** (que serán transformadas internamente a *numpy arrays* en las funciones del paquete **Matlotlib**). Nótese que restringimos el uso a listas formadas por valores del mismo tipo de dato.
# 
# Aunque no es la forma usual, utilizar en este momento listas nos permite:
# * visualizar desde ya los resultados de algunos de nuestros ejercicios.
# * nos obliga a practicar con el manejo de las estructuras de control; no olvidemos que nuestro objetivo es aprender a programar. De la otra forma, muchas operaciones de *bajo nivel* quedan ocultas detrás de las poderosas herramientas que nos brinda el paquete **Numpy**.

# Dentro del **paquete** `matplotlib` destaca el **módulo** `pyplot`.
# Este módulo **oculta** muchas de las funcionalidades de bajo nivel de la biblioteca permitiendo el
# uso de sencillas funciones para los elementos gráficos más habituales, tales como creación de figuras, trazado de líneas, visualización de imágenes, inserción de texto, etc.
# 
# En la bibliografía podéis encontrar otro módulo llamado `pylab` que tiene una funcionalidad similar, en apariencia incluso más simple. Sin embargo, su uso está hoy en día desaconsejado por diferentes razones que sería prolijo comentar.
# 
# El módulo `pyplot` emula el entorno de programación gráfica de **MATLAB**, herramienta software **de pago** muy popular en universidades y empresas. En la misma línea, ya hemos comentado que **Spyder** es un **IDE** muy similar al de **MATLAB**. Más adelante, en otras asignaturas o en vuestra vida profesional, si necesitáis *dar el cambio*, éste será sencillo.
# 
# Para comenzar usando el módulo `pyplot`de **Matplotlib** en un programa **Python** la forma estándar es:

# In[1]:


import matplotlib.pyplot as plt


# ***
# <a id='Gráficos_básicos'></a>

# ## Gráficos básicos
# 
# ### Función `plot()`
# Mediante la función `plot()` suministramos una lista para su trazado.

# In[2]:


lista = [6, 2, 5, 6, 8, 1, 3, 6, 7, 3]
plt.plot(lista)


# Por defecto, `plot(lista)` une con una línea la secuencia de puntos de coordenadas $(i,lista[i])$, siendo $i$ los índices válidos de la lista desde $0$. En nuestro ejemplo, los puntos $\{(0,6),(1,2),(2,5),...,(7,6),(8,7),(9,3)\}$.
# 
# Debe notarse que la figura donde reside la línea trazada se crea de forma automática para contener el dibujo. No sólo eso, en ausencia de indicaciones, se usan diferentes opciones por defecto, como tamaño de la figura, color y grosor de la línea, etc.

# Si proporcionamos dos listas, `plot(lista_x,lista_y)`, se une con una línea la secuencia de puntos de coordenadas $(lista\_x[i],lista\_y[i])$, siendo $i$ los índices válidos de las listas desde $0$. Es decir, la primera lista corresponde a las abcisas y la segunda a las ordenadas. Obviamente, ambas listas tendrán el mismo número de elementos. ¿Qué ocurre en caso contrario? ¡Prueba a eliminar un elemento de una de las listas!

# In[3]:


plt.plot([1.1, -3.23, 5.3, 7.34, 6.6, 0.1, 2.123, 4.17], [6, 2, 5.12, 6.25, 8.2, 1, -3.35, 6.3])


# ### Función `scatter()`
# Mediante la función `scatter()` podemos dibujar los puntos $(lista\_x[i],lista\_y[i])$ sin unir por líneas, apareciendo los puntos de forma *dispersa*.

# In[4]:


plt.scatter([1.1, -3.23, 5.3, 7.34, 6.6, 0.1, 2.123, 4.17], [6, 2, 5.12, 6.25, 8.2, 1, -3.35, 6.3])


# ***
# <a id='Dibujando_funciones_de_una_variable'></a>

# ## Dibujando funciones de una variable
# Un uso habitual de las herramientas gráficas es dibujar una función $y=f(x)$ para una colección de puntos en un intervalo de valores.
# 
# Por ejemplo, supongamos que deseamos dibujar la función $y=cos^2(x)$ utilizando $100$ puntos **equidistantes** en el intervalo $-2\pi\leq x\leq2\pi$.

# In[5]:


import matplotlib.pyplot as plt
import math
num_puntos = 100
x_min = -2*math.pi
x_max = -x_min

# Hay (num_puntos - 1) intervalos incluyendo x_min y x_max
incremento = (x_max - x_min)/(num_puntos - 1)

lista_x = [0]*num_puntos  # Rellenamos de 0's ambas listas. Así evitamos usar el método append().
lista_y = [0]*num_puntos
for i in range(num_puntos):
    x = x_min + i*incremento  # x va tomando los num_puntos valores equidistantes entre x_min y x_max
    lista_x[i] = x
    lista_y[i] = math.cos(x)**2

plt.plot(lista_x, lista_y)


# ### Dibujando varias gráficas superpuestas
# Es muy sencillo dibujar varias funciones superpuestas sin más que invocar a la función `plot()` de manera consecutiva, incluso con listas de abscisas diferentes. En el ejemplo, se añade una gráfica de la función $y=sin(x)cos(x)$ utilizando $50$ puntos en el intervalo $-3\leq x\leq3$.
# 
# Nótese cómo **Matplotlib** configura el gráfico de forma automática para adaptarse a los distintos rangos y eligiendo colores diferentes.

# In[6]:


num_puntos = 50
x_min = -3
x_max = -x_min

incremento = (x_max-x_min)/(num_puntos - 1)

lista_x2 = [0]*num_puntos
lista_y2 = [0]*num_puntos
for i in range(num_puntos):
    x = x_min + i*incremento
    lista_x2[i] = x
    lista_y2[i] = math.sin(x)*math.cos(x)

plt.plot(lista_x, lista_y)
plt.plot(lista_x2, lista_y2)


# ### Valores indefinidos en la lista de ordenadas

# La función **seno cardinal** desnormalizada $sinc(x)$ tiene por ecuación:
# 
# $$y = \frac{sin(x)}{x}$$
# 
# En la abscisa $x=0$, esta función presenta una singularidad evitable, que sabemos por la teoría de límites del cálculo que tiene el valor 1.
# 
# Sin embargo, cuando en un programa generamos los posibles valores de una función, no siempre el código está *sintonizado* para detectar estas singularidades. 
# 
# Vamos a elegir $301$ puntos en el intervalo $-15\leq x\leq15$. Sabemos que vamos a tener problemas si intentamos generar la lista de abscisas.

# In[7]:


import math
num_puntos = 301
x_min = -15
x_max = -x_min

incremento = (x_max-x_min)/(num_puntos - 1)

lista_x = [0]*num_puntos
lista_y = [0]*num_puntos
for i in range(num_puntos):
    x = x_min + i*incremento
    lista_x[i] = x
    lista_y[i] = math.sin(x)/x


# Vemos que se ha generado la excepción `ZeroDivisionError: float division by zero`.
# 
# Una opción que podemos emplear en este caso particular es evitar añadir a la lista de abscisas el valor $x=0$. Este método es engorroso, pues, en el caso general, para cada función debemos identificar previamente los valores conflictivos.  
# 
# Una opción más inteligente es capturar la **excepción** y, en esos casos, a esos valores conflictivos les asignamos como valor de la función un valor `float` especial llamado `nan`, **not a number**. La buena noticia es que cuando la función `plot()` detecta un valor `nan` en una lista, omite la representación de ese punto.
# > Por supuesto, en este ejemplo concreto también podemos asignar el valor $1$ de nuestro conocimiento de la *teoría de límites*.

# In[ ]:


import matplotlib.pyplot as plt
import math
num_puntos = 301
x_min = -15
x_max = -x_min

incremento = (x_max-x_min)/(num_puntos - 1)

lista_x = [0]*num_puntos
lista_y = [0]*num_puntos
for i in range(num_puntos):
    x = x_min + i*incremento
    lista_x[i] = x
    try:
        lista_y[i] = math.sin(x)/x
    except ZeroDivisionError:
        lista_y[i] = float('nan')  # Podríamos haber puesto en este ejemplo lista_y[i] = 1

plt.plot(lista_x, lista_y)


# En el siguiente ejemplo, dibujamos la función:
# $$y = \frac{cos(x)}{(x-10)(x+2)(x+12)}$$
# 
# que tiene 3 singularidades, pero nos *despreocupamos* con el método propuesto de su posición.

# In[ ]:


# Utilizamos lista de abscisas de la celda anterior
lista_y = [0]*len(lista_x)
for i, x in enumerate(lista_x):
    try:
        lista_y[i] = math.cos(x)/((x-10)*(x+2)*(x+12))
    except ZeroDivisionError:
        lista_y[i] = float('nan')

plt.plot(lista_x, lista_y)


# ***
# <a id='Título_y_etiquetas_en_ejes'></a>

# ## Título y etiquetas en ejes
# Mediante la función `title()` podemos añadir un título al gráfico. Mediante las funciones `xlabel()` e `ylabel()`añadimos etiquetas a los ejes de coordenadas.

# In[ ]:


plt.plot(lista_x, lista_y)
plt.title('Función con tres singularidades')
plt.xlabel('$x$')
plt.ylabel('${cos(x)}/{((x-10)(x+2)(x+12))}$')


# Estas son sólo un pequeño ejemplo de las enormes opciones de personalización que ofrece **Matplotlib**.

# ***
# <a id='La_función_linspace_del_paquete_Numpy'></a>

# ## La función `linspace()` del paquete Numpy
# Hemos visto un método relativamente engorroso de generar las abscisas:
# 1. Elegimos un límite inferior.
# 2. Elegimos un límite superior.
# 3. Decidimos cuantos puntos necesitamos.
# 4. Calculamos el tamaño del intervalo entre dos abscisas adyacentes.
# 5. Generamos la lista correspondiente.
# 
# La función `linspace()` del paquete **Numpy** hace todo esto de forma cómoda, proporcionándonos un nivel de **abstracción** superior y **encapsulando** todo ese código en una función. Basta introducir los 3 primeros parámetros como argumentos. Para utilizarla, debemos importar el paquete `numpy`.
# 
# Veámosla en acción para dibujar la función **campana de Gauss**:
# $$y = \frac{1}{{\sigma\sqrt{2\pi}}}e^{{-(x-\mu)^2}/{2\sigma^2}}$$
# 
# Elegiremos $1000$ valores en el intervalo $-5\leq x\leq5$ para una distribución normal de *media* $\mu=0$ y *desviación estándar* $\sigma=1$.

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import math

num_puntos = 1000
x_min = -5
x_max = 5
lista_x = np.linspace(x_min, x_max, num_puntos)

media = 0
desviacion_estandar = 1
factor = 1./(desviacion_estandar*math.sqrt(2*math.pi))
den = 2*desviacion_estandar**2

lista_y = [0]*num_puntos
for i, x in enumerate(lista_x):
    lista_y[i] = factor*math.exp((-(x-media)**2)/den)

plt.plot(lista_x, lista_y)
plt.title('Distribución de Gauss')
plt.xlabel('$x$')
plt.ylabel('$N({},{})$'.format(media, desviacion_estandar))


# In[ ]:




