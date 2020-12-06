#!/usr/bin/env python
# coding: utf-8

# # Control de flujo iterativo
# **Autores**: Rogelio Mazaeda Echevarría, Félix Miguel Trespaderne.   

# ## Contenidos
# [Introducción](#Introducción)<br>
# [Bucle `while`](#Bucle_while)<br>
# [Bucle `for`](#Bucle_for)<br>
# [Iterables](#Iterables)<br>
# [Sentencia `break`: salida temprana de un bucle](#Sentencia_break:_salida_temprana_de_un_bucle)<br>
# [Sentencia `continue`](#Sentencia_continue)<br>
# [Bucles anidados](#Bucles_anidados)

# ***
# <a id='Introducción'></a>

# ## Introducción
# 
# La otra estructura de **control de flujo** fundamental que nos falta es la **estructura iterativa**, conocida también por el nombre de **bucle**. 
# 
# El **control de flujo iterativo** permite resolver cómodamente una situación frecuente a la hora de resolver un problema, en la que es necesario ejecutar un conjunto de sentencias una y otra vez:
# * **mientras** determinada condición lógica se cumpla o,
# * un **número determinado** de veces.

# ***
# <a id='Bucle_while'></a>

# ## Bucle `while`
# Veamos un ejemplo que mejora el código previo de introducción de un mes válido. Ahora, repregunta al usuario (cuantas veces sea necesario) en el caso de que se equivoque al introducir un mes inválido:

# In[1]:


# Un bucle para garantizar que el mes introducido es correcto

mes = int(input("Introduzca el mes del año (entre 1 y 12): "))

while mes > 12 or mes < 1:
    print("Mes introducido incorrecto. Inténtelo de nuevo")
    mes = int(input("Introduzca el mes del año (entre 1 y 12):"))

print("El mes {} es válido".format(mes))


# Observe en el fragmento anterior la sintaxis en Python del bucle `while`:
# * Por un lado, la palabra reservada que lo identifica más la **condición lógica** y el **delimitador** `:`
# * Por el otro lado, el **cuerpo** de sentencias, que deben aparecer adecuadamente sangradas
# 
# Si la expresión se evalúa como `True`, se ejecuta el bloque de sentencias *regresando* de nuevo a la sentencia `while`. Así de forma iterada hasta que la **expresión de control** asociada al `while` se evalúe como `False`. 

# Se debe comprender que si la condición de control del bucle se evalúa inicialmente como `False`, las sentencias afectadas por el bucle no serán ejecutadas ni siquiera una vez. Por tanto, en el momento en que se realiza la programación, el número de veces que se repite un bucle `while` ¡no puede saberse de antemano!
# 
# Así, en el ejemplo anterior puede ocurrir: 
# * que no se ejecute el cuerpo del `while` ninguna vez, si el usuario introduce un mes correcto desde el inicio
# * que se ejecute un número arbitrariamente alto, que dependerá de la mucha o poca *habilidad* del usuario en seguir correctamente las instrucciones que se le dan

# El alumno observador puede constatar la repetición en el código de la línea:
# ```Python
# mes = int(input("Introduzca el mes del año (entre 1 y 12):"))
# ```
# Una forma alternativa de programar el ejemplo anterior es la siguiente:

# In[ ]:


# Un bucle para garantizar que el mes introducido es correcto. Versión alternativa.

mes = 0 # Inicializamos la variable con un valor que 
        # hace que se evalúe a True la condición de control

while mes > 12 or mes < 1:
    mes = int(input("Introduzca el mes del año (entre 1 y 12):"))
    if mes > 12 or mes < 1:
        print("Mes introducido incorrecto. Inténtelo de nuevo")

print("El mes {} es válido".format(mes))


# Aunque para este ejemplo la ventaja en legibilidad es discutible, cuando el cuerpo del bucle `while` tiene varias sentencias repetidas antes del propio bucle, entonces suele ser ventajosa la segunda alternativa. 

# ### Bucle **controlado** por un **contador**
# El anterior es un ejemplo de un bucle **controlado** por una **condición lógica** de carácter general. En muchas ocasiones, la condición de salida del bucle viene determinada por un **contador**. 
# 
# **Nota**:En los depuradores de los sistemas de desarrollo y en herramientas como [pythontutor](http://www.pythontutor.com/visualize.html#mode=edit) se puede analizar la evolución paso a paso de los programas.

