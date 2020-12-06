#!/usr/bin/env python
# coding: utf-8

# # Control de flujo condicional
# **Autores**: Rogelio Mazaeda Echevarría, Félix Miguel Trespaderne.   

# ## Contenidos
# [Introducción](#Introducción)<br>
# [Control de flujo condicional (`if`)](#Control_de_flujo_condicional)<br>
# [Estructura condicional doble (`if ... else`)](#Estructura_condicional_doble)<br>
# [Estructura condicional múltiple (`if ... elif ...else`)](#Estructura_condicional_múltiple)

# ***
# <a id='Introducción'></a>

# ## Introducción 
# 
# Los sencillos programas vistos hasta ahora funcionan perfectamente, pero son poco más que un conjunto de expresiones y de asignaciones de variables, colocadas unas a continuación de otras y provistas de comunicación con el usuario a través de la entrada y salida.
# 
# Esta visión de la programación, limitada a la **ejecución secuencial** de instrucciones, es demasiado simple y no aporta nada esencialmente novedoso con respecto al funcionamiento tipo calculadora utilizando directamente el intérprete. 
# 
# Las capacidades que vemos día a día en nuestra interacción con los ordenadores y las aplicaciones informáticas, serían imposibles si solamente contáramos con las posibilidades vistas hasta el momento.

# Resulta asombroso saber que es suficiente la introducción de dos nuevas estructuras básicas para que se abra la puerta a la posibilidad de realizar todas las tareas de cómputo que son teóricamente concebibles.
# 
# Estas dos estructuras son:
# * las **estructuras condicionales**
# * las **estructuras iterativas o bucles**
# 
# Sirven para alterar, durante la ejecución del programa, la estructura secuencial que se tiene por defecto. 
# 
# Dedicaremos este cuaderno a la primera de ellas.

# ***
# <a id='Control_de_flujo_condicional'></a>

# ## Control de flujo condicional (`if`)
# 
# La estructura **condicional**, en su versión más sencilla, permite decidir si ejecutar o no determinadas sentencias, en base a si se cumple una condición lógica dada.

# In[1]:


# Estructura condicional simple

a = int(input("Introduzca el número a invertir: "))

if a != 0:
    a = 1/a
    print(a)
print("Esta línea se ejecuta en cualquier caso\n")    


# La sintaxis incluye la palabra reservada `if` seguida de una **expresión lógica** y el **delimitador** `:`. Las sentencias que aparecen **sangradas** a partir del delimitador `:` son aquellas que se evaluarán si la expresión lógica es `True`. ¡El sangrado (4 espacios es el valor recomendado) es obligatorio!
# 
# En este ejemplo, se *pregunta* si el valor referido por `a` es diferente de cero.
# * Si durante la ejecución del programa el valor de `a` es diferente de `0` (porque el usuario lo decidió de ese modo al introducir el dato), entonces la expresión entre el `if` y el `:` se evalúa como `True` y esto implicará que se ejecuten las dos sentencias que aparecen sangradas hacia la derecha en el código.
# * Si la evaluación de la **expresión de control** diera `False`, estas dos sentencias serían omitidas en la ejecución del programa.
# 
# En cualquiera de los dos casos, la sentencia final (que aparece *sin sangrar*, es decir, escrita a partir de la misma columna que la sentencia `if` en el texto del programa) es ejecutada.

# El condicional es una estructura de control de flujo que aparece, de una forma u otra, en todos los lenguajes de programación. Por ejemplo, en C/C++ el mismo programa se escribiría de la siguiente forma:
# 
# ```python
# cout << "Introduzca el número a invertir: ";
# cin >> a;
# 
# if(a != 0)
# {
#     a = 1/a;
#     cout << a;
# }
# cout << "Esta línea se ejecuta en cualquier caso" << endl;
# ```
# Trate de identificar la equivalencia entre las diferentes sentencias, haciendo énfasis en la estructura `if`. 
# 
# Note que en C/C++ las sentencias afectadas por el `if`, si son más de una, tienen que estar obligatoriamente delimitadas por llaves. En C/C++ el sangrado no es obligatorio como en Python, aunque muy recomendado. De esta forma, de un solo golpe de vista, podemos identificar claramente la estructura y el significado del código. De hecho, la ausencia del sangrado es considerada como una deficiencia grave de estilo de programación que conduce a código de difícil *lectura* y, por tanto, también difícil de poner a punto y mantener.

