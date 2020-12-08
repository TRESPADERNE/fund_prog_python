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

# Funciones predefinidas

+++

[Introducción](#Introducción)<br>
[Funciones nativas](#Funciones_nativas)<br>
[Funciones definidas en módulos](#Funciones_definidas_en_módulos)<br>
[Introspección](#Introspección)<br>
[El operador ``.``](#El_operador_punto)<br>
[Conversiones de tipos](#Conversiones_de_tipos)

+++

***
<a id='Introducción'></a>

+++

## Introducción

Las expresiones combinan valores y operadores para obtener un nuevo valor. No obstante, si nos concentramos por el momento en la aritmética, existen operaciones matemáticas a las que usualmente tenemos acceso en una calculadora comercial convencional, como la aplicación de funciones matemáticas comunes, tales como raíz cuadrada, potencias, funciones trigonométricas, logaritmos, etc. entre muchas otras.

Python, al igual que otros lenguajes de programación, tiene también el concepto de **función**, cuyo significado no coincide de forma exacta con la definición matemática, pero que puede ser utilizada para dar cuerpo a estas últimas.

Las funciones de Python serán objeto de un estudio más detallado posteriormente, donde aprenderemos a programar nuestras propias funciones. De momento, sin embargo, iremos introduciendo las **funciones nativas** (**built-in functions**) que Python pone a nuestra disposición.

+++

***
<a id='Funciones_nativas'></a>

+++

## Funciones nativas
Un ejemplo de función numérica que está siempre a nuestra disposición es `abs()`, que se utiliza para hallar el valor absoluto de valores enteros o reales y el módulo de números complejos. 

Nótese en la celda siguiente el uso de **comentarios**: líneas de texto libre, que comienzan con el carácter `#` y que se extienden hasta el final de la línea. Estos comentarios son ignorados por el intérprete, pero son útiles para aclarar el funcionamiento del código.
> La regla de estilo **PEP 8** sugiere dejar un espacio en blanco tras `#`

```{code-cell} ipython3
# Uso de la función abs()
abs(-1)
```

```{code-cell} ipython3
# Las funciones pueden aparecer formando parte de expresiones más complejas. 
# ¿Puedes predecir el resultado de la siguiente expresión?
10**abs(2*3 - 7) + 5
```

La expresión
```python
10**abs(2*3 - 7) + 5
```
es interpretada por Python siguiendo las reglas de precedencia. Así, la potencia debe ser evaluada primero. Pero para hacerlo, el intérprete necesita primero obtener el valor absoluto de la subexpresión que está entre los paréntesis, los cuales forman parte de la sintaxis de la función. Los pasos serían:
1. Se evalúa la subexpresión `2*3 - 7`, obteniéndose el valor `-1`. Este valor es el **parámetro** que se **envía** a la función `abs()`.
2. La función `abs()` **devuelve** el valor absoluto de `-1`, es decir, `1` .
3. El valor devuelto `1` es el exponente de la base `10`. El resultado es `10`.
4. Al valor `10` se le suma el operando `5`.

+++

Otro ejemplo, es la función predefinida `round()`, que devuelve redondeada la expresión entre paréntesis al entero más cercano, `3` en el ejemplo:

```{code-cell} ipython3
round(3.1)
```

Las funciones en Python pueden diseñarse para recibir un número opcional de parámetros.
Así, la función `round()` puede ser utilizada con dos parámetros: el primero sigue siendo el número real a redondear, pero el segundo es un entero que especifica el número de lugares decimales para el redondeo.

```{code-cell} ipython3
# Prueba diferentes lugares decimales para el redondeo
round(3.14159, 3)
```

Un elemento importante de la sintaxis de los lenguajes de programación es que admiten la **composición**:
>Cualquier subexpresión que participe en una expresión puede ser sustituida por otra subexpresión equivalente, originando una expresión resultante que será también sintácticamente correcta. 

Esto incluye el uso de las funciones en las expresiones. Ya vimos antes que el valor del parámetro que se envía a una función puede ser el resultado de la evaluación de otra expresión. 

Por ejemplo:

```{code-cell} ipython3
# ¿Cuál será el valor que resulta? ¿En que orden serán llamadas las funciones?
abs(round(3.5) - 10)
```

Existen funciones predefinidas asociadas al trabajo con **cadenas de caracteres** (y de otras **secuencias**) que veremos a lo largo del curso. Por el ejemplo, la función `len()` devuelve un entero con el tamaño de la cadena, es decir, el número de caracteres que la forman, incluidos espacios en blanco, que son caracteres al fin y al cabo.

```{code-cell} ipython3
len("hola mundo ")
```

Funciones como `abs()`, `round()` o `len()` están predefinidas y directamente disponibles para el intérprete de Python. Existen otras muchas funciones en esta situación, que iremos viendo poco a poco. Una lista completa de las mismas puede ser consultada en https://docs.python.org/3/library/functions.html

+++

***
<a id='Funciones_definidas_en_módulos'></a>

+++

## Funciones definidas en módulos
Además de las funciones **nativas** del lenguaje existen muchas otras, útiles en diferentes campos, que están disponibles si se **importa** el **módulo** adecuado.

Una discusión completa del significado de los módulos, cómo trabajar con ellos y cómo crearlos se hará más adelante. Por ahora baste mencionar que mediante ellos podemos acceder a un conjunto suplementario de funciones. 

Una forma de *importar* todas las funciones de un módulo es con la expresión:
```python
from modulo import *

```
Por ejemplo, el modulo `math` contiene las habituales funciones matemáticas, `cos()`, `exp()`,`log()`, etc., funciones coincidentes con las de la biblioteca homónima del lenguaje C.

Un conjunto completo de las funciones del módulo `math` se encuentra en https://docs.python.org/3/library/math.html.

```{code-cell} ipython3
# ¿Puedes predecir el resultado antes de ejecutarlo?
from math import * # Importamos el módulo math
log(exp(cos(0)))
```

Aunque importar con la expresión `from modulo import *` puede resultar cómodo, lo cierto es que es totalmente desaconsejable. La razón es que diferentes módulos pueden contener identificadores coincidentes.

Por ejemplo, los módulos `math` y `cmath` (este último adaptado al cálculo con números complejos) tienen ambos una función para el cálculo de raíces cuadradas, `sqrt()`.

En el ejemplo siguiente, al importarse en segundo lugar el módulo `math` se **sobrescribe** la función `sqrt()` para complejos y el cálculo produce un **error en tiempo de ejecución** `ValueError`. ¡Se ha producido una **colisión** entre identificadores!

```{code-cell} ipython3
:tags: [raises-exception]

from cmath import *
from math import *

sqrt(-3)
```

Nótese que el hecho de que se produzca este error es una buena noticia. Imaginad una **colisión** entre dos funciones con desempeños diferentes que no generen este tipo de error. ¡Tendríamos un **error semántico** de difícil detección!

Si en la celda anterior cambiamos el orden de importación, el error desaparece. ¡Verifícalo!

+++

### Procedimiento de importación
¿Cuál es la manera correcta de proceder? Veámoslo con el mismo ejemplo.

```{code-cell} ipython3
import cmath
import math

cmath.sqrt(-3)
```

Ahora, para acceder a las funciones de cada módulo anteponemos su nombre seguido del operador `.`. 

Es cierto que el código resultante es más verboso, pero evitamos colisiones entre los identificadores de los objetos definidos en cada módulo. Tanto ``cmath.`` como ``math.`` actúan como **espacio de nombres** que permiten acceder al correcto identificador contenido en cada módulo.

+++

***
<a id='Introspección'></a>

+++

## Introspección
Ya hemos comentado que en Python, tanto las variables como las funciones son objetos. Entre las funciones nativas que proporciona Python, se encuentran aquellas que permiten examinar las propiedades de un objeto en **tiempo de ejecución**.

+++

#### La función ``type()``
La función ``type()`` interroga el tipo del valor de un objeto.

```{code-cell} ipython3
a = 1
type(a)      # Devuelve el tipo de datos del valor que representa a
```

```{code-cell} ipython3
a = 1.1
type(a)      # Devuelve el tipo de datos del valor que representa a
```

```{code-cell} ipython3
a = 'Hola'
type(a)      # Devuelve el tipo de datos del valor que representa a
```

#### La función ``id()`` y el operador ``is``
La función nativa ``id()`` muestra por pantalla un entero, que es **único** para cada objeto almacenado en memoria. Es equivalente a su dirección de memoria.

```{code-cell} ipython3
x = 3.5
id(x)
```

```{code-cell} ipython3
y = x
id(y)
```

Nótese que la función ``id()`` devuelve la identificación del objeto ``float`` de valor ``3.5``. Las variables ``x`` e ``y`` son meras etiquetas ligadas a ese objeto.

El operador ``is`` permite determinar si dos variables están ligadas al mismo objeto.

```{code-cell} ipython3
x is y
```

Nótese que la salida de la celda anterior es ``True``. Es un resultado lógico o booleano (en referencia al álgebra de G. Boole). El otro posible valor es ``False``.

```{code-cell} ipython3
x = 5.6
x is y
```

#### La función ``dir()``
La función nativa ``dir()`` muestra por pantalla todos los atributos, datos y métodos, utilizables con un **objeto**.

```{code-cell} ipython3
a = 1.1
dir(a)
```

***
<a id='El_operador_punto'></a>

+++

## El operador `.`
Para acceder a un atributo tipo dato o utilizar un método de un objeto, debe utilizarse el operador `.`.

Por ejemplo, los valores de tipo `complex` tienen, entre otros, dos atributos llamados `real` e `imag`, que permiten acceder de forma individual a la parte real e imaginaria del valor.

+++

#### Ejemplos con ``complex``

Por ejemplo, los valores de tipo `complex` tienen, entre otros, dos atributos llamados `real` e `imag`, que permiten acceder de forma individual a la parte real e imaginaria del valor.

```{code-cell} ipython3
a = 3.1 + 5.62j
a.real
```

```{code-cell} ipython3
a.imag
```

En el siguiente ejemplo, el método `.conjugate()` obtiene el complejo conjugado de `a`.

```{code-cell} ipython3
b = a.conjugate()
b
```

#### Ejemplos con ``str``
El método `.upper()` actúa sobre el valor de una variable de tipo `str` transformando todos sus caracteres a mayúsculas.

```{code-cell} ipython3
a = "cadena para probar métodos"
a.upper()
```

Obsérvese que un método es conceptualmente similar a una función en el sentido de que ejecuta un código que devuelve algún valor. A diferencia de una función convencional, el método está asociado al objeto sobre el que actúa. 

Hay muchos otros métodos asociados a las cadenas: para una referencia completa ir a: https://docs.python.org/3/library/stdtypes.html#string-methods.

Algunos métodos útiles:
```python
str.lower()       # convierte a minúsculas los caracteres de la cadena.
str.capitalize()  # hace que el primer carácter de la cadena esté en mayúscula.
str.title()       # hace que todas las palabras comiencen con caracteres en mayúscula.
str.isalnum()     # devuelve `True` si todos los caracteres de la cadena son alfanuméricos.
str.isdigit()     # devuelve `True` si todos los caracteres son dígitos.
```

```{code-cell} ipython3
cad = "1232"
cad.isdigit()
```

#### Ejemplos para ``float``
Para valores numéricos también disponemos de métodos. Por ejemplo, el método `.as_integer_ratio()` de los `float` devuelve la representación fraccionaria del número real.

```{code-cell} ipython3
a = 1.5
a.as_integer_ratio()
```

El método `.is_integer()` devuelve ``True`` si el valor no tiene parte fraccionaria.

```{code-cell} ipython3
a = 2.0
a.is_integer()
```

Tanto en el entorno **Jupyter Notebook** como en **Spyder**, pulsando el tabulador después de escribir
`variable.` se muestra un menú desplegable que nos muestra los atributos y métodos asociados al tipo de objeto al que pertenece `variable`.

+++

***
<a id='Conversiones_de_tipos'></a>

+++

## Conversiones de tipos
Para determinados tipos, es posible realizar **conversiones** entre ellos. Existen diversas funciones de conversión de tipo: ``float()``, ``int()``, ``complex()``, etc.

```{code-cell} ipython3
b = float(a) # 
type(b)
```

Estos tipos de funciones son muy versátiles: pueden recibir como argumentos diferentes valores *representando* distintos tipos de datos. Son incluso capaces de convertir una cadena de caracteres, que puede representar un valor (entero en el ejemplo), al valor numérico equivalente.

```{code-cell} ipython3
a = "1221"   # Se obtiene el entero representado en la cadena, si es posible
int(a)
```

Si la conversión no es posible, se genera una **excepción**.

```{code-cell} ipython3
:tags: [raises-exception]

a = "12.21"   # Se obtiene el entero representado en la cadena, si es posible
int(a)
```

La función `str()` por su parte, recibe como argumento un valor y lo convierte a su representación como cadena de caracteres.

```{code-cell} ipython3
str(1.e-12)
```
