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

# La entrada/salida

+++

[Introducción](#Introducción)<br>
[La función `print()`](#La_función_print())<br>
[La función `input()`](#La_función_input())<br>
[Salida con formato](#Salida_con_formato)

+++

***
<a id='Introducción'></a>

+++

## Introducción

El trabajo directo con el intérprete de Python, aunque útil para realizar pruebas puntuales, no resulta la estrategia más apropiada para escribir programas de cierta envergadura.
La opción preferida en la práctica es la de escribir, utilizando un editor de texto cualquiera, las sentencias de Python necesarias. Al fichero creado, conocido como **guion** (**script**) se le da un nombre arbitrario con extensión `.py`.

El programa así almacenado podrá ser ejecutado directamente desde una terminal del sistema operativo, con un comando similar al siguiente:
```
python primer_programa.py
```

También se puede editar y ejecutar un **guion** desde **entornos de desarrollo integrado (IDE)**, como *Spyder*, utilizando los recursos que los mismos ponen a disposición del programador.

Los programas almacenados en el archivo son ejecutados por el intérprete, sentencia a sentencia, en el orden en que estas aparezcan en el texto del mismo.

El comportamiento de una misma sentencia puede ser ligeramente diferente si se ejecuta directamente por el intérprete o como parte de la ejecución de un programa salvado previamente en un fichero. En particular, en este último caso, la evaluación de una sentencia que contiene, por ejemplo, una expresión, no produce la salida inmediata por pantalla del resultado parcial.

```{code-cell} ipython3
# Programa que calcula el área de un cilindro de radio y altura dados

radio = 2
altura = 3
PI = 3.14159

area_seccion = PI*radio**2
area_lado = 2*PI*radio*altura
area_cilindro = 2*area_seccion + area_lado
```

El programa anterior puede ser editado y almacenado en un fichero, para posteriormente ser ejecutado siguiendo alguna de las formas comentadas.

El programa es, desde luego, muy simple y tiene además el defecto de que, tal y como está, su utilidad es muy limitada:
* En primer lugar, para hallar el área exterior de un cilindro de `altura` y/o `radio` diferente, habría que editar el texto del programa para modificar las líneas pertinentes y volverlo a salvar para posteriormente ejecutarlo. 
* Otro defecto importante es que no se visualiza por pantalla el resultado del cálculo.

Nuestra experiencia en la utilización de programas de ordenador nos sugiere otra forma de actuar:
* se ejecuta el programa cuantas veces sea necesario
* en cada ocasión, se introducen datos diferentes según las necesidades utilizando el teclado del ordenador
* se visualiza, típicamente por pantalla, el resultado que se desea

O sea, dos elementos básicos que le faltan al programa anterior son las facilidades de **entrada** de datos y **salida** de resultados.

Un programa mucho más útil se muestra en la siguiente celda.

+++

***
<a id='La_función_print()'></a>

+++

### La función `print()`

```{code-cell} ipython3
# Programa que calcula el área de un cilindro de radio y altura dados por el usuario. 
# Saca por pantalla el resultado
from math import pi

radio = 2
altura = 3

area_seccion = pi*radio**2
area_lado = 2*pi*radio*altura
area_cilindro = 2*area_seccion + area_lado

print("El área del cilindro es:")
print(area_cilindro, "unidades al cuadrado")
```

Sin haber introducido aún la entrada de datos, el código anterior es capaz de mostrar por pantalla el contenido de la variable que almacena el resultado del cálculo. Para ello se utiliza la función ``` print()``` nativa del lenguaje Python.

Otra mejora importante se deriva de utilizar una mejor aproximación del número $\pi$ que se encuentra disponible, como una constante, en el módulo `math`. Al hacer esto, además evitamos cambios accidentales del valor de $\pi$.

+++

***
<a id='La_función_input()'></a>

+++

### La función `input()`

Para lograr la introducción vía teclado de los valores de los datos (`radio` y `altura`) se utiliza la función `input()` y una conversión de tipos a ``float``, tal como se muestra a continuación:

```{code-cell} ipython3
:hidePrompt: false
:tags: [raises-exception, remove-output]

# Programa que calcula el área de un cilindro con entrada y salida
from math import pi

cadena_radio = input()
radio = float(cadena_radio)

# Las dos líneas anteriores se codifican de forma más compacta e informativa para el usuario como:
# radio = float(input('Dame el radio:'))

altura = float(input('Dame la altura: '))

area_seccion = pi*radio**2
area_lado = 2*pi*radio*altura
area_cilindro = 2*area_seccion + area_lado

print("El área del cilindro es:", area_cilindro)
```

Una posible ejecución de la celda sería:

+++

```cpp
1
Dame la altura: 1
El área del cilindro es: 12.566370614359172
```

+++

Observe que la función `input()` tiene como argumento opcional una cadena de caracteres que ha de servir para informar al usuario (por pantalla) de lo que se espera introduzca por teclado. 

Por otra parte, se debe notar que la función `input()` devuelve un valor que es de tipo `str`. Es cierto que si el usuario ha hecho lo correcto, esa cadena de caracteres contendrá los dígitos y signos que puedan ser interpretados como un número real, pero para poder realizar aritmética con dicho número hay que obtener la representación numérica del mismo como un valor de tipo `float`. Para lograrlo se utiliza la función nativa de Python `float()`, que espera como argumento una cadena y devuelve el tipo de datos real que la representa (en caso de que no haya errores).

La solicitud de la variable `radio` no se hace de una forma **amigable** para el usuario (**user friendly**). Si este no conoce la dinámica del programa, le será imposible saber qué se le está solicitando.

La solicitud del valor de la variable `altura` corrige el defecto de la anterior de no contener un indicación clara al usuario. Al mismo tiempo resulta más compacta, puesto que utiliza la capacidad de composición de las funciones para aplicar directamente la función `float()` a la cadena que devuelve la función `input()`.

+++

***
<a id='Salida_con_formato'></a>

+++

## Salida con formato
Habrá notado que la función `print()` puede tener un número variable de argumentos:
* cuando estos son cadenas de caracteres, los muestra tal cual en la consola de salida, dispositivo genérico normalmente asociado a la pantalla.
* cuando el argumento de la función no es una cadena de caracteres, implícitamente la función `print()` realiza  la conversión requerida desde el tipo de dato original a `str`.

El funcionamiento por defecto de `print()` es tal que, al finalizar la salida por pantalla, escribe un carácter que representa el cambio del cursor de la pantalla hacia una nueva línea, el carácter `\n`. En la mayoría de los casos, este es el comportamiento adecuado.

En algunas ocasiones, sin embargo, se podría requerir que el cursor permaneciera en la misma línea después de ejecutar la función `print()`. Para ello, se puede incluir un argumento invocado mediante el parámetro `end` de forma que contenga el carácter que la función debe utilizar al final de la línea. 

Vea el ejemplo siguiente:

```{code-cell} ipython3
vol = 3
print("El valor del volumen es:", end = " ")
print(vol)
```

El funcionamiento ya descrito de ```print()``` es suficiente para una salida por pantalla básica, útil en muchos casos.

En ocasiones se desea tener un control más detallado de la forma en que los valores van a ser ofrecidos al usuario. Puede desearse, por ejemplo:
* mostrar solo un determinado número de dígitos significativos de determinado valor, o 
* reservar un espacio en pantalla específico para sacar datos en forma de tabla, respetando la alineación de las columnas. 

Para estos casos, se utiliza preferentemente la opción de especificar formatos en las cadenas de caracteres.

Por ejemplo:

```{code-cell} ipython3
area_base = 10.6666
area_lado = 20.3891
area_total = 2*area_base + area_lado

print("El área de la base es {:.2f}, el del lado {:.2f} y el área total es {:.3f}".
      format(area_base, area_lado, area_total))
print("Cambiando el orden total: {2:.2f} es 2*{0:.2f} + {1:.2f}".
      format(area_base, area_lado, area_total))
```

Observe el use de las llaves `{}` para introducir dentro de la cadena de caracteres *referencias* a valores que serán proporcionados mediante el **método** `.format()`. Estas referencias tienen el **formato** `{[n]:[tam][.precisión]formato}`. Se debe entender que los corchetes no se mostrarán por pantalla, sino que, como es costumbre a la hora de describir la sintaxis de algunas sentencias, significa que su contenido puede ser omitido. 

* `n` se utiliza para especificar el número de orden del valor que debe ser embebido tal y como aparece en los argumentos de `.format()`, comenzando en cero. 
Si se omite esta especificación, se asume el mismo orden en que los argumentos aparecen en `.format()`. 
* `tam` establece el tamaño del campo en pantalla; de no existir, se tomará el espacio necesario, cualquiera que este sea. 
* `.precisión` especifica el número de lugares decimales al que se redondeará el valor. Esto es aplicable  en el caso de que se trate de un valor real. 
* `formato` es una letra que identifica el tipo del valor: `f` para `float`, `d` para `int` y `s` para `str` son los más habituales.

Véase el ejemplo siguiente. Haced modificaciones y razonad el resultado.

```{code-cell} ipython3
print("{:5d}{:15.3f}".format(123, 1.234343))
print("{1:5f}{0:15d}".format(1, 1180.2))
```
