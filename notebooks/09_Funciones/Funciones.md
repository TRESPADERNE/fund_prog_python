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

+++ {"hideCode": false, "hidePrompt": false}

# Funciones

+++ {"hideCode": false, "hidePrompt": false}

[Introducción](#Introducción)<br>
[Definición de funciones](#Definición_de_funciones)<br>
[Tipos de funciones según sus parámetros de entrada y valores devueltos](#Tipos_de_funciones_según_sus_parámetros_de_entrada_y_valores_devueltos)<br>
[Funciones y tratamiento de excepciones](#Funciones_excepciones)<br>
[Proceso de desarrollo de un programa](#Proceso_desarrollo_programa)

+++ {"hideCode": false, "hidePrompt": false}

***
<a id='Introducción'></a>

+++ {"hideCode": false, "hidePrompt": false}

## Introducción

En los temas previos ya hemos tenido oportunidad de trabajar con **funciones**. En este tema aprenderemos a definir y utilizar funciones **creadas por nosotros**.

A lo largo del tiempo y en diferentes lenguajes el concepto de función aparece definido también por otros nombres: **subprograma**, **subrutina** o **procedimiento** son los más habituales y con diferentes matices denotan lo mismo.
>Una función es un **conjunto de instrucciones** al que se asigna un nombre, opcionalmente parámetros de entrada y de salida, y que puede ser **llamada** desde otras partes de un programa para realizar una tarea concreta.

+++ {"hideCode": false, "hidePrompt": false}

### La necesidad de las funciones

Los lenguajes de programación utilizan los recursos que brinda el _hardware_ del ordenador: la capacidad de codificar diferentes tipos de datos y la posibilidad de realizar sobre ellos operaciones aritméticas y lógicas. 

Las operaciones que el ordenador brinda de forma nativa, son bastante elementales y no van mucho más allá de:
* la capacidad de realizar sumas, restas, multiplicaciones y divisiones, etc.
* controlar el flujo del programa modificando la ejecución secuencial de las sentencias mediante la utilización de condicionales y bucles.

De manera que la realización de todo el resto de complicadas operaciones que sabemos que son capaces de realizar los programas de ordenador deben ser *construidas* a partir de esas operaciones básicas. 

Cuando hemos utilizado los operadores más sencillos en Python (suma, resta, etc.), el intérprete *traduce* los comandos de alto nivel dados por el programador y usa, casi directamente, las funcionalidades del *hardware*. 

Por tanto, a la hora de hacer operaciones más complejas, estas tienen que ser creadas a partir de esos bloques elementales implementando procedimientos más elaborados. Python y otros lenguajes brindan la posibilidad de agrupar estos bloques de instrucciones en forma de una **función**, para su posterior invocación de forma sencilla.

+++ {"hideCode": false, "hidePrompt": false}

#### Un ejemplo usando funciones de biblioteca

La **función** es entonces el recurso que el lenguaje de programación brinda para implementar esos subprogramas. Ya hemos utilizado muchas funciones, algunas intrínsecas y otras disponibles en módulos como el módulo `math`.

Por ejemplo, supongamos que queremos determinar el siguiente cociente:
$$
\begin{align}
\\y & = \frac{1-{{sin(x/4)}{cos(x)} }^4}{1+cos(x)^2} \\
\end{align}
\notag
$$

El cálculo de $y$ se podría implementar en Python con un programa como el siguiente, que hace uso de las funciones trigonométricas `sin()` y `cos()` definidas en el módulo `math`:

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

# Desaconsejado usar import *, pero utilizado aquí para argumentar el uso de funciones
from math import *  

x = pi
y = (1 - sin(x/4)*cos(x)**4)/(1+cos(x)**2)
print(y)
```

+++ {"hideCode": false, "hidePrompt": false}

Se debe resaltar lo siguiente en el ejemplo anterior:

- **Claridad**
> Observad la similitud en el uso (que no equivalencia) para este caso concreto de las funciones en Python con el concepto matemático de función. La función **recibe** valores como argumentos y **devuelve** un valor que entonces participa en la evaluación del resto de la expresión.

- **Abstracción**
> Como *usuarios* de las funciones `sin()` y `cos()` no sabemos cómo están implementadas. Podríamos aventurar que es posible que la implementación de las mismas recurra a la expansión de series que converjan a las funciones requeridas, con una precisión alta pero finita. Pero el hecho cierto es que no lo sabemos, y tampoco nos interesa para utilizarlas: evidentemente hay que dar un *salto de fe* y confiar en que sean correctas dentro de los límites de la precisión que aseguran.

- **Reutilización**
> Hemos utilizado dos veces la función `cos()` y una el `sin()`. Podemos imaginar que utilizar más expresiones, usando estas funciones un número mayor de veces, no implicaría una dificultad mucho mayor.

Imaginemos, por el contrario, que las funciones no existieran. Y que cada vez que quisiéramos determinar el seno o coseno de un número, tuviésemos que programar los bucles y condicionales del algoritmo específico que determina el valor de estas funciones a partir de operaciones más básicas. Ciertamente, sería muy complicado resolver cualquier problema matemático sencillo. El código resultante sería enormemente difícil de entender. Por otra parte, si se decidiera cambiar la implementación del código, para utilizar otro algoritmo más preciso o eficiente, eso implicaría modificar todo el programa.

+++ {"hideCode": false, "hidePrompt": false}

Una vez visto el ejemplo, mostramos ahora la forma recomendada de usar funciones importadas de un módulo.

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

import math

x = math.pi
y = (1 - math.sin(x/4)*math.cos(x)**4)/(1+math.cos(x)**2)
print(y)
```

+++ {"hideCode": false, "hidePrompt": false}

***
<a id='Ventajas_del_uso_de_funciones'></a>

+++ {"hideCode": false, "hidePrompt": false}

### Ventajas del uso de funciones

Las funciones brindan dos beneficios importantes de los que se pueden derivar muchos otros:
- **Estructura**: Es un recurso que permite descomponer una tarea compleja en varias subtareas de menor entidad, que puedan ser abordables con mayores garantías de éxito.
- **Abstracción**: Las funciones ocultan detalles tras una **interfaz pública** bien definida. Se hace abstracción de los detalles de implementación y lo que interesa únicamente son los valores de entrada que se le suministran y los resultados que devuelve. 


A partir de estas dos características básicas, se derivan el resto de las ventajas que brinda el uso de las funciones:

- Permiten **reutilizar código** sin tener que reescribirlo cada vez.
- Permite el **encapsulamiento** del código de la función. Así, por ejemplo, una vez dado por válido el código interno de una función, los errores de un programa no serán imputables a la implementación interna de la función.
- La implementación interna puede cambiar sin que el programador que use esas funciones tenga que preocuparse de ello.
- Hace que el código resultante sea más claro y mantenible.
- Las funciones brindan el mecanismo para dividir un problema grande en subproblemas pequeños, acotando la interacción entre los mismos a los datos intercambiados a través de su interfaz pública. 
- Es el mecanismo ideal para permitir la colaboración entre varios programadores: una vez puestos de acuerdo en la interfaz, cada cual tiene la libertad de programar la solución a los subproblemas parciales sin temor a que le afecte lo hecho por otros programadores (siempre que el resultado brindado sea el correcto).

+++ {"hideCode": false, "hidePrompt": false}

### Pautas de diseño de una función
Las  características que deben prevalecer a la hora de diseñar una función son aquellas que refuerzan el hecho de que las funciones son abstracciones.

Una función como abstracción debe centrarse en 3 propiedades:
* Su **dominio**, conjunto de valores que pueden tomar sus argumentos de entrada.
* Su **rango**, conjunto de valores que puede devolver.
* Su **propósito**, la relación existente entre los valores de entrada y los de salida, así como los posibles efectos colaterales que puedan existir.

Cómo se logran las salidas a partir de las entradas queda oculto, ese el mecanismo de la abstracción.

Para lograr reforzar el mecanismo de abstracción de una función hay algunas pautas que son de ayuda:
1. Cada función debe tener un único propósito. Es el **principio de responsabilidad única**.
    * El objetivo perseguido con la función debería ser fácilmente identificado con un nombre corto.
    * Si una función hace múltiples tareas de forma consecutiva, debería rehacerse en múltiples funciones.
2. **No te repitas** (**DRY**, **Don't repeat yourself**).
    * Si un fragmento de código aparece varias veces repetido, es una buena oportunidad para darlo un nombre e invocarlo múltiples veces.
3. Las funciones deben ser **generales**.
    * No tiene sentido, por ejemplo, definir una función específica para elevar un número a la quinta, cuando podemos definir con carácter general, una función que eleve un número a cualquier exponente.

+++ {"hideCode": false, "hidePrompt": false}

***
<a id='Definición_de_funciones'></a>

+++ {"hideCode": false, "hidePrompt": false}

## Definición de funciones
Al acto de utilizar una función, tal y como hemos venido haciendo hasta ahora con las funciones nativas (*built-in*) y también con las de biblioteca, se le conoce con el nombre de _llamar_ o _invocar_ a la función.

Aprenderemos a continuación cómo definir nuestras propias funciones con algunos ejemplos sencillos.

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

# Primero definimos la función, especificando su nombre y sus parámetros
def area_circulo(r):
    area = 3.1415*r**2
    return area


diametro = 10
area = area_circulo(diametro/2)
print("Área del círculo de diámetro {} es {}.".format(diametro, area))
```

+++ {"hideCode": false, "hidePrompt": false}

![definicion_funcion.jpg](img/definicion_funcion.jpg)

+++ {"hideCode": false, "hidePrompt": false}

Observe en lo anterior los dos momentos del trabajo con las funciones, la **definición** y la **llamada**: 

* **Definición**: 
    ```python
    def area_circulo(r):
        '''Función que recibe el radio del círculo y calcula su área'''

        area = 3.1415*r**2
        return area
    ```
  Debe aparecer **antes de la primera llamada** a la función definida y está formada por dos partes, el **encabezado** y el **cuerpo**:

    - **Encabezado**: 
      ```python
      def area_circulo(r): 
      ```  
        Se utiliza la palabra reservada `def` seguida del identificador que da **nombre a la función**, `area_circulo` en el ejemplo. Le sigue entre paréntesis (obligatorios) la lista de **parámetros formales**, que puede estar vacía. En el ejemplo, consta de un sólo parámetro formal al que hemos identificado dentro de la definición de la función con el nombre `r`. 
    
        Note que, al definir la función, todavía no se ejecuta el código que ella representa, aunque aparezca primero dentro de la secuencia del programa. 
    - **Cuerpo**:
      ```python
         area = 3.1415*r**2
         return area
      ```   
        Después del encabezado, se tiene el cuerpo de la función. Se debe notar que, de nuevo, Python exige el *sangrado* apropiado para identificar el cuerpo de la función.
         - La primera sentencia **asigna** a la variable `area` el resultado de evaluar la expresión a su derecha
         - La segunda sentencia utiliza la palabra reservada `return` para **devolver** el contenido de `area` al código que haya invocado a la función.

    Es importante entender que `area` dentro de la definición de la función da nombre a una **variable local** que solo está definida y **accesible** dentro de la función `area_circulo()`. El identificador `r` igualmente sólo está definido dentro de la función.
    
* **Llamada(s)**: 
    ```python
    area = area_circulo(diametro/2)
    ```
    Se realiza escribiendo el nombre de la función, seguido obligatoriamente de los paréntesis con los **parámetros reales** (en este caso uno) que se le *pasarán* a la misma. Aquí el parámetro real se obtiene evaluando la expresión indicada, `diametro/2`.

+++ {"hideCode": false, "hidePrompt": false}

A tener en cuenta:
- Antes de llamar a una función, esta debe haber sido **definida** previamente en el programa.
- La primera sentencia _útil_ que se ejecuta es la primera sentencia del **programa principal**. Programa principal es el conjunto de todas las sentencias que **no** están incluidas dentro del cuerpo de ninguna función.
- Si la función tiene parámetros de entrada, a la hora de llamar a la función se calculan los valores de los parámetros reales, evaluando las expresiones correspondientes (en el ejemplo se evalúa `diametro/2`). El valor del parámetro real resulta asociado al parámetro formal o argumento de la función (en este caso `r`).

+++ {"hideCode": true, "hidePrompt": true}

En el siguiente ejemplo, que calcula el área de un cilindro, vemos una **reutilización** de la función `area_circulo(r)`. Hemos añadido entre triples comillas,`'''texto'''`, un comentario para **documentar** brevemente el objeto de la función.

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false
:tags: [raises-exception, remove-output]

def area_circulo(r):
    '''Función que recibe el radio del círculo y calcula su área'''

    area = 3.1415*r**2
    return area


# El estilo PEP 8 recomienza dejar dos líneas en blanco después de una función
# Ahora comienza el programa principal: la primera línea ejecutable es diametro = 10

# Programa principal
radio = float(input("Diga el radio: "))
altura = float(input("Diga la altura: "))

area_cilindro = 2*area_circulo(radio) + 2*3.1415*radio*altura

print('El área lateral de un cilindro de radio {} y altura {} es {}.'.
      format(radio, altura, area_cilindro))
```

+++ {"hideCode": false, "hidePrompt": false}

Las sentencias que se ejecutarán primero de forma secuencial corresponden al **programa principal**:
* la asignación a las variables `radio` y  `altura` de los valores que el usuario introduzca por teclado
* la evaluación de la expresión que se asigna a una nueva variable, `area_cilindro`. Como la función `area_circulo()` devuelve un valor, la llamada a dicha función puede participar de la expresión en la que se calcula el área lateral del cilindro. Nótese que esta forma de utilizar la función que acabamos de definir, no difiere de lo ya visto en temas anteriores o del ejemplo del inicio de este documento con las funciones de biblioteca `cos()` y `sin()`.
* la salida por pantalla de los resultados

Al evaluar la expresión en la que aparece la llamada a `area_circulo()`, se procede siguiendo las reglas de precedencia de los operadores implicados. Primero, cuando se intenta realizar el primer producto, el intérprete de Python *comprende* que necesita antes evaluar la función `area_circulo()`, con lo que se detiene la evaluación de la expresión para *invocar* a la función, asociando el contenido de la variable `radio` (argumento real) al parámetro formal `r` de la definición de la función. Tras terminar la ejecución, la función devuelve el valor del área del circulo contenida en la variable local `area`, y dicho valor es recibido en el programa principal para proceder con la evaluación del resto de la expresión.

Nótese que `area_circulo()` tiene un comportamiento similar a las funciones matemáticas: a cada valor del dominio de definición (cada valor del parámetro formal `r`) le corresponde un único valor de la imagen (la salida que se logra mediante la sentencia `return`) y que además este valor siempre es el mismo.

+++ {"hideCode": false, "hidePrompt": false}

### Principios de responsabilidad única y de generalidad
Desde el punto de vista de la ingeniería del software es deseable que una función realice una única labor, lo que podría englobarse dentro de lo que se conoce como **principio de responsabilidad única**.

Veamos un ejemplo de diseño de función desafortunado:

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

def area_circulo_desafortunado(r):
    area = 3.1415*r**2
    print("Área del círculo de radio {} es {}.".format(r, area))
    return area
```

+++ {"hideCode": false, "hidePrompt": false}

Esta función tiene dos responsabilidades: calcular el área de un círculo e imprimir su valor por pantalla.

A la hora de programar funciones, se debe buscar que están sean lo más generales posible, de forma que puedan ser reusadas en diferentes circunstancias. La función anterior no es muy flexible, puesto que siempre *imprime* en pantalla el resultado y, probablemente, no en todas las ocasiones ese es el comportamiento que se desea.

Por tanto, desde otro punto de vista, violaría un **principio de generalidad**: no en todos los casos en que se quiera calcular el área del círculo, se desea imprimir el resultado por pantalla. Más bien lo contrario.

+++ {"hideCode": false, "hidePrompt": false}

***
<a id='Tipos_de_funciones_según_sus_parámetros_de_entrada_y_valores_devueltos'></a>

+++ {"hideCode": false, "hidePrompt": false}

## Tipos de funciones según sus parámetros de entrada y valores devueltos
### Funciones sin parámetros de entrada

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

def intro():
    print('Este código sólo imprime este mensaje.')

    
intro()
intro()
```

+++ {"hideCode": false, "hidePrompt": false}

Las funciones pueden carecer de parámetros de entrada. Observe que el único objetivo en este caso es sacar un aviso por pantalla.

Pueden existir una función trivial, _que no hace nada_.

```python
def funcion():
    pass  # TODO: completar más tarde
```
En todo caso, los paréntesis deben ser obligatoriamente utilizados tanto en la definición como en cada una de las llamadas a la función.

#### La sentencia ``pass``
La palabra clave ``pass`` indica algo así como no hacer nada. Suele utilizarse en ocasiones para crear la estructura de un programa sin que sea necesario tener completado todo su código.

+++ {"hideCode": false, "hidePrompt": false}

### Funciones que no devuelven valores mediante `return`

El caso del ejemplo anterior, también ejemplifica a las funciones que no contienen la sentencia `return`.
Este tipo de funciones, al ser utilizadas incorrectamente en contextos en que se espera un valor devuelto (al realizar composición de funciones o en sentencias de asignación), _devuelven_ el valor especial ```None``` que indica la ausencia de un valor válido.

Por ejemplo:

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

a = intro()
print(a)
```

+++ {"hideCode": false, "hidePrompt": false}

### Funciones con más de un parámetro

Las funciones pueden tener más de un parámetro formal. Tomando como referencia el ejemplo ya visto, definamos una función que reciba el radio y la altura de un cilindro y devuelva su área lateral.

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

# Primero definimos la función, especificando su nombre y sus parámetros
def area_cilindro(r, h):
    '''Función que recibe el radio y la altura de un cilindro y calcula su área lateral'''
    
    pi = 3.14159
    area = 2*pi*r**2 + 2*pi*r*h
    return area


area_c = area_cilindro(1, 4.5)
print('El área lateral del cilindro es {}.'.format(area_c))
```

+++ {"hideCode": false, "hidePrompt": false}

Note que los parámetros formales de ```area_cilindro()``` ahora son dos, representando el radio (```r```) y la altura (```h```).

Obsérvese la **correspondencia posicional** entre los parámetros formales y los reales: la constante literal `1` será copiada en el primer parámetro formal `r` y la constante `4.5` en el segundo `h`.

+++ {"hideCode": false, "hidePrompt": false}

### Funciones que devuelven más de un parámetro

En Python, las funciones pueden devolver mediante la sentencia ```return``` un número arbitrario de valores separados por coma, es decir, **tuplas**. Esta característica es una potente característica del lenguaje que lo diferencia de otros que no lo poseen de forma directa, como el C/C++.

Por ejemplo:

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

def min_max(lista):
    '''Devuelve el mínimo y el máximo de la lista que recibe como argmento'''
    
    mn = mx = lista[0]
    for elem in lista[1:]:  #[1:] evita comparar con el índice 0
        if mn > elem:
            mn = elem
        elif mx < elem:
            mx = elem
    return mn, mx  # Devolvemos una tupla


lista_prueba = [1, 10, 2, -3, 6, 8]

mn, mx = min_max(lista_prueba)  # Desempaquetado de la tupla

print('Los valores extremos de la lista {} son:\nMin: {} Max: {}'.format(lista_prueba, mn, mx))
```

+++ {"hideCode": false, "hidePrompt": false}

Observe que en el ejemplo anterior, el parámetro que espera la función ```min_max()``` es de tipo lista. Este ejemplo, además, ilustra bien el hecho de que las funciones deben ser entendidas como subprogramas, capaces de utilizar todas las posibilidades vistas: definir sus propias variables, utilizar estructuras de control de flujo como condicionales y bucles, etc.

La sentencia ```return``` devuelve el mínimo y máximo valor de la misma, creando una **tupla**.

En la línea en que se realiza la llamada, se asigna el resultado a dos variables, **desempaquetando** la tupla.

+++ {"hideCode": false, "hidePrompt": false}

### Especificando el nombre de los parámetros
Python permite especificar los nombres de los parámetros formales a la hora de invocar a la función.

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

area_c = area_cilindro(1, h=4.5)
print("El área lateral del cilindro", area_c)
```

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

area_c = area_cilindro(r=1, h=4.5)
print("El área lateral del cilindro", area_c)
```

+++ {"hideCode": false, "hidePrompt": false}

Por supuesto, no se permite que un parámetro que no tenga nombre, **argumento posicional**, esté a la derecha de un argumento con nombre.

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false
:tags: [raises-exception]

area_c = area_cilindro(r=1, 4.5)
print("El área lateral del cilindro", area_c)
```

+++ {"hideCode": false, "hidePrompt": false}

Poder especificar nombres permite que los parámetros reales pueden ser enviados a la función en cualquier orden.

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

area_c = area_cilindro(h=4.5, r=1)
print("El área lateral del cilindro", area_c)
```

+++ {"hideCode": false, "hidePrompt": false}

### Parámetros con valores por defecto
En ocasiones resulta útil definir funciones para las que uno o varios parámetros tengan valores por defecto.

Supongamos, por ejemplo, que hacemos una función para garantizar que el valor que se pasa como argumento está entre dos límites dados: 
* si lo está, devuelve el valor tal cual.
* si no lo está, devuelve el límite superior o inferior, según el caso. 

Se sabe además que, en la aplicación de que se trata, el rango de valores que interesa normalmente suele ser el [0,1]. Una implementación posible de dicha función es la que se muestra:

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

def limita(valor, inf=0.0, sup=1.):
    '''Devuelve valor si inf < valor < sup.
    Si valor < inf devuelve inf.
    Si valor > sup devuel sup'''
    
    if inf <= valor <= sup:
        return valor
    elif valor > sup:
        return sup
    else:
        return inf

valor = 3.
# con límites por defecto
print('Valor {} limitado en el rango por defecto [0.0, 1.0]: {}'.format(valor, limita(valor)))

# con un límite cambiado: inf -> -1.
print('Valor {} limitado en el rango [-1.0, 1.0]: {}'.format(valor, limita(valor, -1.)))

# con un límite cambiado: sup -> 5.
print('Valor {} limitado en el rango [0.0, 5.0]: {}'.format(valor, limita(valor, sup=5.)))

# con los dos límites cambiados: inf -> -1., sup -> 5.
print('Valor {} limitado en el rango [-1.0, 5.0]: {}'.format(valor, limita(valor, -1., 5.)))
```

+++ {"hideCode": false, "hidePrompt": false}

Observe que, en el encabezado de la definición de la función, a los parámetros formales `inf`y `sup` se les asignan respectivamente los valores `0.0` y `1.0`. Esto significa que, si esos parámetros no son utilizados (no se les pasa un valor o parámetro real) durante la llamada a la función, se utilizarán en el cuerpo de la misma esos valores por defecto.

En la tercera llamada a la función, se requiere cambiar el límite superior solamente. Para estos casos, se puede utilizar una llamada a función que utiliza, no la posición del argumento como criterio de emparejamiento de los parámetros reales a formales, sino utilizar directamente el nombre del parámetro formal y el signo ```=``` para pasar el parámetro real. De no hacerlo así, y utilizar el paso de parámetro posicional, habría que haber utilizado una llamada a función como la que se muestra a continuación, perdiendo la ventaja de los parámetros por defecto:
```python
limita(valor, 0, 5)
```

+++ {"hideCode": false, "hidePrompt": false}

***
<a id='Funciones_excepciones'></a>

+++ {"hideCode": false, "hidePrompt": false}

## Funciones y tratamiento de excepciones

El **tratamiento estructurado de excepciones** y el enfoque **EAFP** (**Easier to Ask Forgiveness than Permission**), visto con anterioridad, alcanza su mayor utilidad cuando es aplicado conjuntamente con las funciones.

Veamos un ejemplo que implementa una función clónica del método `index()` de las listas.

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

# Función clónica del método index() de las listas
def indice(lista, valor):
    for i, x in enumerate(lista):
        if x == valor:
            return i
    raise ValueError('{} is not in list.'.format(valor))


lista = [-5, 1, 3, 4, 12, 21, 23, 34, 43, 123]
try:
    valor = 0
    print('{} está en la posición {} de la lista {}.'.format(valor, indice(lista, valor), lista))
except ValueError as error:
    print(error)

# Usando el método index()
try:
    valor = 0
    print('{} está en la posición {} de la lista {}.'.format(valor, lista.index(valor), lista))
except ValueError as error:
    print(error)
```

+++ {"hideCode": false, "hidePrompt": false}

La función `indice()` utiliza el mecanismo de excepciones para comunicar la existencia de un error que lanza una excepción `ValueError`, utilizando la sentencia `raise`. Esta excepción será manejada por el primer bloque `try: ... except:` que englobe la llamada a la función.

Nótese que una excepción termina inmediatamente el **hilo de ejecución** de la función.

Veamos un ejemplo en el que dividimos valor por valor dos listas. La idea es que si un valor de la lista *denominador* es nulo, asignemos el valor **Not a number** `nan`. 

Para el resto de excepciones:
* Las listas tienen tamaños diferentes
* Datos incompatibles entre sí

será el usuario de la función quien deba manejarlas:

```{code-cell} ipython3
:hideCode: false
:hidePrompt: false

# Función que divide valor por valor dos listas
def divide_dos_listas_entre_si(lista_num, lista_den):
    lista_coc = []
    for i in range(len(lista_num)):
        try:
            lista_coc.append(lista_num[i]/lista_den[i])
        except ZeroDivisionError:
            lista_coc.append(float('nan'))            
    return lista_coc


lista_num = [-5, 1, 3, 4, 12, 21, 23, 34, 43, 123]
lista_den_1 = [1]
lista_den_2 = [-5, 0, 'a', 4, 12, 21, 23, 34, 43, 123]
lista_den_3 = [-5, 0, 3, 4, 12, 21, 23, 34, 43, 123]

# Probamos dividir lista_num entre las tres listas siguientes, capturan las excepciones
try:
    print(divide_dos_listas_entre_si(lista_num, lista_den_1))
except (IndexError, TypeError) as error:
    print(error)
    
try:
    print(divide_dos_listas_entre_si(lista_num, lista_den_2))
except (IndexError, TypeError) as error:
    print(error)
    
try:
    print(divide_dos_listas_entre_si(lista_num, lista_den_3))
except (IndexError, TypeError) as error:
    print(error)
```

+++ {"hideCode": false, "hidePrompt": false}

***
<a id='Proceso_desarrollo_programa'></a>

+++

### Proceso de desarrollo de un programa
Una vez conocido cómo definir funciones, tenemos muchas de las herramientas para acometer el **desarrollo de un programa**.

La programación es una tarea compleja a la que es mejor enfrentarse de manera **iterativa**. En los diferentes ejemplos de determinación de si un número es primo estamos viendo una prueba de ello.

Algunos pasos generales para hacerlo son:

1. Analizar cuidadosamente el problema a resolver. Utilizar en esta etapa **lápiz y papel** y la ayuda de **bosquejos**, entre otros recursos. Identificar los **datos de entrada** y cuales deben ser las **salidas** buscadas, para todas las posibles condiciones. Hacer cálculos paso a paso. Identificar **resultados intermedios** tratando de encontrar el algoritmo adecuado. 

2. Una vez se llega a una primera solución *en papel* razonable, se pasa a programar, utilizando los recursos provistos por el lenguaje. Como se ha dicho, ya se poseen los elementos imprescindibles para resolver cualquier problema solucionable por un ordenador. Por supuesto, en la medida que avance el curso, los recursos a nuestra disposición crecerán.

3. Puede darse el caso de que el programa no funcione para los **casos límites o especiales** (¿funciona para el 2, que es el primer posible primo?, etc.). Es importante identificar esos casos para poder testarlos y, en su caso, corregir los fallos. 

4. Por otro lado, es frecuente que en un primera esbozo del programa, se asuma que el usuario va a actuar de la forma prevista pero ¿qué pasa si no lo hace? ¿qué pasa si el número introducido es menor que dos o incluso negativo?. En ocasiones, el no prever todas estas posibles situaciones puede dar un resultado incorrecto o que el programa se interrumpa bruscamente por un error de ejecución. La solución de cada uno de los problemas detectados, implicará probablemente volver al paso 1 y la realización de modificaciones del código más o menos importantes, hasta que se llega a un código robusto y que funcione para todas las posibles entradas de datos. 

5. El primer programa seguramente no constituye la forma más **eficiente** (más rápida, por ejemplo) de resolver el problema. Un código que ya funciona correctamente puede estar sujeto a mejoras y optimizaciones. Aunque no se hará hincapié sobre este tema en un curso básico, en algunas ocasiones, sobre todo cuando se manipulan grandes volúmenes de datos, son importantes las consideraciones de cómo crece, por ejemplo, el tiempo de ejecución del programa cuando aumenta el *tamaño* de los datos de entrada. El encontrar un código eficiente es una tarea en general difícil, y debe ser en todo caso enfrentada cuando ya se tenga un programa básico que funcione correctamente. ¡No se debe caer en la trampa de la **optimización prematura**! En este sentido, es útil conocer que en la gran mayoría de los casos es bueno sacrificar la velocidad de ejecución en aras de una mayor claridad del código.

6. Así, se debe tener en cuenta que un programa tiene otras virtudes además de dar las salidas correctas para todas los casos. Los programas deben ser **legibles**, estar escritos de forma clara y consistente, de manera que otros programadores o el mismo programador original pasado un tiempo, puedan comprenderlos con facilidad para hacer las modificaciones que son frecuentemente necesarias. Los identificadores de las variables deben ser **autoexplicativos**, las estructuras de control deberán estar bien elegidas. El sangrado del código y el uso correcto de los espacios en blanco ayuda notablemente en este aspecto. En este sentido, Python ha adoptado la decisión de *exigir* sintácticamente un sangrado correcto del código. Los comentarios son útiles pero es mejor evitarlos usando código autoexplicativo. Aprenderemos a **documentar** nuestros programas.

7. Frecuentemente ocurre que, en la medida en que el programa crece, se debe **reestructurar** el código. Buena legibilidad y facilidad de reestructuración están íntimamente ligadas. Sobre este concepto se abundará cuando se discutan las funciones y la forma de enfrentar el diseño de los programas, utilizando técnicas como la del **refinamiento descendente**.

El alumno atento observará que en muchos de los ejemplos no nos *preocupamos* de **manejar las excepciones**, por ejemplo las causadas por entradas con un formato incorrecto de datos por parte del usuario. La razón principal es la de centrarnos en los aspectos clave de Python, evitando *distracciones* y exponiendo código de la forma más escueta posible. Esta *táctica* es la habitual en cualquier texto introductorio sobre lenguajes de programación.  

```{code-cell} ipython3

```

```{code-cell} ipython3

```
