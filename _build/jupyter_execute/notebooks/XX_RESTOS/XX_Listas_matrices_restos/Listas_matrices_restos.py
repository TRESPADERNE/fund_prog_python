#!/usr/bin/env python
# coding: utf-8

# # Listas: matrices restos
# **Autores**: Rogelio Mazaeda Echevarría, Félix Miguel Trespaderne.   

# ## Matrices matemáticas utilizando lista anidadas
# Las matrices son uno de los conceptos matemáticos más importantes. Aunque hay módulos, como **Numpy** que permiten trabajar con matrices de forma eficiente Una forma de implementarlas en Python es utilzar listas, y en particular listas anidadas, como en el ejemplo que sigue:
# 
# ```python
# mat = [[a11, a12, ..., a1n],[a21, a22, ..., a2n],..., [am1, am2, ..., amn]]
# ```
# 
# El anterior código podría interpretarse como la creación de una matriz de **nxm**: ```n``` columnas y ```m``` filas. Nótese que otra manera de verla, sería como una lista de **m** sublistas (filas) cada una de las cuales tiene __n__ elementos (columnas).
# 
# En el código que sigue se utiliza esta representación para realizar la suma (matemática) de dos matrices de enteros.

# In[1]:


a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
b = [[1, 1, 1, 1], [2 ,2 ,2, 2], [3, 3, 3, 3]]

#Inicializamos matriz suma 
mat_suma=[]

#Recorremos la matriz con un doble bucle anidado, sumando elementos correspondientes
for i in range(len(a)):
    fila = []
    for j in range(len(a[i])):
        suma= a[i][j]+b[i][j]
        fila.append(suma)
    mat_suma.append(fila)

#Sacamos por pantalla la lista anidada en forma de matriz matemática
for fila in mat_suma:
    for elem in fila:
        print ('{:5d}'.format(elem), end = " ")
    print()


# En el codigo anterior se utiliza un doble bucle anidado para recorrer las filas y las columnas de las dos matrices de igual dimensión que actúan como sumandos.
# 
# Al inicio y fuera de ambos bucles, se inicializa la lista que actuará como matriz resultado de la suma.
# 
# En cada iteración del bucle externo, primero se inicializa una lista vacía (```fila```) que actuará precisamente como la fila actual de la matriz resultado. En el bucle interno se va actualizando la lista fila, añadiendo el elemento que toca como suma de los elementos correspondientes de los dos sumandos. 
# 
# Una vez creada la fila, se añade a la matriz suma también utilizando el método ```.append()```, pero en este caso de la matriz resultado.
# 
# El siguiente doble bucle anidado se encarga de sacar por pantalla el contenido de la lista resultante en forma de matriz matemática.

# El código anterior es correcto. Muchas veces, a la hora de recorrer listas (también en el caso de las listas anidadas) se utiliza una construcción como la que se muestra a continuación:
# 
# ```python
# for i in range(len(lista)):
#     # Hacer algo con los elementos
#     print(lista[i])
# ```
# Esta construcción es válida, pero un estilo mucho más en consonancia con las posibilidades y el estilo de Python, es acceder directamente al los elementos del iterable:
# 
# ```python
# for elem in lista:
#     # Hacer algo con los elementos
#     print(elem)
# ```
# 
# ¿Como resultaría el código anterior, utilizando esta última construcción? Se debe tomar como referencia el bucle del programa principal que muestra por pantalla la matriz.
# 
# Un posible resultado se muestra a continuación, utilizando también una función:

# In[2]:


# Función (no pura) para sacar matriz por pantalla
def muestra_matriz(a):
    for fila in a:
        for elem in fila:
            print ('{:5d}'.format(elem), end = " ")
        print()
    
# Función (pura) para sumar dos matrices 
def suma_mat(a,b): 
    mat_suma=[]
    for i,fila in enumerate(a):
        fila = []
        for j,elem in enumerate(fila):
            suma= elem+b[i][j]
            fila.append(suma)
        mat_suma.append(fila)
    return mat_suma

# Programa principal para probar las funciones previas

suma = suma_mat(a, b)
muestra_matriz(suma)


# En el código previo se utiliza el **for** de la manera correcta para recorrer el **iterable** que es la lista. Surge, sin embargo, la necesidad de obtener no sólo el elemento adecuado de la matriz ```a```, sino también el elemento correspondiente (en la misma fila y columna) de la matriz ```b```. Para ello resulta conveniente obtener adicionalmente el índice de las listas (```i``` para la fila y ```j``` para la columna) para utilizar la sintaxis de los corchetes (```b[i][j]```). Esto se puede lograr utilizando el **iterable** que devuelve **enumerate**.
# 
# Una alternativa al uso de **enumerate**, para este caso concreto, sería el uso de la función **zip()** que permite _unir_ dos listas, para obtener simultáneamente los elementos a sumar de ambas matrices.

# In[3]:


# Función (no pura) para sacar matriz por pantalla
def muestra_matriz(a):
    for row in a:
        for elem in row:
            print ('{:5d}'.format(elem), end = " ")
        print()
    
# Función (pura) para sumar dos matrices 
def suma_mat(a, b): 
    mat_suma=[]
    for fila_a, fila_b in zip(a, b):
        fila = []
        for elem_a, elem_b in zip(fila_a, fila_b):
            suma= elem_a + elem_b
            fila.append(suma)
        mat_suma.append(fila)
    return mat_suma

# Programa principal para probar las funciones previas

suma = suma_mat(a, b)
muestra_matriz(suma)


# ¿Qué sucede, en el código previo, si los argumentos que se pasan no son matrices, o no tiene las mismas dimensiones? ¿Cómo se podría modificar el código de las funciones previas de forma que se implemente el concepto **EAFP** utilizando excepciones?