# In[ ]:


# Bucle controlado por un contador que suma un determinado conjunto de reales. (Versión 1)

contador = int(input("Diga cuantos números reales quiere sumar: "))

suma = 0.0
while contador > 0:
    valor = float(input("Deme valor real a sumar: "))
    suma += valor                                       # Equivalente a suma = suma + valor
    contador = contador - 1                             # Se podría usar: contador -= 1

print("La suma de los números introducidos es", suma)


# En el código anterior se debe notar:
# - Antes de entrar al bucle, ya se conoce el número de veces que éste se va a repetir.
# - Si la expresión de control es `False` ni siquiera se entra al bucle la primera vez.

# ### El acumulador
# Por otra parte, el ejemplo implementa una de las ideas básicas de mayor utilidad en programación: el concepto de **acumulador**. Se quiere realizar una operación (la suma) que involucra un conjunto (no determinado en el momento de la programación) de operandos. La idea consiste en dedicar una variable (`suma`) para contener los resultados parciales de dicha operación. 
# 
# Dicha variable **acumulador** ha de ser **inicializada** antes de entrar al bucle a un valor que sea **neutro** respecto a la operación seleccionada (el `0` en caso de la suma). Ya dentro del bucle, la variable acumulador es actualizada en cada iteración.

# Podríamos haber programado el ejemplo anterior de otra forma, igualmente válida y legible, en la que no *perdemos* el valor inicial de cuantos números queremos sumar. Además, resulta fácil distinguir el caso en el cual no se introdujeron números.

# In[ ]:


# Bucle controlado por un contador que suma un determinado conjunto de reales. (Versión 2)

num_valores = int(input("Diga cuantos números reales quiere sumar: "))

suma = 0.0
contador = 0
while (contador < num_valores):
    valor = float(input("Deme el valor real {:d} a sumar: ".format(contador)))
    suma += valor
    contador += 1

if num_valores > 0:
    print("La suma de los {:d} números introducidos es {:f}".format(num_valores, suma))
else:
    print("El usuario no introdujo ningún valor.")


# ***
# <a id='Bucle_for'></a>

# ## Bucle `for`
# 
# Para el caso, muy común, de los bucles controlados por contador, Python tiene el bucle `for` que resulta especialmente adaptado. 
# 
# Véase el ejemplo siguiente, que muestra el producto de los enteros incluidos en determinado **rango**:

# In[ ]:


# Determina producto de enteros en rango

inf = int(input("Diga límite inferior del rango: "))
sup = int(input("Diga límite superior del rango: "))

producto = 1
for elem in range(inf, sup+1):
    producto *= elem                             # Se podría usar: producto = producto*elem

print("El producto de los enteros en el rango [{},{}] es {}".format(inf, sup, producto))


# El bucle `for ... in ...` en Python utiliza en este ejemplo la función nativa `range()`.
# 
# Así, el bucle `for` del ejemplo asigna de forma iterada y ordenada cada uno de los enteros del rango de que se trate a la variable que actúa como **contador** del bucle, `elem`. En cada una de las iteraciones ejecuta las sentencias contenidas en el cuerpo del bucle.
# 
# En el anterior ejemplo se tiene una nueva implementación de la idea del **acumulador**, en este caso representada por la variable `producto` en la que se *acumula* precisamente el resultado de la multiplicación de los enteros en el rango. En consonancia con su propósito, en este caso el acumulador es inicializado a 1, que es el valor **neutro** para la operación de multiplicación.

# La sentencia `for` de Python tiene una sintaxis que presenta diferencias notables con respecto a la que se utiliza en C/C++ y en otros lenguajes de programación:
# 
# ```python
# for (int elem = inf; elem <= sup; elem = elem + 1)
# {
#     producto *= elem;
# }
# ```
# El `for` de C/C++ describe de manera más explícita el proceso de inicialización del contador, la expresión lógica de control que evalúa la permanencia o no en el bucle, y el incremento (o en general modificación) del contador en cada iteración.

# Ahora tenemos una nueva alternativa más compacta para realizar la suma de un determinado conjunto de números reales.

