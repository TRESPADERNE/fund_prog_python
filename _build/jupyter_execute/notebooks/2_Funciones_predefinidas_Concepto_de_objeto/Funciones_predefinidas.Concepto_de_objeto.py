#!/usr/bin/env python
# coding: utf-8

# # Funciones nativas. Concepto de objeto.
# **Autores**: Rogelio Mazaeda Echevarría, Félix Miguel Trespaderne.   

# ## Contenidos
# [Funciones nativas](#Funciones_nativas)<br>
# [Funciones definidas en módulos](#Funciones_definidas_en_módulos)<br>
# [(*) _Introspección y conversiones de tipo_](#Introspección_y_conversiones_de_tipo)<br>
# [(*) _Introducción al concepto de objeto: atributos y métodos_](#Introducción_al_concepto_de_objeto:_atributos_y_métodos)

# ***
# <a id='Funciones_nativas'></a>

# ## Funciones nativas
# 
# Las expresiones combinan valores y operadores para obtener un nuevo valor. No obstante, si nos concentramos por el momento en la aritmética, existen operaciones matemáticas a las que usualmente tenemos acceso en una calculadora comercial convencional, como la aplicación de funciones matemáticas comunes, tales como raíz cuadrada, potencias, funciones trigonométricas, logaritmos, etc. entre muchas otras.
# 
# Python, al igual que otros lenguajes de programación, tiene también el concepto de **función**, cuyo significado no coincide de forma exacta con la definición matemática, pero que puede ser utilizada para dar cuerpo a estas últimas.
# 
# Las funciones de Python serán objeto de un estudio más detallado posteriormente, donde aprenderemos a programar nuestras propias funciones. De momento, sin embargo, iremos introduciendo las **funciones nativas** (**built-in functions**) que Python pone a nuestra disposición. 
# 
# Un ejemplo de función numérica que está siempre a nuestra disposición es `abs()`, que se utiliza para hallar el valor absoluto de valores enteros o reales y el módulo de números complejos. 
# 
# Nótese en la celda siguiente el uso de **comentarios**: líneas de texto libre, que comienzan con el carácter `#` y que se extienden hasta el final de la línea. Estos comentarios son ignorados por el intérprete, pero son útiles para aclarar el funcionamiento del código.
# > La regla de estilo **PEP 8** sugiere dejar un espacio en blanco tras `#`

# In[1]:


# Uso de la función abs()
abs(-1)


# In[2]:


# Las funciones pueden aparecer formando parte de expresiones más complejas. 
# ¿Puedes predecir el resultado de la siguiente expresión?
10**abs(2*3 - 7) + 5


# La expresión
# ```python
# 10**abs(2*3 - 7) + 5
# ```
# es interpretada por Python siguiendo las reglas de precedencia. Así, la potencia debe ser evaluada primero. Pero para hacerlo, el intérprete necesita primero obtener el valor absoluto de la subexpresión que está entre los paréntesis, los cuales forman parte de la sintaxis de la función. Los pasos serían:
# 1. Se evalúa la subexpresión `2*3 - 7`, obteniéndose el valor `-1`. Este valor es el **parámetro** que se **envía** a la función `abs()`.
# 2. La función `abs()` **devuelve** el valor absoluto de `-1`, es decir, `1` .
# 3. El valor devuelto `1` es el exponente de la base `10`. El resultado es `10`.
# 4. Al valor `10` se le suma el operando `5`.

# Otro ejemplo, es la función predefinida `round()`, que devuelve redondeada la expresión entre paréntesis al entero más cercano, `3` en el ejemplo:

# In[3]:


round(3.1)


# Las funciones en Python pueden diseñarse para recibir un número opcional de parámetros.
# Así, la función `round()` puede ser utilizada con dos parámetros: el primero sigue siendo el número real a redondear, pero el segundo es un entero que especifica el número de lugares decimales para el redondeo.

# In[4]:


# Prueba diferentes lugares decimales para el redondeo
round(3.14159, 3)


