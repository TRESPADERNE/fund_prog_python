#!/usr/bin/env python
# coding: utf-8

# # Diccionarios. Resto. Eficiencia.
# **Autores**: Rogelio Mazaeda, Félix Miguel Trespaderne.   

# ## Contenidos
# [Eficiencia de los Diccionarios](#Eficiencia)

# ***
# <a id='Eficiencia'></a>

# ## Eficiencia de los diccionarios
# Los diccionarios constituyen una de las colecciones intrínsecas de Python más poderosas y flexibles. Muchos problemas se simplifican notablemente si se utilizan diccionarios. El propio lenguaje Pyhton utiliza los diccionarios en la definición de muchas otras estructuras internas.
# 
# Algunos programadores, sin embargo, son reticentes a la hora de utilizarlos, porque tienen dudas sobre su eficiencia. Pero estas preocupaciones no están justificadas: el mecanismo interno que Python utiliza para implementar los diccionarios, basado en conceptos clave de la informática como los **mapas asociativos** y **tablas hash**, hacen que el trabajo con **diccionarios** sea comparable, en términos de **eficiencia**, con las **listas**.

# ![lista_memoria.jpg](attachment:lista_memoria.jpg)

# La lista es almacenada en memoria, colocando las referencias a los datos almacenados, una a continuación de la otra. Cuando se necesita acceder a un elemento, se presenta (mediante la sintaxis de los corchetes (ej: `lista[4]`) el número entero que se interpreta como el _desplazamiento_ desde el inicio de la lista hasta la posición a acceder. El acceso a un elemento es prácticamente inmediato y **no depende del tamaño de la lista**. Observe que está disposición en memoria corresponde a la naturaleza **secuencial** de la lista: la posición del dato se determina a partir de la posición de ese elemento en la lista.
# 
# Observe además que, si bien el acceso al elemento, una vez que se conoce su índice es casi _inmediato_, la situación es muy diferente si se quiere **determinar** si un elemento está en la lista: en este caso, el proceso es más lento y dependede del tamaño de la lista, aunque si la lista estuviese ordenada, el acceso sería más rápido con una búsqueda binaria.

# ![dicc_memoria.jpg](attachment:dicc_memoria.jpg)

# El diccionario es una colección **no secuencial**. Este hecho también se refleja en la forma en que los datos son almacenados en la memoria del ordenador. Aquí también se tiene una tabla con las referencias a los datos almacenados, pero la forma de determinar dónde almacenar cada elemento es muy diferente.
# 
# Como no existe una relación de orden establecida, no se puede nunca decir que el elemento de _clave_ dada (por ejemplo 'cuatro') se encuentra antes o después de otra _clave_ cualquiera. 
# 
# ¿Cómo se determina entonces qué desplazamiento desde el inicio de la tabla es necesario para acceder, por ejemplo, al elemento `diccionario['cuatro']`?
# 
# Para ello se utiliza un tipo especial de algoritmo (_hash_) que tiene las siguientes características:
# - devuelve un valor, que siempre es el mismo, para cada posible _clave_ 
# - dos _claves_ diferentes pueden devolver el mismo valor _hash_
# - el algorimo es tal, que se trata de minimizar la ocurrencia de que dos _claves_ devuelvan igual número.
# 
# El valor _hash_ devuelto no puede ser utilizado directamente como índice para encontrar la posición en la tabla porque es, quizá, demasiado grande. Por este motivo ese número resulta _comprimido_ utilizando otra función que mantiene las características especiales del valor _hash_ pero que hace que ahora el resultado esté dentro de los límites `[0,N-1]` para una tabla en memoria de tamaño N.
# 
# ¿Qué se hace cuando dos o más _indices_ diferentes dan el mismo valor _hash_ y por tanto resultan en el mismo desplazamiento en la tabla?
# 
# Una alternativa posible a asoptar en este caso, es el que la celda en cuestión ahora haría refencia a un conjunto de elementos en memoria donde se alamcenan consecutivamente los elementos coincidentes del diccionario.
# 
# Veáse que con este esquema, el acceso a un elemento del diccionario es casi tan rápido como el acceso a un elemento de la lista pero mucho más flexible: el índice no está límitado a ser el desplazamiento desde el inicio de la tabla sino que es libre. Tengáse en cuenta en particular que este acceso es prácticamente independiente del tamaño del diccionario (si se obvian las escasas coincidencias de números _hash_ para diferentes índices).