# In[ ]:


# Bucle que suma un determinado conjunto de reales. Versión con for. (Versión 3)

num_valores = int(input("Diga cuantos números reales quiere sumar: "))

suma = 0.0
for i in range(num_valores):
    valor = float(input("Deme el valor real {:d} a sumar: ".format(i)))
    suma += valor

if num_valores > 0:
    print("La suma de los {:d} números introducidos es {:f}".format(num_valores, suma))
else:
    print("El usuario no introdujo ningún valor.")


# ***
# <a id='Iterables'></a>

# ## Iterables
# La función `range()` devuelve un objeto **iterable**, objetos capaces de ir generando ordenadamente uno por uno la secuencia de elementos que lo componen. Las **listas**, `list` y las **cadenas de caracteres**, `str`, también son objetos iterables.
# Cualquier objeto iterable es susceptible de ser recorrido por un bucle for.

# In[ ]:


# Crea una lista con los valores impares de una lista de enteros
lista = [1, 3, 2, 7, 5, 4, 6]
impares = []
for x in lista:
    if x % 2:
        impares.append(x)
print(impares)


# In[ ]:


# Sustituye los caracteres en blanco de una cadena por el caracter '_'
cadena = 'Hola amigos'
nueva_cadena = ''
for c in cadena:
    if c == ' ':
        nueva_cadena += '_'
    else:
        nueva_cadena += c
print(nueva_cadena)


# En la siguiente versión del ejemplo sobre el que venimos trabajando, primero creamos una lista con los valores introducidos por teclado. Luego realizamos la suma de sus elementos.

# In[ ]:


# Bucle que suma un determinado conjunto de reales. Versión con lista y for. (Versión 4)

num_valores = int(input("Diga cuantos números reales quiere sumar: "))
lista = []
for i in range(num_valores):
    lista.append(float(input("Deme el valor real {:d} a sumar: ".format(i))))
    
suma = 0.0
for x in lista:
    suma += x

if num_valores > 0:
    print("La suma de los {:d} números introducidos es {:f}".format(num_valores, suma))
else:
    print("El usuario no introdujo ningún valor.")


# Otra posibilidad más eficiente hubiese sido crear inicialmente una lista del tamaño final y luego ir actualizando los valores.

# In[ ]:


# Bucle que suma un determinado conjunto de reales. Versión con lista y for. (Versión 5)

num_valores = int(input("Diga cuantos números reales quiere sumar: "))
lista = [0]*num_valores
for i in range(num_valores):
    lista[i]=float(input("Deme el valor real {:d} a sumar: ".format(i)))
    
suma = 0.0
for x in lista:
    suma += x

if num_valores > 0:
    print("La suma de los {:d} números introducidos es {:f}".format(num_valores, suma))
else:
    print("El usuario no introdujo ningún valor.")


# ### `enumerate()`
# En ocasiones, además del valor del ítem, necesitamos saber su posición, su índice dentro del objeto iterable. Una posibilidad para resolver el problema es ayudarnos de las funciones `len()` y `range()`.

# In[ ]:


# Crea una lista con los valores impares de una lista de enteros
lista = [1, 3, 2, 7, 5, 4, 6]
impares = []
posiciones = []
for i in range(len(lista)):
    if lista[i] % 2:
        impares.append(lista[i])
        posiciones.append(i)

print("La lista con los impares es {} y sus posiciones son {}.".format(impares, posiciones))


# Sin embargo, para estos casos Python proporciona la función nativa `enumerate()`. Esta función va generando junto con un `for` la secuencia de **tuplas** formada por el índice y el ítem.

# In[ ]:


# Crea una lista con los valores impares de una lista de enteros
lista = [1, 3, 2, 7, 5, 4, 6]
impares = []
posiciones = []
for i, x in enumerate(lista): # i, x es la tupla desempaquetada
    if x % 2:
        impares.append(x)
        posiciones.append(i)

print("La lista con los impares es {} y sus posiciones son {}.".format(impares, posiciones))