# Un elemento importante de la sintaxis de los lenguajes de programación es que admiten la **composición**:
# >Cualquier subexpresión que participe en una expresión puede ser sustituida por otra subexpresión equivalente, originando una expresión resultante que será también sintácticamente correcta. 
# 
# Esto incluye el uso de las funciones en las expresiones. Ya vimos antes que el valor del parámetro que se envía a una función puede ser el resultado de la evaluación de otra expresión. 
# 
# Por ejemplo:

# In[5]:


# ¿Cuál será el valor que resulta? ¿En que orden serán llamadas las funciones?
abs(round(3.5) - 10)


# Existen funciones predefinidas asociadas al trabajo con **cadenas de caracteres** (y de otras **secuencias**) que veremos a lo largo del curso. Por el ejemplo, la función `len()` devuelve un entero con el tamaño de la cadena, es decir, el número de caracteres que la forman, incluidos espacios en blanco, que son caracteres al fin y al cabo.

# In[6]:


len("hola mundo ")


# Funciones como `abs()`, `round()` o `len()` están predefinidas y directamente disponibles para el intérprete de Python. Existen otras muchas funciones en esta situación, que iremos viendo poco a poco. Una lista completa de las mismas puede ser consultada en https://docs.python.org/3/library/functions.html

# ***
# <a id='Funciones_definidas_en_módulos'></a>

# ## Funciones definidas en módulos
# Además de las funciones **nativas** del lenguaje existe muchas otras, útiles en diferentes campos, que están disponibles si se **importa** el **módulo** adecuado.
# 
# Una discusión completa del significado de los módulos, cómo trabajar con ellos y cómo crearlos se hará más adelante. Por ahora baste mencionar que mediante ellos podemos acceder a un conjunto suplementario de funciones. 
# 
# Una forma (**¡desaconsejada!**) de *importar* todas las funciones de un módulo es con la expresión:
# ```python
# from modulo import *
# 
# ```
# Por ejemplo, el modulo `math` contiene las habituales funciones matemáticas, `cos()`, `exp()`,`log()`, etc., funciones coincidentes con las de la biblioteca homónima del lenguaje C.
# 
# Un conjunto completo de las funciones del módulo `math` se encuentra en https://docs.python.org/3/library/math.html.

# In[7]:


# ¿Puedes predecir el resultado antes de ejecutarlo?
from math import * # Importamos el módulo math
log(exp(cos(0)))


# Aunque importar con la expresión `from modulo import *` puede resultar cómodo, lo cierto es que es totalmente desaconsejable. La razón es que diferentes módulos pueden contener identificadores coincidentes.
# 
# Por ejemplo, los módulos `math` y `cmath` (este último adaptado al cálculo con números complejos) tienen ambos una función para el cálculo de raíces cuadradas, `sqrt()`.
# 
# En el ejemplo siguiente, al importarse en segundo lugar el módulo `math` se **sobrescribe** la función `sqrt()` para complejos y el cálculo produce un **error en tiempo de ejecución** `ValueError`. ¡Se ha producido una **colisión** entre identificadores!
# 
# Nótese que el hecho de que se produzca este error es una buena noticia. Imaginad una **colisión** entre dos funciones con desempeños diferentes que no generen este tipo de error. ¡Tendríamos un **error semántico** de difícil detección!

# In[8]:


from cmath import *
from math import *

sqrt(-3)


# Si en la celda anterior cambiamos el orden de importación, el error desaparece. ¡Verifícalo! 
# 
# ¿Cuál es la manera de proceder? Veámoslo con el mismo ejemplo.

# In[ ]:


import cmath
import math

cmath.sqrt(-3)


# Ahora, para acceder a las funciones de cada módulo anteponemos su nombre seguido del operador `.`. 
# 
# Es cierto que el código resultante es más verboso, pero evitamos colisiones entre los identificadores de los objetos definidos en cada módulo. Estos identificadores constituyen el **espacio de nombres** de cada módulo.

# ***
# <a id='Introspección_y_conversiones_de_tipo'></a>

# ## (*) _Introspección y conversiones de tipo_
# 
# Las funciones disponibles en Python son de muy diversa naturaleza. Por ejemplo, hay funciones que permiten hacer **introspección** interrogando el tipo de los valores.

# In[ ]:


a = 1
type(a)      # Devuelve el tipo de datos del valor que representa a


