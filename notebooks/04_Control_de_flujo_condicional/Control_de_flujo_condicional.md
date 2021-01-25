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

# Control de flujo condicional

+++

[Introducción](#Introducción)<br>
[El tipo booleano y sus operadores](#El_tipo_booleano_y_sus_operadores)<br>
[Control de flujo condicional `if`](#Control_de_flujo_condicional)<br>
[Estructura condicional ampliada `if ... else`](#Estructura_condicional_doble)<br>
[Estructura condicional anidada `if ... elif ...else`](#Estructura_condicional_múltiple)

+++

***
<a id='Introducción'></a>

+++

## Introducción 

Los sencillos programas vistos hasta ahora funcionan perfectamente, pero son poco más que un conjunto de expresiones y de asignaciones de variables, colocadas unas a continuación de otras y provistas de comunicación con el usuario a través de la entrada y salida.

Esta visión de la programación, limitada a la **ejecución secuencial** de instrucciones, es demasiado simple y no aporta nada esencialmente novedoso con respecto al funcionamiento tipo calculadora utilizando directamente el intérprete. 

Las capacidades que vemos día a día en nuestra interacción con los ordenadores y las aplicaciones informáticas, serían imposibles si solamente contáramos con las posibilidades vistas hasta el momento.

+++

Es suficiente la introducción de dos nuevas estructuras básicas para que se abra la puerta a la posibilidad de realizar todas las tareas de cómputo que son teóricamente concebibles.

Estas dos estructuras son:
* las **estructuras condicionales**
* las **estructuras iterativas o bucles**

Sirven para alterar, durante la ejecución del programa, la estructura secuencial que se tiene por defecto. 

Dedicaremos este cuaderno a la primera de ellas.

Una **sentencia condicional** realiza un conjunto u otro de sentencias dependiendo del cumplimiento
o no de una determinada condición.
En Python podemos distinguir diferentes tipos:
* Simple: ``if``
* Ampliada: ``if - else``
* Anidada: ``if – elif - . . . - else``

Además de las sentencias de control de flujo condicional, introduciremos en este tema
un nuevo el tipo de dato ``bool`` y algunos de sus operadores asociados.

+++

***
<a id='El_tipo_booleano_y_sus_operadores'></a>

+++

## El tipo booleano y sus operadores

En temas anteriores, hemos visto los tipos ``int``, ``float`` y ``str`` y algunos de sus operadores asociados. En la
práctica existen otros tipos de valores y otras categorías de operaciones que quisiéramos poder realizar.

+++

### Operadores de comparación
Muchas veces es necesario comparar valores cuyo tipo tiene definida alguna operación de orden, como, por ejemplo, los propios datos de tipo numéricos. Python tiene para ese propósito los **operadores de comparación**:  

| Operador | Tipo de comparación | 
|:--------:|:--------------------|
| `<`      | Menor que           |
| `>`      | Mayor que           |
| `<=`     | Menor o igual que   |
| `>=`     | Mayor o igual que   |
| `==`     | Igual que           |
| `!=`     | Distinto de         |

+++

Observe en las celdas siguientes el comportamiento de estos operadores y experimente con varios de ellos.

```{code-cell} ipython3
x = 2
y = 3
print(x > 3)
```

```{code-cell} ipython3
x = 3
y = 3*1
print(x == y)
```

### El tipo ``bool``
Estas expresiones involucran típicamente operandos de tipo numérico pero el resultado es cualitativamente diferente. Es un resultado **lógico** o **booleano** (en referencia al álgebra de [**G. Boole**](https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole)). Estos resultados se asocian a un nuevo tipo, el **tipo** ``bool``,  que puede representar solo dos valores: `True` ó `False`.

Las palabras reservadas `True` y `False` son literales predefinidos por el lenguaje con el objetivo de
aportan legibilidad y contexto a las expresiones booleanas.

+++

### Operadores lógicos booleanos
Sirven para evaluar **expresiones booleanas compuestas**.

Los operadores lógicos permiten trabajar con las **conectivas lógicas** **conjunción**, **disyunción** y **negación**.

| Operador | Conectiva  | 
|:--------:|:-----------|
| `and`    | Conjunción |
| `or`     | Disyunción |
| `not`    | Negación   |

+++

El **operador de conjunción** o **Y lógico** se representa con el operador `and`.
Devuelve un valor que es `True` solo si todas las proposiciones lógicas representadas por sus operandos son simultáneamente también `True`. 

Véase el ejemplo a continuación:

```{code-cell} ipython3
x = 1
y = 0
z = 100
print(x > y and x < z)
```

La conectiva lógica **disyunción** o **O lógico** se representa con el operador `or`. La operación `or` brinda un resultado cierto (`True`) cuando al menos uno de sus operandos es `True`. Tanto el `or` como el `and` son operadores binarios.

```{code-cell} ipython3
print(x < y or x < z)
```

Una operación lógica aún más simple es la **negación**, representada en Python por el operador `not`. Este último es un operador unario que simplemente *invierte* el valor lógico del operando al que se aplica.

```{code-cell} ipython3
not False and True
```

Los operadores lógicos se especifican completamente por sus **tablas de verdad**.



|  ``x``   | ``y``    | ``x and y`` | ``x or y``| 
|:------:|:------:|:---------:|:--------:|
|``True``  | ``True`` | ``True``  | ``True``   | 
|``True``  | ``False``| ``False`` | ``True``   | 
|``False`` | ``True`` | ``False`` | ``True``   | 
|``False`` | ``False``| ``False`` | ``False``  |

|  ``x``    | ``not x``  | 
|:------:|:--------:|
| ``True``  | ``False``  | 
| ``False`` | ``True``   |

+++

Se pueden asociar tantos operadores como se deseen. El `not` unario es el de mayor prioridad y el `or` es el de menor. Se deben utilizar paréntesis para modificar esa precedencia por defecto. 

La evaluación de las operaciones lógicas se realiza de izquierda a derecha y se interrumpe cuando
se ha asegurado el resultado. Esto se conoce como **propiedad de cortocircuito**: si se puede concluir
el valor lógico del resultado a partir de una evaluación parcial de la expresión, no se sigue
evaluando la misma.

Analice, por ejemplo, por qué la siguiente expresión no genera al ejecutarse una **excepción** de división por cero. ¿Qué pasa si se cambia el orden de ambos operandos?

```{code-cell} ipython3
True or 2/0 > 1
```

Los valores y operadores lógicos se pueden mezclar con operadores de tipo numérico. En esos casos, un valor numérico `0` se comporta como `False` y cualquiera diferente de cero como `True`.
En cualquier caso, los operadores lógicos típicamente se utilizan junto a los operadores de comparación.

```{code-cell} ipython3
x = 3
y = 0
y or x
```

En un ejemplo anterior, queríamos determinar si el valor `x` estaba entre otros dos valores, `y` y `z`:

```{code-cell} ipython3
x = 1
y = 0
z = 100
print(x > y and x < z)
```

O sea, tiene que cumplirse que el `x` es simultáneamente menor que el `z` `and` mayor que el `y`. Este tipo de sintaxis es habitual y obligada en la mayoría de los lenguajes de programación. En Python es perfectamente legítima. Sin embargo, este lenguaje ofrece una forma alternativa de *encadenar* los operadores de comparación, que resulta, en ocasiones como esta, estar más en concordancia con nuestras intuiciones matemáticas. 

Por ejemplo, la misma proposición se podría haber expresado en Python de la siguiente manera:

```{code-cell} ipython3
print(x > y and x < z)
```

### Tabla de precedencias

La siguiente tabla muestra las precedencias de los operadores estudiados hasta el momento.

| Operador | Evaluación | Rango |
|:--------:|:----------:|:-----:|
| `()`     | Izq. a Der.| 1     |
| `**`     | Der. a Izq.| 2     |
| `+`      | Unario     | 3     |
| `-`      | Unario     | 3     |
| `*`      | Izq. a Der.| 4     |
| `\`      | Izq. a Der.| 4     |
| `\\`     | Izq. a Der.| 4     |
| `%`      | Izq. a Der.| 4     |
| `+`      | Izq. a Der.| 5     |
| `-`      | Izq. a Der.| 5     |
| `==`     | Izq. a Der.| 6     |
| `!=`     | Izq. a Der.| 6     |
| `<`      | Izq. a Der.| 6     |
| `<=`     | Izq. a Der.| 6     |
| `>`      | Izq. a Der.| 6     |
| `>=`     | Izq. a Der.| 6     |
| `not`    | Unario     | 7     |
| `and`    | Izq. a Der.| 8     |
| `or`     | Izq. a Der.| 9     |

+++

***
<a id='Control_de_flujo_condicional'></a>

+++

## Control de flujo condicional `if`

La estructura **condicional**, en su versión más sencilla, permite decidir si ejecutar o no determinadas sentencias, en base a si es cierta una expresión lógica dada.

```{code-cell} ipython3
:tags: [remove-output, raises-exception]

# Estructura condicional simple

a = int(input("Introduzca el número a invertir: "))

if a != 0:
    a = 1/a
    print(a)
print("Esta línea se ejecuta en cualquier caso\n")    
```

Una posible ejecución de la celda sería:

```cpp
Introduzca el número a invertir: 4
0.25
Esta línea se ejecuta en cualquier caso
```

+++

La sintaxis incluye la palabra reservada `if` seguida de una **expresión lógica** y el **delimitador** `:`.

Las sentencias asociadas al bloque ``if`` aparecen **sangradas** a partir del delimitador `:`. Son aquellas que se evaluarán si la expresión lógica es `True`. ¡El sangrado es obligatorio!, es parte de la sintaxis. (4 espacios es el valor recomendado). 

En este ejemplo, se *pregunta* si el valor referido por `a` es diferente de cero.
* Si durante la ejecución del programa el valor de `a` es diferente de `0` (porque el usuario lo decidió de ese modo al introducir el dato), entonces la expresión entre el `if` y el `:` se evalúa como `True` y esto implicará que se ejecuten las dos sentencias que aparecen sangradas hacia la derecha en el código.
* Si la evaluación de la **expresión de control** diera `False`, estas dos sentencias serían omitidas en la ejecución del programa.

En cualquiera de los dos casos, la sentencia final (que aparece *sin sangrar*, es decir, escrita a partir de la misma columna que la sentencia `if` en el texto del programa) es ejecutada.

+++

El condicional es una estructura de control de flujo que aparece, de una forma u otra, en todos los lenguajes de programación. Por ejemplo, en C/C++ el mismo programa se escribiría de la siguiente forma:

```python
cout << "Introduzca el número a invertir: ";
cin >> a;

if(a != 0)
{
    a = 1/a;
    cout << a;
}
cout << "Esta línea se ejecuta en cualquier caso" << endl;
```
Trate de identificar la equivalencia entre las diferentes sentencias, haciendo énfasis en la estructura `if`. 

Note que en C/C++ las sentencias afectadas por el `if`, si son más de una, tienen que estar obligatoriamente delimitadas por llaves. En C/C++ el sangrado no es obligatorio como en Python, aunque muy recomendado. De esta forma, de un solo golpe de vista, podemos identificar claramente la estructura y el significado del código. De hecho, la ausencia del sangrado es considerada como una deficiencia grave de estilo de programación que conduce a código de difícil *lectura* y, por tanto, también difícil de poner a punto y mantener.

+++

La forma en que Python elige la sintaxis del `if` dice mucho sobre la filosofía seguida en el diseño de este lenguaje: eliminar los elementos innecesarios y *forzar*, en lo posible, al programador a codificar los programas siguiendo las mejores prácticas.

En cuanto a la eliminación de elementos innecesarios, se puede observar que Python no exige ningún carácter para terminar las sentencias, a diferencia del C/C++ que necesita del uso del `;` para este propósito. 

Ya en lo referente específicamente al `if` se puede observar que Python logra los dos propósitos anteriores a la vez:
* no requiere de las llaves para delimitar las sentencias afectadas por el condicional
* es capaz de indicar cuáles son estas sentencias por medio del sangrado 

De esta forma, dicho sangrado, lejos de ser un elemento opcional (deseado) como en C/C++, ahora es un elemento esencial de la definición del `if` en Python.

Nótese además que en Python no es obligatorio que la expresión de control esté entre paréntesis.

+++

***
<a id='Estructura_condicional_doble'></a>

+++

## Estructura condicional ampliada `if ... else`

+++

La **estructura condicional ampliada** establece, como en el caso previo, las sentencias que se han de ejecutar si la expresión lógica de control se satisface. Pero, adicionalmente, indica aquellas sentencias que se ejecutarán en el caso contrario, cuando la expresión de control es falsa, introduciendo la palabra reservada `else`. Véase el siguiente ejemplo:

```{code-cell} ipython3
:tags: [remove-output, raises-exception]

# Estructura condicional ampliada (if ... else)

mes = int(input("Introduzca el mes de año "))

if 1 <= mes <= 12:
    print("Se ha introducido un mes válido")
else: 
    print("El mes es incorrecto. Por defecto se elige Enero")
    mes = 1
    
print("Se utilizará mes", mes)    
```

Una posible ejecución de la celda sería:

```cpp
Introduzca el mes de año 2
Se ha introducido un mes válido
Se utilizará mes 2
```

+++

***
<a id='Estructura_condicional_múltiple'></a>

+++

## Estructura condicional anidada `if ... elif ...else`

En el caso de que existan, en lugar de dos, **n** caminos de ejecución alternativos, se puede extender la estructura anterior de la manera que se muestra a continuación:

```{code-cell} ipython3
:tags: [remove-output, raises-exception]

# Estructura condicional anidada (if ... elif ...else)

mes = int(input("Introduzca el mes del año "))

if mes == 1:
    print("El mes de enero tiene 31 días")
elif mes == 2: 
    print("El mes es de febrero tiene 28 o 29 días")
elif mes == 3:
    print("El mes es de marzo tiene 31 días")
elif mes == 4:
    print("El mes es de abril tiene 30 días")
elif mes == 5:
    print("El mes es de mayo tiene 31 días")
elif mes == 6:
    print("El mes es de junio tiene 30 días")
elif mes == 7:
    print("El mes es de julio tiene 31 días")
elif mes == 8:
    print("El mes es de agosto tiene 31 días")
elif mes == 9:
    print("El mes es de septiembre tiene 30 días")
elif mes == 10:
    print("El mes es de octubre tiene 31 días")
elif mes == 11:
    print("El mes es de noviembre tiene 30 días")
elif mes == 12:
    print("El mes es de diciembre tiene 31 días")
else:
    print("Mes no válido")
```

Una posible ejecución de la celda sería:

```
Introduzca el mes del año 12
El mes es de diciembre tiene 31 días
```

+++

Algunas cosas sobre las que reflexionar en el código de la celda previa:

* Esta estructura se debe utilizar cuando las alternativas sean todas **mutuamente excluyentes**.
- Si la expresión de control de un `if` **múltiple** evalúa a cierta, el resto de las expresiones de control *aguas abajo* no son ni siquiera evaluadas.
- El último `else` es opcional.

Frecuentemente se utilizan conectivas lógicas en las expresiones de control del `if`. Vea una variante, más compacta, del código previo. Eso sí, se pierde la información respecto al mes.

```{code-cell} ipython3
:tags: [remove-output, raises-exception]

# Estructura condicional anidada (if ... elif ...else) (con conectivas lógicas)

mes = int(input("Introduzca el mes del año "))

if mes == 1 or mes == 3 or mes == 5 or mes ==7 or mes == 8 or mes == 10 or mes == 11:
    print("El mes tiene 31 días")
elif mes == 2: 
    print("El mes tiene 28 o 29 días")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("El mes tiene 30 días")
else:
    print("Mes no válido")
```

La naturaleza anidada puede verse en el siguiente ejemplo. Es una variante idéntica a la anterior, sin utilizar ``elif``.
Lógicamente, la fórmula anidada aporta legibilidad.

```{code-cell} ipython3
:tags: [remove-output, raises-exception]

# Estructura condicional anidada (if ... elif ...else) (con tuplas)

mes = int(input("Introduzca el mes del año "))

if mes == 1 or mes == 3 or mes == 5 or mes ==7 or mes == 8 or mes == 10 or mes == 11:
    print("El mes tiene 31 días")
else:
    if mes == 2: 
        print("El mes tiene 28 o 29 días")
    else:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            print("El mes tiene 30 días")
        else:
            print("Mes no válido")
```