# ### `zip()`
# Otra función nativa muy utilizada asociada a los bucles `for` es `zip()`. Con ella, podemos recorrer simultáneamente dos o más objetos iterables. Así, por ejemplo, la función `zip(lista_1, lista_2, ..., lista_n)` va generando junto con un `for` una secuencia formada por las tuplas `(lista_1[0], lista_2[0], ..., lista_n[0])`, `(lista_1[1], lista_2[1], ..., lista_n[1])`, etc. El bucle `for` termina cuando se alcanza el elemento de la lista de menor longitud.
# 
# Al igual que con `range()` y `enumerate()`, mediante la función `list()` podemos transformar la salida de `zip()`en una lista.

# In[1]:


lista_1 = [1, 2, 3, 4]
lista_2 = ['a', 'b', 'c' , 'd']
lista_3 = [3.2, 6.7, 9.8, 3.2]

lista = list(zip(lista_1, lista_2, lista_3))
print(lista)

for x, y, z in zip(lista_1, lista_2, lista_3):
    print(x, y, z)


# ***
# <a id='Sentencia_break:_salida_temprana_de_un_bucle'></a>

# ## Sentencia `break`: salida temprana de un bucle
# 
# En muchas ocasiones resulta conveniente salir de un bucle, no mediante la evaluación a `False` de la expresión de control, sino desde dentro del bucle utilizando un `if` junto con la sentencia `break` de **salto incondicional**.
# 
# En el siguiente código se muestra un ejemplo típico. Se trata de determinar si un determinado número entero es primo o no.

# In[1]:


# Determina si un número entero es primo. (Versión 1)

numero = int(input('Deme un entero positivo mayor que 1: '))

es_primo = True  # Variable centinela o bandera
for div in range(2, numero):
    if numero % div == 0:
        es_primo = False
        break

if es_primo:
    print("El número {} es primo".format(numero))
else:
    print("El número {} no es primo".format(numero))


# Una advertencia: existen formas más eficientes de realizar la tarea propuesta; el código anterior debe verse como un intento inicial. 
# 
# Se trata básicamente de aplicar la propia definición de número primo: *aquel que es divisible sólo por él y por la unidad*. 
# 
# La estrategia entonces consiste en hallar, mediante un bucle, todos los posibles divisores *legítimos* que harían que se pudiera decidir que el número no es primo. Se utiliza un bucle `for` **por rango**, y el rango elegido es $[2,numero)$. Obsérvese que el límite inferior está incluido en el rango y el superior no. Y esto es precisamente lo que se requiere. 

# Se debe notar que el bucle necesario tiene una especie de *carácter asimétrico*:
# * por una parte, para concluir que el número es primo, se debe llevar el bucle hasta su conclusión, investigando todos los posibles divisores, sin hallar ningún divisor exacto.
# * por el contrario, para concluir que el número no es primo, basta con encontrar el primer divisor exacto.
# 
# En sintonía con esta _asimetría_ del problema, se utiliza una construcción en la cual al bucle `for` **por rango** se le asocia una variable **centinela**, **testigo** o **bandera**, `es_primo`. Si en el transcurso de las iteraciones se detectara, mediante un condicional `if`, que el número investigado es divisible por alguno de los divisores posibles, se sale inmediatamente del bucle, utilizando la sentencia `break` y _activando_ la bandera.
# 
# Ya fuera del bucle, se interroga el valor del **centinela** para informar al usuario sobre el resultado encontrado. 

# Las variables **testigo** son inicializadas a un valor conocido antes de entrar a una zona del código y luego tomarán diferentes valores en dependencia de las sentencias que sean ejecutadas o no. De esta manera, cuando su valor sea interrogado al final, indicarán el *camino* concreto que siguió el programa, permitiendo sacar las oportunas conclusiones. 
# 
# Se debe comprender que la salida anticipada de un bucle constituye un recurso que puede mejorar la escritura o legibilidad del código. No obstante, siempre se puede modificar el bucle de manera que sólo se pueda decidir la permanencia o salida del mismo a partir de la expresión de control. 
# 
# En el ejemplo que nos ocupa:

# In[ ]:


# Determina si un número entero es primo. Versión sin salida incondicional break. (Versión 2)

numero = int(input('Deme un entero positivo mayor que 1: '))

es_primo = True
div = 2
while div < numero and es_primo:
    if numero % div == 0:
        es_primo = False
    div += 1

if es_primo:
    print("El número {} es primo".format(numero))
