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

# Manejo de excepciones  

+++

[Tipos de errores de programación](#Tipos_de_errores_de_programación)<br>
[Errores en tiempo de ejecución](#Errores_en_tiempo_de_ejecución)<br>
[La estructura condicional `try ... except`](#La_estructura_condicional_try_except)<br>
[Creación manual de excepciones: `raise`](#Creación_manual_de_excepciones)

+++

***
<a id='Tipos_de_errores_de_programación'></a>

+++

## Tipos de errores de programación
Al programar es normal cometer errores, que son básicamente de tres tipos:

- **Sintácticos**: el código escrito no conforma una expresión válida en Python y es el propio intérprete el que lanza el aviso con el error detectado. Suelen ser fáciles de corregir.   
- **Errores en tiempo de ejecución** (**Runtime errors**): el código es correcto pero, en ocasiones, al ejecutarse, el programa falla. 
    - Estos errores son fáciles de corregir si el programador detecta el error en la *fase de desarrollo*, ya que el intérprete lanza una **excepción**. Como veremos enseguida, Python tiene herramientas para que podamos **manejar** adecuadamente estos casos excepcionales. 
    - En caso contrario, si el error surge con el programa ya *en producción*, entonces los efectos pueden ser catastróficos y reputacionalmente graves.
- **Semánticos**: el código es correcto y el programa se ejecuta sin problemas, pero los resultados no son válidos. Son los errores más difíciles de detectar y/o corregir pues muchas veces el programador o cliente ni siquiera es consciente de que algo va mal.

De los dos primeros hemos visto ya algún ejemplo. Seguro que a estas alturas habéis *padecido* bastantes del tercer tipo. Veamos algún ejemplo de error semántico.

```{code-cell} ipython3
# Ejemplo 1 error semántico
# Cálculo de la media de dos números
x = 3.5
y = 5.6

media = x + y / 2  # Necesitamos paréntesis para que la primera operación realizada no sea y/2
```

```{code-cell} ipython3
# Ejemplo 2 error semántico
# Cálculo de área de un rectángulo
lado1 = 3.5
lado2 = 5.6

area = lado1*lado1  # Inadvertidamente hemos usado dos veces lado1
```

```{code-cell} ipython3
# Ejemplo 3 error semántico
# Deseamos que una expresión sea True si un valor entero no está en el intervalo 0 <= valor <=3 
valor = 4
resultado = valor < 0 and valor > 3  # La conectiva lógica correcta es or
```

```{code-cell} ipython3
# Ejemplo 4 error semántico
# Calculamos la media de una serie de valores en una lista
lista = [1, 3, 5, 2, 4]
media = 1  # Media está incorrectamente inicializado. Debe ser media = 0
for x in lista:
    media += x
media /= len(lista)
```

***
<a id='Errores_en_tiempo_de_ejecución'></a>

+++

## Errores en tiempo de ejecución
Dentro del conjunto de tipos de **errores en tiempo de ejecución** que dan lugar a una **excepción**, están aquellos cuyo origen es debido al uso de un **tipado dinámico** por parte de Python.

Por ejemplo:
* Realización de una operación incompatible entre datos de tipos diferentes, excepción `TypeError`.
* Utilizar un identificador en una expresión que aún no está definido, excepción `NameError`.

De hecho, en un lenguaje con **tipado estático**, como C/C++, estos errores serían burdos **errores sintácticos** detectados en fase de compilación. Algunos de estos errores, en especial los del segundo tipo, son fácilmente resolubles.

```{code-cell} ipython3
:tags: [raises-exception]

# Error: Tipos incompatibles, excepción TypeError
x = 3
x + '2'
```

```{code-cell} ipython3
:tags: [raises-exception]

# Error: Identificador no definido, excepción NameError
a = b + 1
```

Hay otras muchas situaciones **excepcionales** que pueden generar un error en tiempo de ejecución. Por ejemplo:
* el usuario introduce datos con formato incorrecto
* se intenta realizar una operación indeterminada, como $x/0$, $0/0$, etc.
* se intenta acceder a un archivo inexistente

Para ver cómo **manejar las excepciones** (**handling exceptions**) en Python, vamos a utilizar un ejemplo sencillo: 
>una división que eventualmente genere la excepción `ZeroDivisionError`si el usuario utiliza como denominador un `0`.

```{code-cell} ipython3
:tags: [raises-exception]

numerador = 5
denominador = 0
cociente = numerador/denominador

print('{}/{} = {}'.format(numerador, denominador, cociente))
```

Veamos dos alternativas para *atacar* el problema de los errores en tiempo de ejecución:
* El enfoque **Piensa antes de actuar**
* El enfoque **Es más sencillo pedir perdón que pedir permiso**

+++

### El enfoque "*Piensa antes de actuar*"

El enfoque **Piensa antes de actuar** (**LBYL**, **L**ook **B**efore **Y**ou **L**eap) preconiza la realización **anticipada** de pruebas explícitas para determinar si se satisfacen las condiciones que evitan la aparición de errores. 

Veámoslo con nuestro ejemplo:

```{code-cell} ipython3
numerador = 5
denominador = 0

if denominador != 0:
    cociente = numerador/denominador
    print('{}/{} = {}'.format(numerador, denominador, cociente))
else:
    print('Error: el denominador es nulo')
```

### El enfoque "*Es más sencillo pedir perdón que pedir permiso*"

El enfoque **Es más sencillo pedir perdón que pedir permiso** (**EAFP**, **E**asier to **A**sk **F**orgiveness than **P**ermission) promueve que, por regla general, es mejor **probar** (**try**) directamente la ejecución de las sentencias y, para los casos excepcionales, **capturar** (**catch**) el error.

Este enfoque es el considerado *pitónico*. El aspecto clave para preferirlo sobre el anterior está en usarlo para tratar los casos **excepcionales**, que previsiblemente se producirán con **baja frecuencia**.
> En nuestro ejemplo, cualquier usuario sabe que no está definida la división por 0, por lo que no tiene mucho sentido, salvo por despiste, que utilice un denominador nulo.

El enfoque **EAFP** se realiza fácilmente con la **estructura condicional** `try ... except`.

+++

***
<a id='La_estructura_condicional_try_except'></a>

+++

## La estructura condicional `try ... except`
La **estructura condicional** `try ... except` es:
```python
try:
    # Probamos nuestro código
except TipoDeExcepcion:
    # Tratamos la excepción TipoDeExcepcion si ha sido capturada en el bloque try
```

La estructura condicional `try ... except` funciona del siguiente modo:
* El bloque `try` se ejecuta (*no pedimos permiso* para ejecutar las sentencias).
* Si no se produce ninguna excepción, se salta el bloque o bloques `except`.
* Si al ejecutar alguna de las sentencias del bloque `try` se produce una excepción, **el resto de sentencias** del bloque ``try`` **se ignoran**.
* Si el bloque `try`ha lanzado una excepción y su tipo coincide con alguna de las contempladas en un bloque `except`, tratamos la excepción ejecutando únicamente las sentencias de ese bloque (*pedimos perdón* por el error cometido). 
* Si el tipo de la excepción no coincide con ninguna de las contempladas se reenvía a otro posible bloque `try` más externo que contenga a este o, de no existir, se detiene la ejecución con el mensaje correspondiente.

+++

En la siguiente celda, el usuario debe introducir los valores por teclado:

```{code-cell} ipython3
:tags: [remove-output, raises-exception]

numerador = float(input('Dame el numerador:'))
denominador = float(input('Dame el denominador:'))

try:
    cociente = numerador/denominador
    print('{}/{} = {}'.format(numerador, denominador, cociente))
except ZeroDivisionError:
    print('Error: el denominador es nulo')
```

El código anterior no está exento de otro tipo de errores, imputables al usuario. Así, en lugar de un valor numérico en alguno de los dos valores introducid, por ejemplo, `kk`.
> En este caso saltará una excepción `ValueError`.

Por tanto, dado que la introducción de datos está sujeta a posibles errores, podemos intentar también *manejarlos*.

Veamos primero una solución con un enfoque **LBYL**. Para ello, necesitamos una función para **analizar** (**parse**) si los caracteres de las secuencias de entrada conforman un número válido, devolviéndonos en ese caso `True`. Esa función, que podría llamarse `isfloat()`, no existe de forma nativa en Python y, como veremos enseguida, su existencia sería redundante.

Una posible solución sería la siguiente, donde, en su caso, no identificamos qué cadena ha podido ser mal introducida:
```python
cad_num = input('Numerador: ')
cad_den = input('Denominador: ')

if isfloat(cad_num) and isfloat(cad_den):
    numerador = float(cad_num)
    denominador = float(cad_den)
    if denominador != 0:
        cociente = numerador/denominador
        print('{}/{} = {}'.format(numerador, denominador, cociente))
    else:
        print('Error: el denominador es nulo')
else:
    print('Error: un valor introducido no es un número válido')
```

Veamos como el enfoque **EAFP** resuelve el problema de forma concisa y elegante:

```{code-cell} ipython3
:tags: [remove-output, raises-exception]

try:
    numerador = float(input('Numerador: '))
    denominador = float(input('Denominador: '))
    cociente = numerador/denominador
    print('{}/{} = {}'.format(numerador, denominador, cociente))
except ZeroDivisionError:
    print('Error: el denominador es nulo')
except ValueError:
    print('Error: el valor introducido no es un número válido')
```

Sintácticamente es factible usar un bloque `except` sin especificar el tipo de excepción. Sin embargo, es una práctica desaconsejada porque capturamos todos los errores sean de la naturaleza que sean, ocultándonos incluso aquellos de los que no somos conscientes en el momento de hacer el programa y que, quizás, necesiten de un manejo especializado.

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

# ¡No utilices nunca un bloque except desnudo!
try:
    numerador = float(input('Numerador: '))
    denominador = float(input('Denominador: '))
    print('{}/{} = {}'.format(numerador, denominador, numerador/denominador))
except:
    print('Ocurrió un error')
```

### `try ... except ... else ... finally`
De forma adicional a `try ...except` tenemos dos palabras clave, `else` y `finally` que, **opcionalmente**, pueden facilitarnos  aún más el manejo de las excepciones.

La estructura básica es:

```{code-cell} ipython3
try:
    print("Probamos nuestro código susceptible de lanzar excepciones.")
except:
    print("Aquí tratamos las excepciones.")
else:
    print("Esta es la parte del programa que creemos que está libre de excepciones.")
finally:
    print("Ocurra lo que ocurra, esta parte la ejecutamos siempre.")
```

El objetivo del bloque `else` es separar claramente la zona que creemos susceptible de generar excepciones de la que está libre de ellas. Esto tiene una ventaja adicional: si se produce una excepción no esperada del mismo tipo de las que ya manejamos en el bloque `try` no quedará enmascarada y podremos darla rehaciendo el código el tratamiento adecuado.

El bloque `finally` suele usarse para tareas de **limpieza** (**cleanup**) como cerrar recursos que se han abierto, por ejemplo un fichero, o cualquier otro tipo de sentencias que es necesario ejecutar haya habido o no una excepción.

Veamos nuestro ejemplo con estos nuevos elementos:

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

try:
    numerador = float(input('Numerador: '))
    denominador = float(input('Denominador: '))
    cociente = numerador/denominador
except ZeroDivisionError:
    print('Error: el denominador es nulo')
except ValueError:
    print('Error: el valor introducido no es un número válido')
else:
    print('{}/{} = {}'.format(numerador, denominador, cociente))
finally:
    print('\nFin del programa.')
```

Python genera de forma automática mensajes de error para los tipos de excepciones predefinidos. Si no tenemos una necesidad especial de lanzar nuestro propio mensaje es la mejor opción.

Así, una forma aún más compacta de programar el ejemplo anterior sería:

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

try:
    numerador = float(input('Numerador: '))
    denominador = float(input('Denominador: '))
    cociente = numerador/denominador
except (ZeroDivisionError, ValueError) as error: 
    print(error)
else:
    print('{}/{} = {}'.format(numerador, denominador, cociente))
finally:
    print('\nFin del programa.')
```

En el ejemplo anterior, ``error`` es una variable. Podríamos llamarla ``e``, ``err``, etc.

En la sintaxis `except (TipoDeError_1, ..., TipoDeError_n) as error`, la cadena de caracteres `error` toma como valor el mensaje de error que Python asocia de forma automática al `TipoDeError` que ha generado la excepción.

+++

En los ejemplos previos, el bloque `except` se limita a lanzar un mensaje de error. Obviamente este bloque puede ocuparse de muchos más aspectos relativos a tratar los problemas derivados de la excepción. 

No debemos perder de vista que **manejando la excepción evitamos que se detenga la ejecución del programa** de forma intempestiva.

En la siguiente variante, mediante un bucle, volvemos a solicitar al usuario los valores mientras éstos no sean válidos.

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

print('Introduzca un numerador y un denominador:')
while True:
    try:
        numerador = float(input('Numerador: '))
        denominador = float(input('Denominador: '))
        cociente = numerador/denominador
    except (ZeroDivisionError, ValueError) as error: 
        print('Se ha producido el error: \'{}\'.'.format(error))
        print('Por favor, vuelva a introducir los valores:')
    else:
        print('{}/{} = {}'.format(numerador, denominador, cociente))
        break
```

Una posible ejecución del fragmento anterior sería:
```
Introduzca un numerador y un denominador:
Numerador: xx
Se ha producido el error: 'could not convert string to float: 'xx''.
Por favor, vuelva a introducir los valores:
Numerador: 5
Denominador: 0
Se ha producido el error: 'float division by zero'.
Por favor, vuelva a introducir los valores:
Numerador: 5
Denominador: 4
5.0/4.0 = 1.25
```

+++

***
<a id='Creación_manual_de_excepciones'></a>

+++

## Creación manual de excepciones: `raise`
Muchos de los ejemplos de temas previos se ejecutan correctamente si utilizamos *entradas legítimas*. 

Analicemos de nuevo el ejemplo de determinar si un número es primo cuando el usuario introduce un entero negativo o nulo. 

```{code-cell} ipython3
:tags: [remove-output, raises-exception]

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

Por ejemplo, si introducimos ``-3``, el resultado es incorrecto. Es un **error semántico**. Este tipo de situaciones es frecuente incluso en programas comerciales y, a veces, las consecuencias son funestas. Por supuesto, si introducimos el valor `kk` tendremos un **error en tiempo de ejecución**.

La creación de un programa robusto frente a todas las posibles entradas, es una de las facetas de la **programación defensiva**. Muchas veces, al programar nos centramos en los aspectos algorítmicos de un problema, pero más tarde es necesario ir progresivamente **refinando el código**. La realización de **programas de prueba** en paralelo que nos permitan testar nuestro código es otra faceta indespensable en la ingeniería del software.

Por ejemplo, la inclusión en el siguiente código del condicional que exige que el número sea mayor que uno, corrige el error semántico y la inclusión de `try ... except` evita formatos de entrada incorrectos. 

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

# Determina si un número entero es primo. Manejo de excepciones. (Versión 2)

try:
    numero = int(input('Deme un entero positivo mayor que 1: '))
except ValueError:
    print("El valor introducido no es numérico.")
else:
    if numero >= 2:  # Solventamos el error semántico
        es_primo = True
        for div in range(2, numero):
            if numero % div == 0:
                es_primo = False
                break

        if es_primo:
            print("El número {} es primo".format(numero))
        else:
            print("El número {} no es primo".format(numero))
    else:
        print("El entero debe ser igual o mayor que 2")
```

El hecho de que el usuario introduzca un valor menor que 2 para calcular un número primo podemos considerarlo claramente como un caso excepcional: es un error que es lógico esperar que se produzca con poca frecuencia. Entonces, ¿podríamos **forzar** (**levantar**, **raise**) que se genere esta
excepción **manualmente**? La respuesta es sí: con la sentencia `raise`. 

Veámosla en acción en el siguiente ejemplo. En este caso, se omite el bloque ``else`` sacándolo fuera del bucle ``while``.

```{code-cell} ipython3
:tags: [raises-exception, remove-output]

# Determina si un número entero es primo. Manejo de excepciones. raise. (Versión 3)

while True:
    try:
        numero = int(input('Deme un entero positivo mayor que 1: '))
        if numero < 2:
            raise ValueError('El entero debe ser igual o mayor que 2.')
        break  # Si ha llegado aquí, no se ha producido ninguna excepción
    except ValueError as error: 
        print('Se ha producido el error: \'{}\'.'.format(error))
        print('Por favor, vuelva a introducir el valor.')

# A partir de aquí sabemos que estamos exentos de las excepciones contempladas
es_primo = True
for div in range(2, numero):
    if numero % div == 0:
        es_primo = False
        break

if es_primo:
    print("El número {} es primo".format(numero))
else:
    print("El número {} no es primo".format(numero))
```

Una posible ejecución del fragmento anterior sería:
```
Deme un entero positivo mayor que 1: kk
Se ha producido el error: 'invalid literal for int() with base 10: 'kk''.
Por favor, vuelva a introducir el valor.
Deme un entero positivo mayor que 1: -3
Se ha producido el error: 'El entero debe ser igual o mayor que 2.'.
Por favor, vuelva a introducir el valor.
Deme un entero positivo mayor que 1: 97
El número 97 es primo
```

+++

Un formato habitual para forzar manualmente una excepción es `raise TipoDeError(Mensaje)`. Aunque un programador puede personalizar sus propios *tipos de error*, lo recomendable es comprobar si alguno de los [tipos de excepción nativos de Python](https://docs.python.org/3/library/exceptions.html#bltin-exceptions) se ajusta al tipo de error que queremos lanzar. Así, en nuestro ejemplo, parece lógico catalogar el error que puede cometer el usuario al introducir un valor no contemplado como del tipo `ValueError`.

El `Mensaje` que ponemos como argumento es el que se mostrará cuando `except` trate la excepción. En este caso, con la sintaxis `except TipoDeError as error` la variable `error` toma como valor la cadena de caracteres `Mensaje` que hemos asociado al `TipoDeError`. 

>En el ejemplo, tenemos dos posibles fuentes de excepciones `ValueError`. Una forzada con nuestro mensaje personalizado y la otra automática si el usuario introduce un valor que no se corresponde con un entero. El mensaje asociado a esta última también se genera de forma automática. ¡Comprobadlo!