# O **convertir** valores entre diferentes tipos siempre que esto sea posible.

# In[ ]:


b = float(a) # Existen funciones de conversión de tipo: float(), int (), bool(), complex()
type(b)


# Estos tipos de funciones son muy versátiles: pueden recibir como argumentos diferentes valores *representando* distintos tipos de datos. Son incluso capaces de convertir una cadena de caracteres, que puede representar un valor (entero en el ejemplo), al valor numérico equivalente.

# In[ ]:


a = "1221"   # Se obtiene el entero representado en la cadena, si es posible
int(a)


# La función `str()` por su parte, recibe como argumento un valor y lo convierte a su representación como cadena de caracteres.

# In[ ]:


str(1.e-12)


# Las cadenas de caracteres son *colecciones* de caracteres alfanuméricos. Veremos algunas de las diferentes formas de codificar estos caracteres a partir de valores numéricos (**ASCII**, **UNICODE**). Las funciones `ord()` y `chr()` brindan respectivamente el código que representa una letra determinada y el carácter representado por un código numérico. Las mayúsculas y las minúsculas tienen códigos diferentes.

# In[ ]:


ord('a')


# In[ ]:


chr(65)


# ***
# <a id='Introducción_al_concepto_de_objeto:_atributos_y_métodos'></a>

# ## (*) _Introducción al concepto de objeto: atributos y métodos_
# 
# Tanto las variables como las funciones son **objetos** en Python. 
# 
# Un **objeto** es una entidad conformada por:
# 
# * **Atributos**, conjunto de datos que determinan el **estado** del objeto, en definitiva, el **valor** del objeto.
# * **Métodos**, funciones específicas que pueden ser aplicadas a los **atributos** del objeto para obtener información acerca de este o, en ocasiones, para modificarlo.
# 
# Todo **objeto** en Python tiene una **identidad**, un **tipo** y un **valor**.
# 
# #### Identidad
# La **identidad** de un objeto nunca cambia una vez que ha sido creado. Puede asimilarse como su dirección en memoria.
# * mediante el operador nativo `is` podemos comparar la identidad de dos objetos, es decir, si dos variables referencian al mismo objeto.
# * la función nativa `id()` devuelve un entero que representa su identidad
# 
# #### Tipo
# El **tipo** determina los posibles valores y operadores que ese objeto soporta.
# * la función nativa `type()` devuelve el tipo de un objeto
# 
# Al igual que la identidad, el tipo de un objeto es inalterable.
# 
# #### Valor
# El **valor** de un objeto puede o no variar en función del tipo. Los objetos cuyo valor puede cambiar son objetos **mutables** mientras que los que no pueden ser alterados son objetos **inmutables**. Por ejemplo, los tipos de datos `int`, `float`, `bool` y `str` son inmutables. Más adelante veremos tipos como las **listas** y los **diccionarios** que son mutables.

# ###  **_Variables_** de Python en memoria
# 
# El tratamiento que _internamente_ reciben las **variables** de Python difiere del que reciben en otros lenguajes más convencionales como el C/C++. 

# ![traza1.jpg](attachment:traza1.jpg)

# En lenguajes como el C/C++, en los que el tipo de cada variable se declara antes de usarlo, los nombres de estas últimas hacen referencia a **localizaciones** o **bloques** de memoria **diferentes** en el ordenador. Cada uno de estos **bloques** tiene la _capacidad_ de almacenar el **tipo** de dato declarado. De manera que, en el ejemplo, `x` e `y` representan dos conjuntos de celdas diferentes. La primera asignación, hace que en el **bloque** correspondiente a `x` se almacene un `1` y en la segunda asignación, que el contenido de `x` (un `1` como se ha visto) sea **colocado** en las celdas de memoria que representan a `y`.
# 
# En el caso de Python, la interpretación es diferente. Python es un lenguaje de **_tipado dinámico_** en que no hay que declarar el tipo de las variables antes de usarlas. De manera que, cuando se realiza la primera asignación, se deposita el valor `1` en algún **bloque** de memoria del ordenador, y se le asigna a ese valor el **nombre** o **identificador** `x`. Cuando se realiza la siguiente asignación, se le asigna un nuevo nombre (un **alias**), en este caso `y`, al **mismo bloque** de memoria donde estaba colocado el `1`.
# 
# En lenguajes como el C/C++, cada **variable** identifica una localización de memoria diferente que puede **modificar** su contenido: de ahí el nombre de variable.
# 
# En Python los **nombres**  son como **etiquetas** que puede hacer referencia al mismo valor en la misma localización de memoria. En cualquier caso, también nos referimos a estos como variables.

