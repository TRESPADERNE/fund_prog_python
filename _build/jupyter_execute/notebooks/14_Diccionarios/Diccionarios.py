#!/usr/bin/env python
# coding: utf-8

# # Diccionarios
# **Autores**: Rogelio Mazaeda, Félix Miguel Trespaderne.   

# ## Contenidos
# [Introducción](#Introducción)<br>
# [Diccionarios](#Diccionarios)<br>
# [Diccionarios_versus_listas](#Diccionarios_vs_listas)<br>
# [Operaciones con diccionarios](#Operacciones_con_diccionarios)<br>
# [El diccionario como iterable](#El_diccionario_como_iterable)<br>
# [Ejemplos con Diccionarios](#Ejemplos)

# ***
# <a id='Introducción'></a>

# ## Introducción.
# 
# La posibilidad de crear en memoria y manipular de una manera consistente, conjuntos o colecciones de datos, es una funcionalidad básica que brindan los lenguajes de programación. Python es particularmente eficaz en este cometido, porque ofrece muchos de estos tipos de datos compuestos.
# 
# Ya se ha visto con cierto detalle el tipo de datos **lista**. Representa un conjunto **secuencial** (con un orden implícito) de datos, que pueden ser de diferentes tipos. En la lista, la forma de acceder a los elementos es mediante el uso de un **índice** entero, que comienza en cero y que puede interpretarse como el *desplazamiento* a realizar desde el inicio de la lista hasta el elemento buscado. La lista es, desde luego, la colección más utilizada y es la adecuada para muchas aplicaciones.
# 
# En otros casos, una organización diferente del conjunto de datos resulta más apropiada. 
# 
# Los **diccionarios** son colecciones en las que los datos almacenados no son *identificados* por un índice entero, sino por una **clave** (**key**) que, para cada colección, puede ser de diferente tipo.
# 
# Entonces, la operación de acceso a los elementos del diccionario exige *presentar* la **clave** que lo identifica.
# 
# ```python
# primer_semestre = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio'}
# 
# print('El primer mes es:', primer_semestre[1])
# ```

# ***
# <a id='Diccionarios'></a>

# ## Diccionarios
# 
# Los **diccionarios** son colecciones **iterables**, **no secuenciales** y **mutables** donde cada elemento está compuesto de una **clave** (que identifica de modo único al elemento) y el dato que se desea almacenar.
# 
# Sintaxis:
# ```python
#     {clave_1: dato_1, clave_2: dato_2, ..., clave_n: dato_n} 
# ```
# 
# Nótese el uso de llaves `{..., ...}` en lugar de corchetes `[..., ...]`.
# 
# #### Ejemplos:

# In[1]:


num = {1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro'}

asig = {'asignatura': 'Fundamentos de Programación', 'creditos': 6, 'tipos': ['teoría', 'prácticas']} 

nom = {'persona': {'nombre': 'María', 'primer apellido': 'García', 'segundo apellido': 'Pérez'}, 'edad': 30}


print(num)
print(asig)
print(nom)


# Como se observa, los **diccionarios** presentan una gran flexibilidad. Los datos pueden ser de cualquier tipo: datos simples, listas, incluso otros diccionarios, etc., con cualquier nivel de anidamiento. Las claves, sin embargo, tiene que ser tipos inmutables (enteros, cadenas, tuplas).
# 
# Para acceder individualmente a los elementos de los diccionarios, se utiliza la sintaxis de los corchetes.

# In[2]:


num = {1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro'}

print(num[1])


# En el caso de tener estructuras más complejas (anidadas) se deberá proceder en consecuencia. Por ejemplo:

# In[3]:


nom = {'persona': {'nombre': 'María', 'primer apellido': 'García', 'segundo apellido': 'Pérez'}, 'edad': 30}

print(nom['persona']['primer apellido'])


# En el ejemplo, en la clave `persona` del diccionario `nom`,  se almacena a su vez otro diccionario. Para acceder a la clave `primer apellido` del diccionario anidado, se procede de la forma mostrada.

# Otro ejemplo:

# In[4]:


asig = {'asignatura': 'Fundamentos de Programación', 'creditos': 6, 'tipos': ['teoría', 'prácticas']} 

print(asig['tipos'][0])


# En este caso, se accede al primer elemento de la lista que aparece como dato accesible a través de la clave `tipos`.

# ***
# <a id='Diccionarios_vs_listas'></a>

# ## Diccionarios versus listas
# 
# Tanto los **diccionarios** como las **listas** son colecciones **iterables** y **mutables**. 
#  - **Iterables**: los elementos que las componen pueden ser accedidos de *uno en uno* utilizando construcciones como el `for`.
#  - **Mutables**: los elementos pueden ser modificados, las colecciones pueden ser borradas, extendidas, etc.
# 
# Las **listas** son colecciones **secuenciales** que establecen una relación de orden entre los elementos contenidos. Los **diccionarios** son **no secuenciales**: no tiene ningún sentido decir que un elemento cualquiera de un diccionario *va primero* que otro. El hecho de ser **no secuenciales**, por ejemplo, implica que en los diccionarios no se puedan utilizar los **cortes** (**slices**), como sí ocurre con las listas.
# 
# Todo lo que puede ser realizado con **diccionarios** puede ser llevado a cabo con **listas**. Habrá un conjunto de tareas en los que resultará más conveniente, por ser más intuitivo o más eficiente, el utilizar **diccionarios**.
# 
# Veamos un ejemplo resuelto de ambas formas. Se trata de programar un glosario reducido de términos de programación en Python.

# In[5]:


conceptos = ['hashable', 'inmutable', 'interactivo', 'interpretado', 'iterable']
definiciones = ['Si su valor "hash" nunca cambia. Pueden actuar como "clave de diccionarios".',
                'Objeto con valor fijo.',
                'Python posee un intérprete interactivo.',
                'Python es un lenguaje interpretado.',
                'Objeto capaz de devolver sus elementos, uno cada vez.']

str = input('Diga concepto a buscar:')

indice = conceptos.index(str)
definicion = definiciones[indice]

print(definicion)


# En el código anterior se implementa el glosario utilizando dos *listas*: en la primera se almacenarían los conceptos a definir (siguiendo un orden lexicográfico, aunque en este caso el orden podría ser arbitrario) y en la segunda lista aparecen las definiciones correspondientes: aquí el orden tiene que ser consecuente con el orden elegido para la primera lista, cualquiera que este sea.
# 
# La tarea es realizable utilizando **listas**, pero resulta más compacta e intuitiva si se utilizan los diccionarios de Python.

# In[ ]:


# Glosario de Python implementado con un diccionario

glosario = {'hashable': 'Si su valor "hash" nunca cambia. Pueden actuar como "clave de diccionarios".',
            'inmutable': 'Objeto con valor fijo.',
            'interactivo': 'Python posee un intérprete interactivo.',
            'interpretado': 'Python es un lenguaje interpretado.',
            'iterable': 'Objeto capaz de devolver sus miembros, uno cada vez.'}

str = input('Diga concepto a buscar: ')
definicion = glosario[str]
print(definicion)


# La diferencia entre las dos implementaciones previas (con listas y con diccionarios) sugiere que para esta aplicación particular, la solución basada en diccionarios es preferible.
# 
# - Con los diccionarios se necesita *mantener* una única colección en memoria y no dos listas, que deberán estar necesariamente *coordinadas*, con lo que esto supone de una mayor susceptibilidad a errores.
# - A la hora de acceder a la *definición* de un concepto, la clave, simplemente se utiliza directamente el mismo. En el caso de las dos listas, explícitamente hay que encontrar el índice que se corresponde con el concepto en la primera lista, para después acceder a la segunda utilizando el dicho índice.

# Se puede considerar al **diccionario** como una generalización de las **listas**. O a la inversa, una **lista** sería una especie de **diccionario** especializado que no tiene clave porque esa función sería realizada por el **índice**: los enteros en el intervalo `[0, N-1]` donde `N` es el número de elementos almacenados.
# 
# Debido a este hecho, la **lista** establece implícitamente una relación de orden entre los elementos.
# En el **diccionario**, al identificar individualmente a cada uno de los elementos por una clave explícita, dicho orden ya no tiene sentido.

# ### Elementos que pueden actuar como *claves* en diccionarios
# 
# Como se ha visto, las **claves** de los **diccionarios** pueden estar creadas usando diferentes tipos, no sólo por **cadenas de caracteres**.
# 
# No todos los valores pueden ser *claves*. Solo lo pueden ser aquellos valores que sean **inmutables**:
# - caracteres
# - cadenas de caracteres
# - enteros, booleanos y reales
# - tuplas
# 
# No pueden actuar como *claves* ni las listas ni los propios diccionarios.

# ***
# <a id='Operacciones_con_diccionarios'></a>

# ## Operaciones con diccionarios
# 
# Entre las operaciones a realizar con diccionarios se tienen:
# 
# - **Crear los diccionarios**: utilizando una de varias alternativas.
# - **Copiar diccionarios**: copiar diccionarios: alias, copia superficial y copia profunda.
# - **Acceder a datos**: obtener el dato asociado a una *clave* dada.
# - **Modificar datos**: se pueden modificar los datos asociados a una *clave*.
# - **Extender**: añadir nuevos datos (con sus *claves* asociadas)
# - **Borrar datos**: borrar un elemento.
# 
# Otras operaciones básicas incluyen:
# 
# - **Obtener tamaño**: interrogar sobre la longitud de la estructura de datos, con la función nativa `len()`.
# - **Recorrer diccionario**: utilizar bucles considerando al **diccionario** como un **iterable**.

# Los **diccionarios** (al igual que las **listas**) son estructuras de datos **mutables**. Esto quiere decir que se pueden modificar: cambiar el dato asociado a una *clave*, borrarlo, extender el diccionario con nuevos elementos, etc.
# 
# Véase el siguiente ejemplo, donde se parte de un diccionario vacío, para crearlo paso a paso.
# 
# Para actualizar el dato de un elemento en un diccionario basta con asignar un valor al elemento en cuestión, accediendo a él mediante la clave.
# 
# Si el elemento existe, se modifica. Si no existe, se crea uno nuevo: el diccionario se expande dinámicamente.

# In[ ]:


mediciones = {}
mediciones['temperatura'] = 30
mediciones['pres'] = 1.2
mediciones['nivel'] = 50
mediciones['valv'] = 'abierta'
print(mediciones)


# ### La función `dict()`
# También es posible utilizar la función ```dict()```, con diversos argumentos, para crear diccionarios de forma flexible.
# 
# ```python
#     dic_arg    = dict(clave_1 = dato1, clave_2 = dato2, ...)    # Como conjunto variable de argumentos con nombre
#     dic_tuplas = dict([(clave_1, dato1), (clave_2, dato2)])     # Como una lista de tuplas
#     dic_listas = dict(zip([clave_1, clave_2], [dato1, dato2]))  # Uniendo dos listas con función zip
# ```

# In[7]:


digitos = dict(uno=1, dos=2)
romanos = dict([(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')])
por_dos = dict(zip([1, 2, 3], [2, 4, 6]))

print(digitos, romanos, por_dos)


# ### Copiar diccionarios
# 
# Los diccionarios son colecciones mutables, al igual que las listas. Debido a ello, es importante ser consciente acerca de qué es lo que ocurre cuando se intenta *copiar* un diccionario a otro.
# 
# #### Alias
# 
# Las asignaciones del tipo ```dic2 = dic1``` simplemente crean un *alias*: otorgan otro nombre, `dic2`, a un diccionario también llamado `dic1`. Evidentemente, las modificaciones hechas a los datos subyacentes mediante un alias, serán accesibles cuando se acceda a través del otro.
# 
# #### Copia superficial (shallow copy)
# 
# Hace una copia de los pares (clave: dato) de un diccionario a otro. No realiza copia de otras estructuras (listas, otros diccionarios) anidadas.
# ```python
# dic2_copia = dict(dic1)    # Utilizando la función dict()
# dic3_copia = dic1.copy()   # Utilizando el método .copy() del diccionario fuente.
# ```

# In[ ]:


dic1 = {1: 2, 3: 4}
dic2 = dict(dic1)   
dic3 = dic1.copy()

print(id(dic1), id(dic2), id(dic3))
dic1[1] = 100
print(dic1)
print(dic2)
print(dic3)


# #### Copia profunda (deep copy)
# Hace copia separadas de diccionarios con independencia del grado de anidamiento que presenten.

# In[ ]:


import copy

dir1 = {'Apt': 2, 'id': {'iq1': 1, 'iq2': 2}}
dir2 = copy.deepcopy(dir1)  # Copia profunda
dir3 = dir1.copy()  # Copia superficial
dir1['id']['iq1'] = 1000

print(dir1)
print('La copia profunda no sufre alteración con el cambio en dict1:', dir2)
print('La copia superficial se ve afectada con el cambio en dict1:', dir3)


# ### Acceder a los elementos de forma segura
# 
# Probablemente haya observado que, si se intenta acceder mediante la *clave* a un objeto que no se encuentra en el **diccionario**, se produce un error en tiempo de ejecución. Para evitar este tipo de errores se puede *interrogar* al diccionario por la existencia de la *clave*. Esto se puede realizar utilizando una estructura condicional y el operador `in`, que devuelve `True` si la clave indicada existe en el **diccionario** y `False` en caso contrario.

# In[ ]:


if 'temperatura' in mediciones:
    print(mediciones['temperatura'])
else:
    print('Probablemente deba ejecutar la celda previa')


# ### Borrar elementos
# Igual que para las listas, se utiliza la función nativa `del()`.
# 
# ```python
# del mediciones['valv']
# ```
# Pero también es posible utilizar el *método* `.pop()` del diccionario, para simultáneamente acceder al elemento señalado y borrarlo.
# 
# ```python
# valor_temp = mediciones.pop('temperatura')
# ```

# In[ ]:


mediciones = {}
mediciones['temperatura'] = 30
mediciones['pres'] = 1.2
mediciones['nivel'] = 50
mediciones['valv'] = 'abierta'

valor = mediciones.pop('pres')
print(valor)
print(mediciones)


# El método `.clear()` borra todos los elementos de un diccionario, dejándolo vacío.

# ### Tamaño del diccionario
# 
# La función `len()` está *sobrecargada* para trabajar también con diccionarios.
# 
# ```python
# print(len(mediciones))
# ```

# ### Uniendo diccionarios
# 
# Una posibilidad interesante es la de unir dos diccionarios en uno. La sintaxis es:
# 
# ```python
# dicionario1.update(dicionario2)
# ```
# El método `.update()` del `diccionario1` recibe otro diccionario, `diccionario2` a modo de *actualización*.
# 
# El resultado es el siguiente:
# - Se añaden al **diccionario** actualizado todos los elementos del otro diccionario. 
# - Si alguna clave coincide, el resultado final será el del elemento del segundo diccionario.

# In[ ]:


dic1 = {'a': 10, 'b': 1}
dic2 = {'a': 3, 'c': 0}

dic1.update(dic2)

print(dic1)


# ***
# <a id='El_diccionario_como_iterable'></a>

# ## El diccionario como iterable
# El uso de los diccionarios en programación, requiere frecuentemente de la posibilidad de recorrerlos, accediendo a cada uno de los elementos almacenados. 

# In[ ]:


asig = {'asignatura': 'Fundamentos de Programación', 'creditos': 6, 'tipos': ['teoría', 'prácticas']} 

for clave in asig:
    print(asig[clave])


# El anterior bucle es equivalente al siguiente:
# 
# ```python
# for clave in asig.keys():
#     print(asig[clave])
# ```
# El método `.keys()` del **diccionario** devuelve un objeto iterable consistente en las claves del mismo, con lo cual su uso en este contexto es redundante.
# 
# Pero también es posible recorrer directamente los datos, obviando su relación con sus claves, utilizando el método `.values()`, como se ejemplifica a continuación.

# In[ ]:


for valor in asig.values():
    print(valor)


# Existe todavía otra manera de recorrer el diccionario y es la ejemplificada en el siguiente código:

# In[ ]:


for clave, valor in asig.items():
    print(clave, valor)


# Utiliza el método `.items()` que devuelve una **tupla** conteniendo la clave y el dato asociado.

# ***
# <a id='Ejemplos'></a>

# ## Ejemplos
# 
# #### Contar las veces que aparece cada letra (y otros signos de puntuación) en una cadena de caracteres. 
# 
# - Crear un diccionario vacío
# - Iterar por cada una de las letras de la cadena:
#     - Si la letra no existe como _clave_ en el diccionario:
#         - Agregar la _clave_ asignándole como valor al elemento un cero
#     - Si ya existe
#         - Incrementar en uno el entero asociado a la letra

# In[ ]:


texto = '''Este es un texto del que se van a extraer letras para analizar la frecuencia de las mismas.
La cadena tiene varias lineas, por eso utilizan 3 comillas. También tiene digitos y signos'''

letras_frec = {}

for letra in texto:
    if letra not in letras_frec:
        letras_frec[letra] = 1
    else:
        letras_frec[letra] += 1
    
print(letras_frec)


# El código anterior es perfectamente válido y resulta muy claro.
# 
# En la medida en que conozcamos más en profundidad las diversas posibilidades que ofrece Python, podemos utilizarlas en nuestro beneficio.
# 
# Por ejemplo, los diccionarios tienen el método `.get(clave, valor)` , que sirve el propósito de devolver:
# * el valor asociado a la `clave` que se pasa como primer parámetro, si esta existe, 
# * o el `valor` de un segundo parámetro opcional, si no se encuentra. 
# 
# Pues bien, el uso de este método simplifica el código previo de la siguiente forma.

# In[ ]:


letras_frec = {}

for letra in texto:
    letras_frec[letra] = letras_frec.get(letra, 0) + 1
    
print(letras_frec)


# #### Matrices dispersas  (sparse)
# 
# Existen muchas aplicaciones con matrices donde estas se caracterizan por tener la gran mayoría de sus elementos con valor cero, y sólo unos pocos con valores significativos. En estas aplicaciones, resulta más eficiente representar la matriz por un método alternativo, que consiste en representar solo los valores diferentes de cero, especificando la fila y la columna donde esos valores están situados. Las matrices susceptibles de ser representadas de esta forma son conocidas como matrices **dispersas** (**sparse**). 
# 
# En el siguiente código se describe una función que recibe una matriz representada de la forma convencional (como una lista anidada de filas). Posteriormente, la convierte al formato de *matriz dispersa* utilizando un diccionario, en el que la clave está formada por una *tupla* que contiene la fila y columna del elemento a representar.
# 
# Un ejercicio interesante es realizar otras funciones para definir una aritmética de matrices dispersas (suma, producto, etc.)

# In[ ]:


# Recibe matriz definida como lista anidada y devuelve matriz dispersa con diccionario
def convierte_dispersa(mat):
    mat_sparse = {}
    for fil, col in enumerate(mat):
        for col, elem in enumerate(mat[fil]):
            if elem != 0:
                mat_sparse[(fil, col)] = elem
    return mat_sparse


# Programa principal
mat = [[0, 0, 0, 1],
       [0, 1, 0, 0],
       [0, 0, 0, 1],
       [1.2, 0, 0, 0]]

mat_eficiente = convierte_dispersa(mat)

print(mat_eficiente)