else:
    print("El número {} no es primo".format(numero))


# La modificación ha supuesto cambiar el `for` por un `while`. Observe la implementación *manual* del contador `div` que actúa como divisor y que debe ser inicializado fuera del bucle. Véase que la expresión de control incluye la condición de que no se haya detectado todavía un divisor para continuar iterando. 

# Una versión más compacta se logra si nos damos cuenta que el propio contador `div` puede actuar como variable testigo. Si `div == numero` tras el bucle es que hemos recorrido todo el rango de valores sin encontrar un divisor. 
# 
# Así:

# In[ ]:


# Determina si un número entero es primo. Versión usando while y el contador como testigo. (Versión 3)

numero = int(input('Deme un entero positivo mayor que 1: '))

div = 2
while numero % div != 0:
    div += 1

if div == numero:
    print("El número {} es primo".format(numero))
else:
    print("El número {} no es primo".format(numero))


# Y en su versión con bucle `for` **por rango**:

# In[ ]:


# Determina si un número entero es primo. Versión usando for y el contador como testigo. (Versión 4)

numero = int(input('Deme un entero positivo mayor que 1: '))

for div in range(2, numero+1):
    if numero % div == 0:
        break

if div == numero:
    print("El número {} es primo".format(numero))
else:
    print("El número {} no es primo".format(numero))


# Decidir cuál de las implementaciones es superior es cuestión de debate. Más allá de optar entre las versiones `for` **por rango** o `while`, a nuestro juicio, el uso explícito de la variable centinela `es_primo` genera un código más legible aunque menos eficiente.

# ***
# <a id='Sentencia_continue'></a>

# ## Sentencia `continue`
# 
# De forma similar al `break`, la sentencia `continue` representa un _salto incondicional_ que se asocia a la ejecución de los bucles. La sentencia `continue` a diferencia del `break` no abandona el bucle, sino que cuando es ejecutada provoca un _salto_ inmediato al inicio del bucle, para procesar la siguiente iteración.

# In[ ]:


# Ejemplo de uso de la sentencia continue

for i in range(21):
    if i%3 == 0:
        continue
    print(i)


# Aunque la sentencia `continue` es menos utilizada que `break`, y al igual que esta última puede ser sustituida por construcciones `if: ...elif ...else:`, en algunas circunstancias ofrece una solución más estructurada y comprensible.

# ***
# <a id='Bucles_anidados'></a>

# ## Bucles anidados
# 
# Con cierta frecuencia la solución de un problema exige el uso de bucles que estén contenidos dentro de otros. Los bucles anidados pueden tener tantos niveles como se quiera. 
# 
# La idea clave es: en cada iteración de un bucle externo, ocurren todas las iteraciones posibles de los bucles internos.
# 
# El siguiente ejemplo es ilustrativo de este proceso. En este caso, se tienen dos bucles anidados implementados mediante `for`. 

# In[1]:


for i in range(1, 11):
    for j in range(1, 11):
        print("{:4d}".format(i*j), end=' ')
    print()


# El bucle externo recorre todos los enteros en el intervalo $[1,10]$ y utiliza un índice o contador `i` y el interno recorre el mismo rango pero asignando los valores del mismo a la variable de control del bucle `j`. De manera que, en la primera iteración del bucle externo, cuando `i` tiene el valor `1`, el bucle interno *agota* todas las posibles iteraciones, con `j` *barriendo* todos los valores del rango $[1,10]$.
# 
# Dentro del bucle interno se saca por pantalla, utilizando un formato útil para alinear correctamente las columnas de una tabla, el producto de ambos contadores. Observe que en esta función `print()`, el caracter a imprimir al final (normalmente el cambio de línea), es sustituido por una cadena de caracteres que representa un espacio en blanco, `end=' '`. 

# El sangrado existente en el segundo `print()` informa al intérprete de Python que este debe ser ejecutado, como parte del bucle externo, cada vez que el interno termina su ejecución. Su propósito es simplemente sacar por pantalla un cambio de línea. 
# 
# El objetivo final logrado es la salida por la consola de la tabla de multiplicar. El ejemplo utilizado en este caso puede resultar trivial, pero el concepto ilustrado tiene muchas otras aplicaciones.