# ![traza2.jpg](attachment:traza2.jpg)

# Si ahora, en el código de C/C++ se ejecuta la siguiente asignación, simplemente se **modifica** el valor de la **variable** `x` que ahora pasará a contener un `2`.
# 
# En el caso de Python, como los enteros (y otros valores simples `float`, `bool`, etc) se consideran **inmutables**, cuando se hace la asignación ```x = 2```, en realidad se está creando, en otra localización de memoria, espacio para almacenar el nuevo valor `2`, haciendo ahora que la _etiqueta_ `x`, que antes estaba _unida_ al valor `1`, se refiera ahora al `2`. Finalmente, se tiene la situación que se muestra en el esquema previo.
# 
# De manera que, aunque el mecanismo de funcionamiento de la memoria en Python es diferente, para el caso de los tipos **inmutables** el resultado neto, es el mismo.

# In[ ]:


# Tras asignar y = x ambos identificadores referencian al mismo objeto
x = 3
y = x
print(x is y)


# In[ ]:


# El objeto 1, un entero, es inmutable
# El identificador x referencia en cada momento a dos objetos distintos
x = 1
print(id(x))

x += 1 # Se crea un nuevo objeto de valor 2
print(id(x))


# Incluso los **valores** aparentemente más simples son objetos en Python. La función nativa `dir()` , al sacar por pantalla todos los atributos y métodos de la **clase** a la que pertenece un **objeto**, nos revela este hecho.

# In[3]:


a = 1
dir(a)


# In[5]:


st = "Una cadena"
dir(st)


# ### El operador `.`
# Para acceder a un atributo o utilizar un método de un objeto debe utilizarse el operador `.`.
# 
# Por ejemplo, los valores de tipo `complex` tienen, entre otros, dos atributos llamados `real` e `imag`, que permiten acceder de forma individual a la parte real e imaginaria del valor.

# In[ ]:


a = 3.1 + 5.62j
a.real


# In[ ]:


a.imag


# En el siguiente ejemplo, el método `.conjugate()` obtiene el complejo conjugado de `a`.

# In[ ]:


b = a.conjugate()
b


# El método `.upper()` actúa sobre el valor de una variable de tipo `str` transformando todos sus caracteres a mayúsculas.

# In[ ]:


a = "cadena para probar métodos"
a.upper()


# Obsérvese que un método es conceptualmente similar a una función en el sentido de que ejecuta un código que devuelve algún valor. A diferencia de una función convencional, el método está asociado al objeto sobre el que actúa. 
# 
# Hay muchos otros métodos asociados a las cadenas: para una referencia completa ir a: https://docs.python.org/3/library/stdtypes.html#string-methods.
# 
# Algunos métodos útiles:
# ```python
# str.lower()       # convierte a minúsculas los caracteres de la cadena.
# str.capitalize()  # hace que el primer carácter de la cadena esté en mayúscula.
# str.title()       # hace que todas las palabras comiencen con caracteres en mayúscula.
# str.isalnum()     # devuelve `True` si todos los caracteres de la cadena son alfanuméricos.
# str.isdigit()     # devuelve `True` si todos los caracteres son dígitos.
# ```

# In[ ]:


cad = "1232"
cad.isdigit()


# Para valores numéricos también disponemos de métodos. Por ejemplo, el método `.as_integer_ratio()` de los `float` devuelve la representación fraccionaria del número real.

# In[ ]:


a = 1.5
a.as_integer_ratio()


# Tanto en el entorno **Jupyter Notebook** como en **Spyder**, pulsando el tabulador después de escribir
# `variable.` se muestra un menú desplegable que nos muestra los atributos y métodos asociados al tipo de objeto al que pertenece `variable`.
