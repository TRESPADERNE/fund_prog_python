#!/usr/bin/env python
# coding: utf-8

# # Comprensiones
# **Autores**: Rogelio Mazaeda, Félix Miguel Trespaderne.   

# ## Contenidos
# [Introducción](#Introducción)<br>
# [Comprensiones con listas](#compresiones_listas)<br>
# [Comprensiones con diccionarios](#compresiones_diccionarios)<br>
# [Comprensiones con conjuntos](#compresiones_sets)<br>

# ***
# <a id='Introducción'></a>

# ## Introducción.
# 
# Los recursos de creación y manipulación de colecciones que se han visto hasta ahora nos permiten enfrentar todo tipo de problemas concebibles.
# 
# Python es un lenguaje de muy alto nivel, que intenta  brindar al programador las herramientas más adecuadas para lidiar con el problema que se tenga entre manos. El utilizar una **abstracción** concreta u otra depende, en buena medida, del grado en que la misma se *acerque* al referente real que nuestro programa informático quiera representar o modelar.
# 
# En el caso de las colecciones como **listas**, **diccionarios** y **conjuntos**, un referente importante lo constituyen los conjuntos en matemáticas.
# 
# De nuestra formación previa en matemáticas, nos resulta familiar una notación concreta a la hora de referirnos a conjuntos. 

# Por ejemplo, si queremos caracterizar el conjunto de elementos que se obtiene tras elevar al cuadrado los primeros 10 enteros, lo podríamos describir de la siguiente forma:
# $$
# \begin{align}
# \\ \{x^2, \, x \in \aleph, \, 0 \leq x < 10 \}\\
# \end{align}
# $$
# 
# Supongamos que quisiéramos crear una lista de Python que representara esos números. Tendríamos varias alternativas, pero una de ellas es siempre el acudir a bucles como el que sigue:
# 
# ```python
# lista = []
# for x in range(10):
#     lista.append(x**2)
# ```
# 
# Pero en Python tenemos la posibilidad de utilizar la sintaxis de las **comprensiones** (**comprehensions**) para obtener un código muy escueto y cercano al referente matemático, de la siguiente forma:
# 
# ```Python
# lista = [x**2 for x in range(10)]
# ```

# In[1]:


lista = [x**2 for x in range(10)]
print(lista)


# ***
# <a id='compresiones_listas'></a>

# ## Comprensiones con listas
# 
# Las comprensiones se pueden aplicar a las colecciones ya vistas. La determinación de si se trata de una **lista**, un **diccionario** o un **conjunto** se realiza en base a la presencia o no de determinados elementos sintácticos como los corchetes `[]` para las listas, o la presencia de una *clave* para los diccionarios, que además deben estar provistos de  llaves, `{}`, etc. 
# 
# Para simplificar la explicación, nos centraremos inicialmente en las **comprensiones de listas**, las más utilizadas, para posteriormente abrir el abanico hacia las otras colecciones.
# 
# La sintaxis general sería:
# 
# ```python
# [expr(var_1 ... var_n) for var1 in iterable_1 [... for var_n in iterable_n] [if expr_bool]]  
# ```
# 
# - `expr(var_1 ...var_2)`: será una expresión de Python que en general involucra `n` variables.
# - A continuación, aparece un `for` que indica, mediante algún *iterable*, el dominio de los valores a considerar.
# - Se pueden poner tantos `for` como sean necesarios (los corchetes internos indican que estos son opcionales).
# - Puede opcionalmente aparecer un único `if` que determina la condición lógica a cumplir por las variables de todos los dominios para poder ser incluida en el conjunto resultante.

# In[2]:


pares = [x for x in range(0, 10, 2)]
impares = [x+1 for x in pares]
print(pares, impares)


# La lista ```pares``` esta compuesta para todos los elementos que cumplen que están en el rango de `[0,10[`, pero tomados de dos es dos.
# 
# Nótese que la variable `x` en la comprensión está **ligada** (**bound**) a la misma: su alcance está limitado a la comprensión donde está definida. 
# 
# La lista `impares` es conformada a su vez a partir de la lista `pares`. Obsérvese que de nuevo se usa  `x` para describir esta otra _comprensión_ con un significado diferente: ahora `x` *recorre* todos los elementos del _iterable_ `pares` para incluir su sucesor (`x + 1`).
# 
# Una alternativa para conformar los pares hubiera sido:

# In[3]:


pares = [x for x in range(10) if x%2 == 0]
pares


# La siguiente comprensión usa dos variables internas a la misma, las variables `x` e `y` y una variable _libre_ definida fuera de la comprensión, `desplazamiento`. Los elementos de la listas se calculan a partir de la expresión definida sobre esas variables, `x*y + desplazamiento`. Esta expresión es calculada mientras `x` _recorre_ la lista que se ofrece literalmente y mientras la variable `y` recibe los valores del iterable expresado por la función `range()`.  

# In[4]:


desplazamiento = 10
tabla = [x*y + desplazamiento for x in [1, 2, 3] for y in range(1, 5)]
tabla


# Nótese que la comprensión anterior sería la forma compacta del siguiente código:

# In[5]:


desplazamiento = 10
tabla = []
for x in [1, 2, 3]:
    for y in range(1, 5):
        tabla.append(x*y + desplazamiento)
tabla


# Otro ejemplo:

# In[6]:


lista_tuplas = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)
                if x != y and y != z and x != z]
lista_tuplas


# De nuevo, el código equivalente sería:

# In[7]:


lista_tuplas = []
for x in range(3):
    for y in range(3):
        for z in range(3):
            if x != y and y != z and x != z:
                lista_tuplas.append((x, y, z))
lista_tuplas


# En el siguiente ejemplo, se recibe una lista de tuplas, y se crea por _comprensión_ otra lista de valores simples, integrado por el primer miembro (convertido a `float`) de aquellas tuplas cuyo segundo miembro sea diferente de cero.

# In[8]:


original = [(1.5, 1), (2.1, 0), (3, 1), (4, 0), (10.5, 5)]
elegido = [float(x[0]) for x in original if x[1] != 0]
elegido


# En el siguiente ejemplo, se itera sobre una lista anidada, que puede representar una matriz, y se crea por comprensión, una lista (sin anidamientos) con todos los elementos de la matriz original. 

# In[9]:


lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_plana = [x for y in lista_anidada for x in y]
lista_plana


# Observe que la variable interna `y` representa cada una de las sublistas (o las filas) de la lista anidada (matriz). Mientras que `x` itera por cada uno de los elementos de esas filas.

# En el siguiente ejemplo se crea, de una manera muy sintética, una matriz de 3x3 inicializada a cero, usando una comprensión anidada en otra.

# In[10]:


matriz = [[0 for col in range(3)] for row in range(3)]
matriz


# ***
# <a id='compresiones_diccionarios'></a>

# ## Comprensiones con diccionarios
# 
# Las listas son las colecciones más utilizadas, pero el concepto de _comprensiones_ es igualmente útil para crear de forma muy sintética **diccionarios** y **conjuntos**.
# 
# Lo único que se debe tener en cuenta es respetar la sintaxis de cada uno.
# 
# ```python
# {expr_clave(x_1,...x_n): expr_dato(x_1,...x_n) for x_1 in _iterable_1_ [...for x_n in _iterable_v] if exp_boll}
# ```
# Para los diccionarios, se utilizan los delimitadores ```{}``` y se plantean expresiones para la _clave_ y los datos.

# In[11]:


from math import sqrt, log

delta = 0.1

abscisas = [round(float(x)/10 + delta, 1) for x in range(20)]

tabla = {x: log(sqrt(x**5)) for x in abscisas}
tabla


# En el ejemplo previo, se crea un diccionario que *implementa* una tabla a partir de evaluar una expresión matemática para cada uno de los elementos de una lista de reales creada previamente.
# 
# Otro ejemplo:

# In[12]:


ascii = {ch: ord(ch) for ch in "abcdefghijklmnopqrstvwxyx"}
ascii


# ***
# <a id='compresiones_sets'></a>

# ## Comprensiones con conjuntos
# 
# Para el caso de **conjuntos**, la sintaxis sería:
# 
# ```python
# {expr_dato(x_1,...x_n) for x_1 in _iterable_1_ [...for x_n in _iterable_v] if exp_boll}
# ```
# El elemento distintivo fundamental de los conjuntos es el hecho de que la propia colección garantiza que sus elementos nunca están repetidos, por así decirlo, los _filtra_.

# In[13]:


cadena = "Una cadena con palabras repetidas. La cadena es filtrada. Resultado: cadena con palabras sin repetir"
palabras_usadas = {pal for pal in cadena.split()}
palabras_usadas