# La forma en que Python elige la sintaxis del `if` dice mucho sobre la filosofía seguida en el diseño de este lenguaje: eliminar los elementos innecesarios y *forzar*, en lo posible, al programador a codificar los programas siguiendo las mejores prácticas.
# 
# En cuanto a la eliminación de elementos innecesarios, se puede observar que Python no exige ningún carácter para terminar las sentencias, a diferencia del C/C++ que necesita del uso del `;` para este propósito. 
# 
# Ya en lo referente específicamente al `if` se puede observar que Python logra los dos propósitos anteriores a la vez:
# * no requiere de las llaves para delimitar las sentencias afectadas por el condicional
# * es capaz de indicar cuáles son estas sentencias por medio del sangrado 
# 
# De esta forma, dicho sangrado, lejos de ser un elemento opcional (deseado) como en C/C++, ahora es un elemento esencial de la definición del `if` en Python.
# 
# Nótese además que en Python no es obligatorio que la expresión de control esté entre paréntesis. 

# ***
# <a id='Estructura_condicional_doble'></a>

# ## Estructura condicional doble (`if ... else`)

# La **estructura condicional doble** establece, como en el caso previo, las sentencias que se han de ejecutar si la expresión lógica de control se satisface. Pero, adicionalmente, indica aquellas sentencias que se ejecutarán en el caso contrario, cuando la expresión de control es falsa, introduciendo la palabra reservada `else`. Véase el siguiente ejemplo:

# In[ ]:


# Estructura condicional doble (if ... else)

mes = int(input("Introduzca el mes de año "))

if 1 <= mes <= 12:
    print("Se ha introducido un mes válido")
else: 
    print("El mes es incorrecto. Por defecto se elige Enero")
    mes = 1
    
print("Se utilizará mes", mes)    


# ***
# <a id='Estructura_condicional_múltiple'></a>

# ## Estructura condicional múltiple (`if ... elif ...else`)
# 
# En el caso de que existan, en lugar de dos, **n** caminos de ejecución alternativos, se puede extender la estructura anterior de la manera que se muestra a continuación:

# In[ ]:


# Estructura condicional múltiple (if ... elif ...else)

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


# Algunas cosas sobre las que reflexionar en el código de la celda previa:
# 
# * Esta estructura se debe utilizar cuando las alternativas sean todas **mutuamente excluyentes**.
# - Si la expresión de control de un `if` **múltiple** evalúa a cierta, el resto de las expresiones de control *aguas abajo* no son ni siquiera evaluadas.
# - El último `else` es opcional.
# 
# Frecuentemente se utilizan conectivas lógicas en las expresiones de control del `if`. Vea una variante. más compacta, del código previo.

# In[ ]:


# Estructura condicional múltiple (if ... elif ...else) (con conectivas lógicas)

mes = int(input("Introduzca el mes del año "))

if mes == 1 or mes == 3 or mes == 5 or mes ==7 or mes == 8 or mes == 10 or mes == 11:
    print("El mes de enero tiene 31 días")
elif mes == 2: 
    print("El mes es de febrero tiene 28 o 29 días")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("El mes es de abril tiene 30 días")
else:
    print("Mes no válido")


# Una alternativa más **"económica"** a la solución anterior y más en consonancia con la filosofía de Pyhton, es la que se ofrece en el siguiente fragmento. Está solución se basa en el hecho de que Python maneja de forma muy eficiente secuencias de datos (listas, tuplas) que se definirán en el siguiente tema. En particular el operador especial ```in``` es capaz de determinar la **pertencia** o no de un valor a una colección de valores. De manera que, aunque el código siguiente se comprenderá en su justa dimensión más adelante, lo insertamos aquí para futura referencia.

# In[3]:


# Estructura condicional múltiple (if ... elif ...else) (con tuplas)

mes = int(input("Introduzca el mes del año "))

if mes in  (1, 3, 5, 7, 8, 10, 11):
    print("El mes de enero tiene 31 días")
elif mes == 2: 
    print("El mes es de febrero tiene 28 o 29 días")
elif mes in (4, 6, 9, 11):
    print("El mes es de abril tiene 30 días")
else:
    print("Mes no válido")

