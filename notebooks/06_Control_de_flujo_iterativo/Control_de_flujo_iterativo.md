---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.7.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Control de flujo iterativo

+++

[Introducción](#Introducción)<br>
[Bucle `while`](#Bucle_while)<br>
[Bucle `for`](#Bucle_for)<br>
[Iterables](#Iterables)<br>
[Sentencia `break`: salida temprana de un bucle](#Sentencia_break:_salida_temprana_de_un_bucle)<br>
[Bucles anidados](#Bucles_anidados)<br>
[Listas por comprensión](#Listas_por_comprension)

+++

***
<a id='Introducción'></a>

+++

## Introducción

La otra estructura de **control de flujo** fundamental es la **estructura iterativa**, conocida también por el nombre de **bucle** (**loop**). 

El **control de flujo iterativo** permite resolver cómodamente una situación frecuente a la hora de resolver un problema, en la que es necesario ejecutar un conjunto de sentencias una y otra vez:
* **mientras** determinada condición lógica se cumpla o,
* un **número determinado** de veces.

+++

***
<a id='Bucle_while'></a>

+++

## Bucle `while`
Veamos un ejemplo que mejora el código previo de introducción de un mes válido. Ahora, repregunta al usuario, cuantas veces sea necesario, en el caso de que se equivoque al introducir un mes inválido:

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

# Un bucle para garantizar que el mes introducido es correcto

mes = int(input("Introduzca el mes del año (entre 1 y 12): "))

while mes > 12 or mes < 1:
    print("Mes introducido incorrecto. Inténtelo de nuevo")
    mes = int(input("Introduzca el mes del año (entre 1 y 12):"))

print("El mes {} es válido".format(mes))
```

Observe en el fragmento anterior la sintaxis en Python del bucle `while`:
* Por un lado, la palabra reservada que lo identifica más la **condición lógica** y el **delimitador** `:`
* Por el otro lado, el **cuerpo** de sentencias, que deben aparecer adecuadamente **sangradas**

Si la expresión se evalúa como `True`, se ejecuta el bloque de sentencias *regresando* de nuevo a la sentencia `while`. Así de forma iterada hasta que la **expresión de control** asociada al `while` se evalúe como `False`.

+++

Se debe comprender que si la condición de control del bucle se evalúa inicialmente como `False`, las sentencias afectadas por el bucle no serán ejecutadas ni siquiera una vez. Por tanto, en el momento en que se realiza la programación, el número de veces que se repite un bucle `while` ¡no puede saberse de antemano!

Así, en el ejemplo anterior puede ocurrir: 
* que no se ejecute el cuerpo del `while` ninguna vez, si el usuario introduce un mes correcto desde el inicio
* que se ejecute un número arbitrariamente alto, que dependerá de la mucha o poca *habilidad* del usuario en seguir correctamente las instrucciones que se le dan

+++

El alumno observador puede constatar la repetición en el código de la línea:
```Python
mes = int(input("Introduzca el mes del año (entre 1 y 12):"))
```
Una forma alternativa de programar el ejemplo anterior es la siguiente:

```{code-cell} ipython3
:tags: [remove-output, raises-exception]

# Un bucle para garantizar que el mes introducido es correcto. Versión alternativa.

mes = 0 # Inicializamos la variable con un valor que 
        # hace que se evalúe a True la condición de control

while mes > 12 or mes < 1:
    mes = int(input("Introduzca el mes del año (entre 1 y 12):"))
    if mes > 12 or mes < 1:
        print("Mes introducido incorrecto. Inténtelo de nuevo")

print("El mes {} es válido".format(mes))
```

Aunque para este ejemplo la ventaja en legibilidad es discutible, cuando el cuerpo del bucle `while` tiene varias sentencias repetidas antes del propio bucle, entonces suele ser ventajosa la segunda alternativa.

+++

### Bucle controlado por un contador
El anterior es un ejemplo de un bucle **controlado** por una **condición lógica** de carácter general. En muchas ocasiones, la condición de salida del bucle viene determinada por un **contador**.

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

# Bucle controlado por un contador que suma un determinado conjunto de reales. (Versión 1)

contador = int(input('Diga cuantos números reales quiere sumar: '))

suma = 0.0
while contador > 0:
    valor = float(input('Dame un valor real: '))
    suma += valor                                       # Equivalente a suma = suma + valor
    contador = contador - 1                             # Se podría usar: contador -= 1

print("La suma de los números introducidos es", suma)
```

Un ejemplo de ejecución es el siguiente:
```
Diga cuantos números reales quiere sumar: 3
Dame un valor real: 1.1
Dame un valor real: 2.2
Dame un valor real: 3.3
La suma de los números introducidos es 6.6
```

+++

En el código anterior se debe notar:
- Antes de entrar al bucle, ya se conoce el número de veces que éste se va a repetir.
- Si la expresión de control es `False` ni siquiera se entra al bucle la primera vez.

+++

**Nota**: En los depuradores de los sistemas de desarrollo y en herramientas como [pythontutor](http://www.pythontutor.com/visualize.html#mode=edit) se puede analizar la evolución paso a paso de los programas.

+++

### El acumulador
Por otra parte, el ejemplo implementa una de las ideas básicas de mayor utilidad en programación: el concepto de **acumulador**. Se quiere realizar una operación (la suma) que involucra un conjunto (no determinado en el momento de la programación) de operandos. La idea consiste en dedicar una variable (`suma`) para contener los resultados parciales de dicha operación. 

Dicha variable **acumulador** ha de ser **inicializada** antes de entrar al bucle a un valor que sea **neutro** respecto a la operación seleccionada (el `0` en caso de la suma). Ya dentro del bucle, la variable acumulador es actualizada en cada iteración.

+++

Podríamos haber programado el ejemplo anterior de otra forma, igualmente válida y legible, en la que no *perdemos* el valor inicial de cuantos números queremos sumar. Además, resulta fácil distinguir el caso en el cual no se introdujeron números.

```{code-cell} ipython3
:tags: [remove-output, raises-exception]

# Bucle controlado por un contador que suma un determinado conjunto de reales. (Versión 2)

num_valores = int(input("Diga cuantos números reales quiere sumar: "))

suma = 0.0
contador = 0
while (contador < num_valores):
    valor = float(input("Deme el valor real {} a sumar: ".format(contador)))
    suma += valor
    contador += 1

if num_valores > 0:
    print("La suma de los {} números introducidos es {}".format(num_valores, suma))
else:
    print("El usuario no introdujo ningún valor.")
```

Un ejemplo de ejecución es el siguiente:
```
Diga cuantos números reales quiere sumar: 3
Deme el valor real 0 a sumar: 1.1
Deme el valor real 1 a sumar: 2.2
Deme el valor real 2 a sumar: 3.3
La suma de los 3 números introducidos es 6.6
```

+++

***
<a id='Bucle_for'></a>

+++

## Bucle `for`

Para el caso, muy común, de los bucles controlados por contador, Python tiene el bucle `for` que resulta especialmente adaptado. 

Véase el ejemplo siguiente, que muestra el producto de los enteros incluidos en determinado **rango**:

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

# Determina producto de enteros en rango

inf = int(input("Diga límite inferior del rango: "))
sup = int(input("Diga límite superior del rango: "))

producto = 1
for elem in range(inf, sup+1):
    producto *= elem                             # Se podría usar: producto = producto*elem

print("El producto de los enteros en el rango [{},{}] es {}".format(inf, sup, producto))
```

Un ejemplo de ejecución es el siguiente:
```
Diga límite inferior del rango: 2
Diga límite superior del rango: 6
El producto de los enteros en el rango [2,6] es 720
```

+++

El bucle `for ... in ...` utiliza en este ejemplo la secuencia `range()`.

Así, el bucle `for` del ejemplo asigna de forma iterada y ordenada cada uno de los enteros del rango de que se trate a la variable que actúa como **contador** del bucle, `elem`.

> Así, en el ejemplo de ejecución, la variable `elem` toma iteradamente los valores ``2, 3, 4, 5, 6``.

Por otro lado, en cada una de las iteraciones ejecuta las sentencias contenidas en el cuerpo del bucle.

En el anterior ejemplo se tiene una nueva implementación de la idea del **acumulador**, en este caso representada por la variable `producto` en la que se *acumula* precisamente el resultado de la multiplicación de los enteros en el rango. En consonancia con su propósito, en este caso el acumulador es inicializado a ``1``, que es el valor **neutro** para la operación de multiplicación.

+++

La sentencia `for` de Python tiene una sintaxis que presenta diferencias notables con respecto a la que se utiliza en C/C++ y en otros lenguajes de programación:

```python
for (int elem = inf; elem <= sup; elem = elem + 1)
{
    producto *= elem;
}
```
El `for` de C/C++ describe de manera más explícita el proceso de inicialización del contador, la expresión lógica de control que evalúa la permanencia o no en el bucle, y el incremento (o en general modificación) del contador en cada iteración.

+++

Ahora tenemos una nueva alternativa más compacta para realizar la suma de un determinado conjunto de números reales.

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

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
```

***
<a id='Iterables'></a>

+++

## Iterables
Muchos de los contenedores y, entre ellos las secuencias, son objetos **iterables**, objetos capaces de ir devolviendo uno por uno, desde el primero hasta el último, los elementos que lo componen.

Cualquier objeto iterable es susceptible de ser recorrido por un bucle ``for``. Es lo que hemos hecho más arriba con el iterable ``range()``.

```{code-cell} ipython3
# Crea una lista con los valores impares de una lista de enteros
lista = [1, 3, 2, 7, 5, 4, 6]
impares = []
for x in lista:
    if x % 2:
        impares.append(x)
print(impares)
```

```{code-cell} ipython3
# Sustituye los caracteres en blanco de una cadena por el caracter '_'
cadena = 'Hola amigos'
nueva_cadena = ''  # Cadena vacía
for c in cadena:
    if c == ' ':
        nueva_cadena += '_'
    else:
        nueva_cadena += c

print(nueva_cadena)
```

En la siguiente versión del ejemplo de suma de números sobre el que venimos trabajando, primero creamos una lista con los valores introducidos por teclado. Luego realizamos la suma de sus elementos.

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

# Bucle que suma un determinado conjunto de reales. Versión con lista y for. (Versión 4)

num_valores = int(input("Diga cuantos números reales quiere sumar: "))
lista = []
for i in range(num_valores):
    lista.append(float(input("Deme el valor real {} a sumar: ".format(i))))
    
suma = 0.0
for x in lista:
    suma += x

if num_valores > 0:
    print("La suma de los {} números introducidos es {}".format(num_valores, suma))
else:
    print("El usuario no introdujo ningún valor.")
```

Otra posibilidad hubiese sido crear inicialmente una lista con el tamaño final y luego ir actualizando los valores. Sería sustituir las líneas:
```python
lista = []
for i in range(num_valores):
    lista.append(float(input("Deme el valor real {} a sumar: ".format(i))))
```
por
```python
lista = [0]*num_valores
for i in range(num_valores):
    lista[i] = float(input("Deme el valor real {} a sumar: ".format(i)))
```

+++

### Enumeración de iterables: ``enumerate()``
En ocasiones, además del valor del ítem de una secuencia, necesitamos saber su posición, su índice dentro del objeto iterable. 

Preste atención a la siguiente celda. El fragmento de código crea una lista de tuplas a partir de un iterable, en este caso una lista. El primer elemento de cada tupla es la posición en el iterable del segundo elemento.

```{code-cell} ipython3
# Asociando índice y elemento de un iterable en una lista de tuplas
lista = [1, 3, 5, 7, 2, 4]
lista_tuplas = []

i = 0
for x in lista:
    lista_tuplas.append((i, x))
    i += 1
    
print(lista_tuplas)
```

Para no tener que explicitar el contador ``i`` del ejemplo anterior, Python proporciona la función nativa `enumerate()`. 
Esta función devuelve un objeto que es capaz de asociar en una tupla el índice y el elemento de un objeto iterable si se la invoca con la herramienta adecuada, como por ejemplo con un bucle ``for``.

```{code-cell} ipython3
# Asociando índice y elemento de un iterable en una lista de tuplas con enumerate() 
lista = [1, 3, 5, 7, 2, 4]
lista_tuplas = []

for tupla in enumerate(lista):
    lista_tuplas.append(tupla)
    
print(lista_tuplas)
```

En realidad, el fragmento anterior podría ser aún más compacto usando el constructor ``list()`` o ``tuple()``.

```{code-cell} ipython3
# Asociando índice y elemento de un iterable en una lista de tuplas con enumerate() 
lista = [1, 3, 5, 7, 2, 4]
lista_tuplas = list(enumerate(lista))

print(lista_tuplas)
```

En los siguientes ejemplos vamos a analizar diferentes alternativas para almacenar a partir de una lista de enteros:
* una lista con sus elementos impares
* una lista con las posiciones de los elementos impares en la lista original

La primera opción que proponemos es recurrir a un contador.

```{code-cell} ipython3
# Crea listas con los valores impares y sus posiciones de una lista de enteros (Versión 1)
lista = [1, 3, 2, 7, 5, 4, 6]
impares = []
posiciones = []
i = 0
for x in lista:
    if x % 2:
        impares.append(x)
        posiciones.append(i)
    i += 1

print("La lista con los impares es {} y sus posiciones son {}.".format(impares, posiciones))
```

Otra posibilidad para resolver el problema es ayudarnos de las funciones `len()` y `range()`.

```{code-cell} ipython3
# Crea listas con los valores impares y sus posiciones de una lista de enteros (Versión 2)
lista = [1, 3, 2, 7, 5, 4, 6]
impares = []
posiciones = []
for i in range(len(lista)):
    if lista[i] % 2:
        impares.append(lista[i])
        posiciones.append(i)

print("La lista con los impares es {} y sus posiciones son {}.".format(impares, posiciones))
```

Una tercera posibilidad sería usar la función ``enumerate()``.

```{code-cell} ipython3
# Crea listas con los valores impares y sus posiciones de una lista de enteros (Versión 3)
lista = [1, 3, 2, 7, 5, 4, 6]
impares = []
posiciones = []
for tupla in enumerate(lista):
    if tupla[1] % 2:
        impares.append(tupla[1])
        posiciones.append(tupla[0])

print("La lista con los impares es {} y sus posiciones son {}.".format(impares, posiciones))
```

Finalmente, proponemos la versión más *pitónica*, también usando ``enumerate()``. En ella, utilizamos la propiedad de **desempaquetado** de una tupla, ``i, x = tupla``, evitando esta forma verbosa de acceder a los elementos de la tupla a través de sus índices, ``tupla[0]`` y ``tupla[1]``.

```{code-cell} ipython3
# Crea listas con los valores impares y sus posiciones de una lista de enteros (Versión 4)
lista = [1, 3, 2, 7, 5, 4, 6]
impares = []
posiciones = []
for i, x in enumerate(lista): # i, x es la tupla desempaquetada
    if x % 2:
        impares.append(x)
        posiciones.append(i)

print("La lista con los impares es {} y sus posiciones son {}.".format(impares, posiciones))
```

### Agregación de elementos de diferentes iterables: ``zip()``
En ocasiones, nos interesa trabajar simultáneamente con los elementos que ocupan posiciones correlativas en dos o más iterables.

Preste atención a la siguiente celda, que muestra un ejemplo visto en el tema de **Secuencias**. Tenemos tres tuplas correspondientes a tres alumnos y queremos
agregar en una lista, una tupla con los nombres y apellidos, otra con los dni's y otra con los nia's.

El fragmento de código crea una lista de tuplas a partir de tres iterables, en este caso tres tuplas, `alumno_1`, `alumno_2` y `alumno_3`. La primera tupla de la lista de tuplas está formada por `(alumno_1[0], alumno_2[0], alumno_3[0])` y así sucesivamente.

```{code-cell} ipython3
nombre_apellidos_1 = 'Juan', 'Sierra', 'Gómez'
dni_1 = '13120714E'
nia_1 = 123434
alumno_1 = nombre_apellidos_1, dni_1, nia_1


nombre_apellidos_2 = 'Pedro', 'López', 'Roldán'
dni_2 = '73131714F'
nia_2 = 471394
alumno_2 = nombre_apellidos_2, dni_2, nia_2

nombre_apellidos_3 = 'María de las Mercedes', 'Santurce', 'Bilbao'
dni_3 = '17571924T'
nia_3 = 729219
alumno_3 = nombre_apellidos_3, dni_3, nia_3

lista = []
for i in range(len(alumno_1)):
    tupla = alumno_1[i], alumno_2[i], alumno_3[i]
    lista.append(tupla)
    
print(lista)
```

La función nativa `zip()` nos permite realizar el trabajo anterior de forma más cómoda. Esta función devuelve un objeto que es capaz de asociar en una tupla los elementos de dos o más iterables que ocupan posiciones correlativas si se la invoca con la herramienta adecuada, como por ejemplo con un bucle ``for`` o los constructores `list()` o ``tuple()``.

```{code-cell} ipython3
lista = []
for tupla in zip(alumno_1, alumno_2, alumno_3):
    lista.append(tupla)
    
print(lista)
```

En el ejemplo anterior, hubiese sido aún más compacto usando el constructor ``list()``:

```{code-cell} ipython3
lista = list(zip(alumno_1, alumno_2, alumno_3))
    
print(lista)
```

Veamos una aplicación para calcular el producto escalar de dos vectores y diferentes variantes para resolverlo. En primer lugar, una versión llamémosla *clásica*:

```{code-cell} ipython3
v1 = [1.1, 2.2, 3.3, 4.4]
v2 = [2.2, 3.3, 4.4, 5.5]

prod_esc = 0.0
for i in range(len(v1)):
    prod_esc += v1[i]*v2[i]
    
print('El producto escalar de \n {} \ny \n {} \nes \n {:f}'.format(v1, v2, prod_esc))
```

Una variante usando ``enumerate()``:

```{code-cell} ipython3
v1 = [1.1, 2.2, 3.3, 4.4]
v2 = [2.2, 3.3, 4.4, 5.5]

prod_esc = 0.0
for i, x in enumerate(v1):
    prod_esc += x*v2[i]
    
print('El producto escalar de \n {} \ny \n {} \nes \n {:f}'.format(v1, v2, prod_esc))
```

Finalmente, la variante más elegante y *pitónica* usando ``zip()``. Nótese, de nuevo, el desempaquetado *in situ* de la tupla devuelta en cada iteración por la función ``zip()``.

```{code-cell} ipython3
v1 = [1.1, 2.2, 3.3, 4.4]
v2 = [2.2, 3.3, 4.4, 5.5]

prod_esc = 0.0
for x, y in zip(v1, v2):  # x, y es la tupla desempaquetada
    prod_esc += x*y
    
print('El producto escalar de \n {} \ny \n {} \nes \n {:f}'.format(v1, v2, prod_esc))
```

***
<a id='Sentencia_break:_salida_temprana_de_un_bucle'></a>

+++

## Sentencia `break`: salida temprana de un bucle

En muchas ocasiones resulta conveniente salir de un bucle, no mediante la evaluación a `False` de la expresión de control, sino desde dentro del bucle utilizando un `if` junto con la sentencia `break` de **salto incondicional**.

En el siguiente código se muestra un ejemplo típico. Se trata de determinar si un determinado número entero es primo o no.

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

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
```

Una posible ejecución de la celda es:
```
Deme un entero positivo mayor que 1: 97
El número 97 es primo
```

+++

Una advertencia: existen formas más eficientes de realizar la tarea propuesta; el código anterior debe verse como un intento inicial. 

Se trata básicamente de aplicar la propia definición de número primo: *aquel que es divisible solo por él y por la unidad*. 

La estrategia entonces consiste en hallar, mediante un bucle, todos los posibles divisores *legítimos* que harían que se pudiera decidir que el número no es primo. Se utiliza un bucle `for` **por rango**, y el rango elegido es $[2,numero)$. Obsérvese que el límite inferior está incluido en el rango y el superior no. Y esto es precisamente lo que se requiere.

+++

Se debe notar que el bucle necesario tiene una especie de *carácter asimétrico*:
* por una parte, para concluir que el número es primo, se debe llevar el bucle hasta su conclusión, investigando todos los posibles divisores, sin hallar ningún divisor exacto.
* por el contrario, para concluir que el número no es primo, basta con encontrar el primer divisor exacto.

En sintonía con esta _asimetría_ del problema, se utiliza una construcción en la cual al bucle `for` **por rango** se le asocia una variable **centinela**, **testigo** o **bandera**, `es_primo`. Si en el transcurso de las iteraciones se detectara, mediante un condicional `if`, que el número investigado es divisible por alguno de los divisores posibles, se sale inmediatamente del bucle, utilizando la sentencia `break` y _activando_ la bandera.

Ya fuera del bucle, se interroga el valor del **centinela** para informar al usuario sobre el resultado encontrado.

+++

Las variables **testigo** son inicializadas a un valor **de reposo** antes de entrar a una zona del código en la que deseamos señalar si un determinado evento se ha producido o no. Las variables centinela suelen ser booleanas, pero en ocasiones pueden usarse enteros que tomarán diferentes valores en dependencia de las sentencias que sean ejecutadas o no. De esta manera, cuando su valor sea interrogado al final, indicarán el *camino* concreto que siguió el programa, permitiendo sacar las oportunas conclusiones.

+++

Se debe comprender que la salida anticipada de un bucle constituye un recurso que puede mejorar la escritura o legibilidad del código. No obstante, siempre se puede modificar el bucle de manera que solo se pueda decidir la permanencia o salida del mismo a partir de la expresión de control. 

En el ejemplo que nos ocupa:

```{code-cell} ipython3
:tags: [remove-output, raises-exception]

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
```

La modificación ha supuesto cambiar el `for` por un `while`. Observe la implementación *manual* del contador `div` que actúa como divisor y que debe ser inicializado fuera del bucle. Véase que la expresión de control incluye la condición de que no se haya detectado todavía un divisor para continuar iterando.

+++

Una versión más compacta se logra si nos damos cuenta que el propio contador `div` puede actuar como variable testigo. Si `div == numero` tras el bucle es que hemos recorrido todo el rango de valores sin encontrar un divisor. 

Así:

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

# Determina si un número entero es primo. Versión usando while y el contador como testigo. (Versión 3)

numero = int(input('Deme un entero positivo mayor que 1: '))

div = 2
while numero % div != 0:
    div += 1

if div == numero:
    print("El número {} es primo".format(numero))
else:
    print("El número {} no es primo".format(numero))
```

Y en su versión con bucle `for` **por rango**:

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

# Determina si un número entero es primo. Versión usando for y el contador como testigo. (Versión 4)

numero = int(input('Deme un entero positivo mayor que 1: '))

for div in range(2, numero+1):
    if numero % div == 0:
        break

if div == numero:
    print("El número {} es primo".format(numero))
else:
    print("El número {} no es primo".format(numero))
```

Decidir cuál de las implementaciones es superior es cuestión de debate. Más allá de optar entre las versiones `for` **por rango** o `while`, a nuestro juicio, el uso explícito de la variable centinela `es_primo` genera un código más legible aunque menos eficiente.

+++

***
<a id='Sentencia_continue'></a>

+++

### Sentencia `continue`

De forma similar al `break`, la sentencia `continue` provoca un _salto incondicional_ durante la ejecución de un bucle. La sentencia `continue`, a diferencia del `break`, no abandona el bucle, sino que cuando es ejecutada provoca un _salto_ inmediato al inicio del bucle, para procesar la siguiente iteración.

```{code-cell} ipython3
# Ejemplo de uso de la sentencia continue: no se imprimen los múltiplos de 3 (versión 1)

lista = []
limite = 25
for i in range(limite):
    if i%3 == 0:
        continue
    lista.append(i)
    
print(lista)
```

Una forma más lógica sin ``continue`` es la que sigue:

```{code-cell} ipython3
# Ejemplo de uso de la sentencia continue: no se imprimen los múltiplos de 3 (versión 2)

lista = []
limite = 25
for i in range(limite):
    if i%3 != 0:
        lista.append(i)
    
print(lista)
```

La sentencia `continue` es poco utilizada. En algunas circunstancias ofrece una solución más estructurada y comprensible. No la usaremos durante el curso.

+++

***
<a id='Bucles_anidados'></a>

+++

## Bucles anidados

Con cierta frecuencia la solución de un problema exige el uso de bucles que estén contenidos dentro de otros. Los **bucles anidados** pueden tener tantos niveles como se quiera. 

La idea clave es: en cada iteración de un bucle externo, ocurren todas las iteraciones posibles de los bucles internos.

El siguiente ejemplo es ilustrativo de este proceso. En este caso, se tienen dos bucles anidados implementados mediante `for`.

```{code-cell} ipython3
for i in range(1, 11):
    for j in range(1, 11):
        print("{:4d}".format(i*j), end=' ')
    print()
```

El bucle externo recorre todos los enteros en el intervalo $[1,10]$ y utiliza un índice o contador `i` y el interno recorre el mismo rango pero asignando los valores del mismo a la variable de control del bucle `j`. De manera que, en la primera iteración del bucle externo, cuando `i` tiene el valor `1`, el bucle interno *agota* todas las posibles iteraciones, con `j` *barriendo* todos los valores del rango $[1,10]$.

Dentro del bucle interno se saca por pantalla, utilizando un formato útil para alinear correctamente las columnas de una tabla, el producto de ambos contadores. Observe que en esta función `print()`, el caracter a imprimir al final (normalmente el cambio de línea), es sustituido por una cadena de caracteres que representa un espacio en blanco, `end=' '`.

+++

El sangrado existente en el segundo `print()` informa al intérprete de Python que este debe ser ejecutado, como parte del bucle externo, cada vez que el interno termina su ejecución. Su propósito es simplemente provocar un cambio de línea. 

El objetivo final logrado es la salida por la consola de la tabla de multiplicar. El ejemplo utilizado en este caso puede resultar trivial, pero el concepto ilustrado tiene muchas otras aplicaciones.

+++

El siguiente ejemplo ilustra algunos de los conceptos vistos en este tema. La celda calcula una lista con las posiciones de la primera ocurrencia de cada elemento de una lista en otra.

```{code-cell} ipython3
# Posiciones de la primera ocurrencia de los elementos de lista2 en lista1
lista1 = [1, 3, 5, 7, 9, 2, 4, 6, 8]
lista2 = [1, 1, 3, 3, -3, 7, -8]
posiciones = [0]*len(lista2)
for i, x in enumerate(lista2):
    encontrado = False
    for j, y in enumerate(lista1):
        if x == y:
            encontrado = True
            break
    if encontrado:
        posiciones[i] = j
    else:
        posiciones[i] = None
        
print('Los elementos de la lista \n {} \nse encuentran en las posiciones \n {} \nde la lista \n {}'.
     format(lista2, posiciones, lista1))
```

### El tipo ``NoneType``
El tipo ``NoneType`` permite representar aquellos objetos que **no tienen valor**. Es el equivalente a ``null`` en lenguajes como C++.

Una variable de tipo ``NoneType`` solo puede tener el valor ``None``, que es una constante literal predefinida, igual que los son ``True`` o ``False``.

El ejemplo anterior muestra uno de los usos habituales de este tipo. Algunos de los elementos buscados no se encuentran en la lista. Una forma concisa de reflejarlo es con el literal ``None``.

La forma correcta de comprobar si una variable no tiene asignada un valor es con el operador ``is``.

```{code-cell} ipython3
# Listado de los elementos de lista2 ausentes en lista1 usando la lista de posiciones
lista_ausentes = []
for i, x in enumerate(posiciones):
    if x is None:
        lista_ausentes.append(lista2[i])
print('Los valores {} de la lista\n {} \nno se encuentran en la lista \n {}.'.format(lista_ausentes, lista2, lista1))
```

***
<a id='Listas_por_comprension'></a>

+++

## Listas por comprensión
Un uso habitual que hemos visto de un bucle ``for`` es transformar una lista en otra. Las **listas por comprensión** (**comprehension list**) es una forma compacta de lograr el mismo efecto en una única línea.

Supongamos un sencillo ejemplo en el que deseamos obtener una lista con los cuadrados de otra. Una solución con un bucle ``for`` sería la siguiente:

```{code-cell} ipython3
lista = [1, 2, 3, 4, 5]
lista_cuad = []
for x in lista:
    lista_cuad.append(x*x)
print(lista_cuad)
```

Este mismo resultado podríamos obtenerle con una comprensión mediante el siguiente fragmento de código:

```{code-cell} ipython3
lista = [1, 2, 3, 4, 5]
lista_cuad = [x*x for x in lista]
print(lista_cuad)
```

Entre los corchetes ``[]`` podríamos *traducir*:
> Crea una lista con la expresión ``x*x`` para cada ``x`` perteneciente al iterable ``lista``

+++

Las listas por comprensión no son sino mero **azúcar sintáctico**, pero su uso está muy extendido en Python. Hasta que el programador novel se acostumbra, pueden parecer una construcción sintáctica que empeora la legibilidad. Sin embargo:
* son construcciones más compactas
* son más rápidas que su equivalente con bucle ``for``, porque internamente se reserva espacio para la nueva lista antes de empezar a formarla.

+++

Veamos a continuación otro uso habitual. En este caso, deseamos formar una lista a partir de otra **filtrando** algunos de los elementos.

Por ejemplo, formemos una lista solo con los cuadrados de los elementos pares de otra. La solución con un bucle ``for`` sería la siguiente:

```{code-cell} ipython3
lista = [1, 2, 3, 4, 5]
lista_cuad = []
for x in lista:
    if x%2 == 0: 
        lista_cuad.append(x*x)
print(lista_cuad)
```

Ahora, su equivalente con una lista por comprensión:

```{code-cell} ipython3
lista = [1, 2, 3, 4, 5]
lista_cuad = [x*x for x in lista if x%2 == 0]
print(lista_cuad)
```

Entre los corchetes ``[]`` podríamos *traducir*:
> Crea una lista con la expresión ``x*x`` para cada ``x`` perteneciente al iterable ``lista`` que cumpla ``x%2 == 0``

+++

En general, en este curso no haremos un uso exhaustivo de listas por comprensión, pues preferimos en un nivel inicial que el alumno trabaje con construcciones más explícitas usando ``for``.
