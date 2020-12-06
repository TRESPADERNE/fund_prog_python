#!/usr/bin/env python
# coding: utf-8

# # Proceso de desarrollo de un programa
# **Autores**: Rogelio Mazaeda Echevarría, Félix Miguel Trespaderne.   

# ## Contenidos
# [Proceso de desarrollo de un programa](#Proceso_de_desarrollo_de_un_programa)<br>
# [Ejemplo 1: Determinación de si una serie de enteros son primos](#Determinación_de_si_una_serie_de_enteros_son_primos)<br>
# [Ejemplo 2: Determinación del número $\pi$ mediante la serie de Euler](#Determinación_del_número_pi_mediante_la_serie_de_Euler)<br>
# [Ejemplo 3: Algoritmo para la determinación del máximo comúm divisor (MCD)](#Algoritmo_para_la_determinación_del_máximo_comúm_divisor_(MCD))<br>
# [Ejemplo 4: Conjetura de Collatz](#Conjetura_de_Collatz)<br>
# [Ejemplo 5: Algoritmo de ordenación por inserción](#Algoritmo_de_ordenación_por_inserción)

# ***
# <a id='Proceso_de_desarrollo_de_un_programa'></a>

# ## Proceso de desarrollo de un programa
# La programación es una tarea compleja a la que es mejor enfrentarse de manera **iterativa**. En los diferentes ejemplos de determinación de si un número es primo estamos viendo una prueba de ello.
# 
# Algunos pasos generales para hacerlo son:
# 
# 1. Analizar cuidadosamente el problema a resolver. Utilizar en esta etapa **lápiz y papel** y la ayuda de **bosquejos**, entre otros recursos. Identificar los **datos de entrada** y cuales deben ser las **salidas** buscadas, para todas las posibles condiciones. Hacer cálculos paso a paso. Identificar **resultados intermedios** tratando de encontrar el algoritmo adecuado. 
# 
# 2. Una vez se llega a una primera solución *en papel* razonable, se pasa a programar, utilizando los recursos provistos por el lenguaje. Como se ha dicho, ya se poseen los elementos imprescindibles para resolver cualquier problema solucionable por un ordenador. Por supuesto, en la medida que avance el curso, los recursos a nuestra disposición crecerán.
# 
# 3. Puede darse el caso de que el programa no funcione para los **casos límites o especiales** (¿funciona para el 2, que es el primer posible primo?, etc.). Es importante identificar esos casos para poder testarlos y, en su caso, corregir los fallos. 
# 
# 4. Por otro lado, es frecuente que en un primera esbozo del programa, se asuma que el usuario va a actuar de la forma prevista pero ¿qué pasa si no lo hace? ¿qué pasa si el número introducido es menor que dos o incluso negativo?. En ocasiones, el no prever todas estas posibles situaciones puede dar un resultado incorrecto o que el programa se interrumpa bruscamente por un error de ejecución. La solución de cada uno de los problemas detectados, implicará probablemente volver al paso 1 y la realización de modificaciones del código más o menos importantes, hasta que se llega a un código robusto y que funcione para todas las posibles entradas de datos. 
# 
# 5. El primer programa seguramente no constituye la forma más **eficiente** (más rápida, por ejemplo) de resolver el problema. Un código que ya funciona correctamente puede estar sujeto a mejoras y optimizaciones. Aunque no se hará hincapié sobre este tema en un curso básico, en algunas ocasiones, sobre todo cuando se manipulan grandes volúmenes de datos, son importantes las consideraciones de cómo crece, por ejemplo, el tiempo de ejecución del programa cuando aumenta el *tamaño* de los datos de entrada. El encontrar un código eficiente es una tarea en general difícil, y debe ser en todo caso enfrentada cuando ya se tenga un programa básico que funcione correctamente. ¡No se debe caer en la trampa de la **optimización prematura**! En este sentido, es útil conocer que en la gran mayoría de los casos es bueno sacrificar la velocidad de ejecución en aras de una mayor claridad del código.
# 
# 6. Así, se debe tener en cuenta que un programa tiene otras virtudes además de dar las salidas correctas para todas los casos. Los programas deben ser **legibles**, estar escritos de forma clara y consistente, de manera que otros programadores o el mismo programador original pasado un tiempo, puedan comprenderlos con facilidad para hacer las modificaciones que son frecuentemente necesarias. Los identificadores de las variables deben ser **autoexplicativos**, las estructuras de control deberán estar bien elegidas. El sangrado del código y el uso correcto de los espacios en blanco ayuda notablemente en este aspecto. En este sentido, Python ha adoptado la decisión de *exigir* sintácticamente un sangrado correcto del código. Los comentarios son útiles pero es mejor evitarlos usando código autoexplicativo. Aprenderemos a **documentar** nuestros programas.
# 
# 7. Frecuentemente ocurre que, en la medida en que el programa crece, se debe **reestructurar** el código. Buena legibilidad y facilidad de reestructuración están íntimamente ligadas. Sobre este concepto se abundará cuando se discutan las funciones y la forma de enfrentar el diseño de los programas, utilizando técnicas como la del **refinamiento descendente**.
# 
# El alumno atento observará que en muchos de los ejemplos no nos *preocupamos* de **manejar las excepciones**, por ejemplo las causadas por entradas con un formato incorrecto de datos por parte del usuario. La razón principal es la de centrarnos en los aspectos clave de Python, evitando *distracciones* y exponiendo código de la forma más escueta posible. Esta *táctica* es la habitual en cualquier texto introductorio sobre lenguajes de programación.  

# ***
# <a id='Determinación_de_si_una_serie_de_enteros_son_primos'></a>

# ## Ejemplo 1: Determinación de si una serie de enteros son primos
# La última versión para determinar si un número es primo es correcta para todos los posibles enteros que el usuario introduzca. Pero sólo puede *analizar* un número cada vez. ¿Cómo modificarlo para darle la oportunidad al usuario de que analice sucesivamente varios enteros sin tener que ejecutar varias veces el programa?
# 
# La solución es utilizar otro bucle (bucles anidados), que incluya el código anterior, de manera que se pueda repetir cuantas veces se desee.

# In[1]:


# Determina si una serie de enteros son primos.

while True:
    try:
        numero = int(input('Deme un entero positivo mayor que 1: '))
        if numero < 2:
            raise ValueError('El valor introducido debe ser mayor que 1.')
    except ValueError as e:
        print(e)
    else:
        es_primo = True
        for div in range(2, numero):
            if numero % div == 0:
                es_primo = False
                break
        if es_primo:
            print("El número {} es primo.".format(numero))
        else:
            print("El número {} no es primo.".format(numero))
    finally:
        opcion = input("Desea salir (s/n):")
        if opcion == 's' or opcion == 'S':
            break


# La expresión de control del bucle `while` externo es la constante literal `True` por lo que no hay forma de salir mediante la expresión de control: es un *bucle infinito*. Este tipo de bucles, muy habituales en programación, van asociados a una sentencia `break` que permitan su terminación prematura. Es el caso con el `break` de la estructura condicional donde se pregunta al usuario si quiere seguir introudciendo enteros.
# 
# Por otro lado, en este ejemplo vemos la utilidad del manejo de excepciones. Si el usuario introduce como entero un valor espurio, por ejemplo `kk`, el programa ya no termina abruptamente.

# Otra alternativa puede ser:

# In[ ]:


# Determina si una serie de enteros son primos (versión 2)

opcion = 'n'
while opcion != 's' and opcion != 'S':
    try:
        numero = int(input('Deme un entero positivo mayor que 1: '))
        if numero < 2:
            raise ValueError('El valor introducido debe ser mayor que 1.')
    except ValueError as e:
        print(e)
    else:
        es_primo = True
        for div in range(2, numero):
            if numero % div == 0:
                es_primo = False
                break
        if es_primo:
            print("El número {} es primo.".format(numero))
        else:
            print("El número {} no es primo.".format(numero))
    finally:
        opcion = input("Desea salir (s/n):")


# El programa previo hace lo que nos proponíamos, aunque su uso por el usuario puede ser algo engorroso debido a la pregunta explícita sobre si se desea salir o no del programa. 
# 
# En ocasiones, la naturaleza del problema es tal que el rango posible de la entrada de datos está limitado. Este hecho se puede utilizar en nuestra ventaja para simplificar el diseño del programa y mejorar la experiencia del usuario. ¿Cómo se hace? Simplemente se utilizan los valores no útiles del rango de entrada para señalar otros *caminos* al programa.
# 
# En el caso que nos ocupa se puede hacer, por ejemplo, que la introducción por parte del usuario de un valor menor que 2 señale su deseo de abandonar el programa. En caso contrario, se continuaría con las iteraciones en el bucle externo, preguntando por otros enteros a considerar.
# 
# Por tanto, la introducción de un valor menor que 2 deja de ser una excepción. Es parte de los valores válidos que puede utilizar el usuario.

# In[ ]:


# Determina si una serie de enteros son primos (versión 3)

numero = 2         # Valor incial arbitrario para que entre al bucle la primera vez
while numero > 1:
    print('\nPara salir introduzca un entero menor que 2.')
    try:
        numero = int(input('Deme un entero: '))
    except ValueError as e:
        print(e)
    else:
        if numero > 1:
            es_primo = True
            for div in range(2, numero):
                if numero % div == 0:
                    es_primo = False
                    break
            if es_primo:
                print("El número {} es primo.".format(numero))
            else:
                print("El número {} no es primo.".format(numero))
                
print("Fin del programa.")


# ***
# <a id='Determinación_del_número_pi_mediante_la_serie_de_Euler'></a>

# ## Ejemplo 2: Determinación del número $\pi$ mediante la serie de Euler
# 
# La constante $\pi$ es una de la más importantes en matemáticas. Conocemos que se trata de un número real con infinitas cifras no periódicas tanto en su representación decimal como en cualquier otra base numérica.
# 
# En el módulo `math` se tiene una aproximación bastante precisa del mismo, suficiente para las aplicaciones ingenieriles concebibles. 
# 
# En el siguiente ejemplo, se va a proceder a su estimación, utilizando uno de las tantas series que se demuestra que convergen a dicho número.
# 
# En particular, se tiene la siguiente serie infinita definida para todos los enteros positivos $k$:
# 
# \begin{align}
# \\\frac{\pi^2}{12} & = 1 - \frac{1}{2^2}+  \frac{1}{3^2} ...+\frac{(-1)^{k+1}}{k^2} \\
# \end{align}
# 
# Nótese que la solución de este problema, la suma en principio ilimitada de un conjunto de números, no se puede emprender sin la presencia de un bucle. 
# 
# Conviene, antes de comenzar, analizar en detalle el mecanismo propuesto para la generación de una aproximación de $\pi$:
# 
# - ¿Sabríamos antes de entrar al bucle el número de iteraciones a ejecutar? Unicamente lo sabríamos si alguien nos dijera que quiere hacer una aproximación que involucre $n$ términos. Esto haría decantarnos hacia la utilización de un bucle `for`. 
# - Sin embargo, lo razonable es plantear el problema de forma que el resultado se aproxime a $\pi$ por debajo de una **tolerancia** o cuando se cumpla una **condición de terminación** previamente elegida por el usuario. Esto hace que nos decantemos por utilizar un bucle `while`.
# 
# - El trabajo con bucles frecuentemente requiere:
#     - Inicializar variables  antes de entrar al bucle.
#     - Identificar qué es lo que variará de una iteración a otra y qué objetivos parciales se van cumpliendo de forma tal que en cada iteración nos vayamos acercando cada vez más a la solución buscada.
#     - Establecer la condición lógica que determine la permanencia en el bucle.
#     - Finalmente, comprobar que el bucle funcione también para los casos límites.
# 

# In[ ]:


# Determinación del número pi mediante la serie de Euler

tolerancia = 1e-6

suma_parcial = 0.0
termino = tolerancia + 1 # Para obligar a entrar en el bucle
k = 1
while abs(termino) > tolerancia:
    termino = (-1)**(k + 1)/k**2
    suma_parcial += termino
    k += 1
    
pi_aprox = (12.0*suma_parcial)**0.5
    
print("La aproximación de PI hallada es {} y se obtuvo en {} iteraciones".format(pi_aprox,k))


# * En el caso anterior, se requiere un **contador** (`k`) que recorra los enteros que participan en la definición de cada término de la serie y que debe ser incrementado en cada iteración. 
# * También de una variable tipo **acumulador** (`suma_parcial`) que siempre va a contener la suma de todos los términos que se hayan calculado hasta la iteración de que se trate.
# * Observe el uso de de la asignación compuesta `+=` para actualizar tanto el acumulador como el contador.
# * Se define por comodidad una variable (`termino`) que contine el valor del término que se añade a la serie en cada iteración. Se hace esto porque se ha decidido utilizar como criterio de permanencia en el bucle el hecho de que el *aporte* nuevo a la estimación del valor de `suma_parcial`sea (en valor absoluto) mayor que un valor elegido pequeño, `tolerancia` (en este caso una millonésima: `1e-6`).
# * Vea que el uso de la función `abs()` en la expresión de control del `while` es indispensable, puesto que el valor de los términos nuevos van cambiando de signo de una iteración a la siguiente. 
# * Antes de entrar al bucle, se eligen los valores iniciales para el contador y el acumulador. En el caso del contador se inicializa a `1` porque se empieza en ese valor en la propia definición de la serie. El acumulador se inicializa a `0`. 
# * A la variable `termino`, que participa en la expresión de control del bucle, se le da un valor inicial arbitrario, en este caso `tolerancia + 1`. El objetivo aquí es darle un valor que sea mayor que `tolerancia` y que permita por tanto la primera entrada al bucle.
# 
# El orden en que aparecen las sentencias dentro del bucle es importante (aunque no es la única posble si el problema se replanteara de otra forma). Es conveniente realizar algunas iteraciones manuales para ver que el esquema elegido funciona correctamente.
# 
# Al salir del bucle se saca por pantalla tanto la aproximación hallada como el número de iteraciones que tomó el calcularla.
# 
# Pruebe a cambiar el valor de la tolerancia. En cualquier caso, se debe recordar que la precisión con la que son manipulados los `float` en Python es limitada.

# ***
# <a id='Algoritmo_para_la_determinación_del_máximo_comúm_divisor_(MCD)'></a>

# ## Ejemplo 3: Algoritmo para la determinación del máximo comúm divisor (MCD)
# 
# Se trata de encontrar el mayor número que divida exactamente dos números enteros positivos dados. El algoritmo que resuelve el problema es uno de los más antiguos y famosos y se atribuye a Euclides. Sean dos enteros positivos: $p$ y $q$ (suponiendo $p >= q$). En general se puede plantear lo siguiente:
# $$p=q*b+r$$
# Euclides razonó que un divisor exacto común de $p$ y $q$ también dividirá a $q$ y a $r$ (el resto de la división).
# 
# Este mismo razonamiento puede repetirse cuantas veces se quiera, haciendo que el dividendo sea el anterior divisor y el nuevo divisor el antiguo resto, hasta que eventualmente, con toda seguridad, se obtendrá un resto igual a cero (puesto que los sucesivos restos van inevitablemente descendiendo y deben ser positivos). Cuando el resto es cero, el último divisor que se utilizó es precisamente el **MCD**.
# 
# Si el divisor inicial es $0$, el **MCD** es el dividendo y si ambos son ceros el **MCD** es $0$.

# In[5]:


# Halla el MCD de dos numeros enteros naturales, incluido el 0

# ENTRADA DE DATOS
while True:
    dividendo = int(input('Introduzca un número >=0: '))
    divisor = int(input('Introduzca un número >=0: '))
    if dividendo < 0 or divisor < 0:
        print("Ambos números deben ser iguales o mayores que 0.\n")
    else:
        break

# ALGORITMO MCD
if dividendo < divisor: # Asegurando que el dividendo sea mayor que el divisor
    dividendo, divisor = divisor, dividendo

if dividendo == divisor == 0:
    mcd = 0
elif divisor == 0:
    mcd = dividendo
else:
    resto = dividendo % divisor          # Hallamos el primero resto fuera del bucle
    while resto != 0:
        dividendo = divisor
        divisor = resto
        resto = dividendo % divisor
    mcd = divisor

# SALIDA
print('El MCD es {}.'.format(mcd))


# El código de Python anterior implementa el algoritmo de Euclides. Podemos ver claramente las tres partes típicas de un programa:
# * Entrada de datos
# * Algoritmo
# * Salida de datos
# 
# Centrándonos en el algoritmo, nótese que:
# * la condición de permanencia en el bucle es que el resto sea diferente de cero.
# * antes de entrar al bucle se hace, una primera división para obtener un resto válido.
# * dentro del bucle la tarea es entonces acomodar lo que antes era el divisor de forma que se convierta en el nuevo dividendo y que el antiguo resto pase a ser el divisor. El orden de estas asignaciones es crucial.
# * la última sentencia del bucle halla el nuevo resto que será considerado en la siguiente evaluación del control del bucle.
# * al salir del bucle el **MCD** es el valor que está en la variable `divisor`.
# 
# Debido al caracter iterativo de un bucle, es primordial elegir el momento clave en que se realiza la división entera y que las variables que participan hallan sido actualizadas de forma que desempeñen el _rol_ adecuado en la iteración de que se trate. Esto implica, en muchas ocasiones, hacer reasignaciones como se muestra en el ejemplo.
# 
# Es importante antes de entrar al bucle, garantizar que el dividendo es mayor o igual que el divisor. Esto se hace mediante el correspondiente `if`. Véase que el intercambio entre los contenidos de `dividendo` y `divisor` se hace en una sola línea, aprovechando la fácilidad que brinda Python y que no existe en muchos otros lenguajes. ¿Se podría hacer uso de esta **asignación doble** dentro del bucle? ¿Cómo se haría?

# Veamos una posible versión más robusta manejando excepciones.

# In[ ]:


# Halla el MCD de dos numeros enteros naturales, incluido el 0 (versión 2)

# ENTRADA DE DATOS
while True:
    try:
        dividendo = int(input('Introduzca un número >=0: '))
        divisor = int(input('Introduzca un número >=0: '))
        if dividendo < 0 or divisor < 0:
            raise ValueError('Ambos números deben ser iguales o mayores que 0.')
    except ValueError as error:
        print(error)
    else:
        break

        
# ALGORITMO MCD
if dividendo < divisor: # Asegurando que el dividendo sea mayor que el divisor
    dividendo, divisor = divisor, dividendo

if dividendo == divisor == 0:
    mcd = 0
elif divisor == 0:
    mcd = dividendo
else:
    resto = dividendo % divisor          # Hallamos el primero resto fuera del bucle
    while resto != 0:
        dividendo = divisor
        divisor = resto
        resto = dividendo % divisor
    mcd = divisor

# SALIDA
print('El MCD es {}.'.format(mcd))


# Nótese de nuevo que esta versión maneja un posible error en el formato de la entrada de datos sin que el programa finalice brúscamente.

# ***
# <a id='Conjetura_de_Collatz'></a>

# ## Ejemplo 4: Conjetura de Collatz
# 
# La conjetura de Collatz propone que para cualquier número positivo, si se sigue el procedimiento que a continuación se establece, al final de muchas iteraciones el valor al que llega $n$ será siempre la unidad.
# 
# $$
# n=\begin{cases}
#     n/2,  & &\text{si $n$ par}.\\
#     3n+1, & & \text{si $n$ impar}.
#   \end{cases}
# $$
# 
# Este hecho no está demostrado, de ahí que se trate de una **conjetura**. El siguiente código implementa el algoritmo propuesto pero añade un contador para acotar el número máximo de iteraciones.
# 

# In[ ]:


# Conjetura de Collatz
# ENTRADA DE DATOS
n = 0
while n < 1:
    n = int(input("Dame un número entero positivo: "))
    if n < 1:
        print("¡ERROR!. El número debe ser positivo.")

num_max_iteraciones = 1e10

# ALGORITMO
iteraciones = 0
while n != 1 and iteraciones < num_max_iteraciones:
    if n % 2 == 0:  # Par
        n = n // 2
    else:
        n = 3*n + 1
    iteraciones += 1

# SALIDA
if n == 1:
    print("Se ha llegado a 1 en {} iteraciones.".format(iteraciones))
else:
    print("No se ha llegado a 1 en {} iteraciones. ¡Se debe investigar más!".format(iteraciones))


# Fuera del bucle se obtiene el valor inicial de $n$ y se inicializa el contador. Dentro del bucle, simplemente se actualiza el valor de $n$ según el procedimiento dado. Se saldrá del bucle cuando $n$ llega al valor de $1$ (reforzando nuestra convicción de que la conjetura de Collatz es válida) o cuando el contador llega al valor de la constante utilizada.
# 
# Los valores intermedios por los que pasa $n$ hasta finalmente llegar $1$ oscilan con amplitudes muy grandes. 
# 
# Aprovechando esta característica, vamos a introducir otra idea básica, que al igual que los **acumuladores**, permite obtener alguna característica del conjunto de números procesados mediante un bucle. 
# 
# Se trata de obtener, el valor máximo o mínimo de todos los valores procesados. En el caso que nos ocupa, sería interesante obtener al final cuál ha sido el valor mayor por el que ha pasado $n$.
# 
# La idea para resolver este tipo de problema es tan sencilla como efectiva y se puede enunciar de la siguiente forma para el caso de querer obtener el valor máximo:
# 
# - Fuera del bucle, incializar una variable, `maximo`, con el primer valor del conjunto de números (o con el menor de los valores del rango esperado, si es que esta información se conoce)
# 
# - Si el algoritmo encuentra un $n$ impar, interrogar mediante un condicional, si el valor actualmente inspeccionado del conjunto de números es mayor que el que teníamos *memorizado* en `maximo` y, en caso afirmativo, actualizar el valor de esta última variable. Nótese que si $n$ es par, el nuevo valor $n$ será necesariamente inferior.
# 
# Modificaremos el código previo para lograr encontrar el valor máximo por el que pasa $n$.

# In[ ]:


# Conjetura de Collatz
# ENTRADA DE DATOS
n = 0
while n < 1:
    n = int(input("Dame un número entero positivo: "))
    if n < 1:
        print("¡ERROR!. El número debe ser positivo.")

num_max_iteraciones = 1e10

# ALGORITMO
iteraciones = 0
maximo = n    # inicializamos a un valor conocido
while n != 1 and iteraciones < num_max_iteraciones:
    if n % 2 == 0:  # Par
        n = n // 2
    else:
        n = 3*n + 1
        if n > maximo:
            maximo = n
    iteraciones += 1

# SALIDA
if n == 1:
    print("Se ha llegado a 1 en {} iteraciones.".format(iteraciones))
else:
    print("No se ha llegado a 1 en {} iteraciones. ¡Se debe investigar más!".format(iteraciones))

print("El mayor valor por el que ha pasado n ha sido", maximo)


# Observe que `maximo` ha sido inicializado con el valor inicial de `n`, que es el primer valor conocido.
# 
# Para finalizar, una posible solución manejando excepciones.

# In[ ]:


# Conjetura de Collatz
# ENTRADA DE DATOS
n = 0
while n < 1:
    try:
        n = int(input("Dame un número entero positivo: "))
        if n < 1:
            raise ValueError("¡ERROR!. El número debe ser positivo.")
    except ValueError as error:
        print(error)

num_max_iteraciones = 1e10

# ALGORITMO
iteraciones = 0
maximo = n    # inicializamos a un valor conocido
while n != 1 and iteraciones < num_max_iteraciones:
    if n % 2 == 0:  # Par
        n = n // 2
    else:
        n = 3*n + 1
        if n > maximo:
            maximo = n
    iteraciones += 1

# SALIDA
if n == 1:
    print("Se ha llegado a 1 en {} iteraciones.".format(iteraciones))
else:
    print("No se ha llegado a 1 en {} iteraciones. ¡Se debe investigar más!".format(iteraciones))

print("El mayor valor por el que ha pasado n ha sido", maximo)


# ***
# <a id='Algoritmo_de_ordenación_por_inserción'></a>

# ## Ejemplo 5: Algoritmo de ordenación por inserción
# Una de las actividades más habituales en programación es la de ordenar una colección de datos. Es tan común esta tarea, que existen funciones y métodos ya listos para ser utilizados, predefinidos en el lenguaje, para realizar esta tarea, como por ejemplo, el método `.sort()`  de las listas.
# 
# La razón que justifica la importancia de tener listas ordenadas radica en la facilidad posterior de encontrar elementos en una lista ordenada, al poder realizar sobre ellas las llamadas **búsquedas binarias**, mucho más eficientes que una búsqueda **secuencial**.
# 
# Existen muchos algoritmos de ordenación, de diferente grado de complejidad y eficiencia. El algoritmo de ordenación por **inserción** o **método de la baraja** es bastante simple y resulta eficaz para colecciones no muy grandes.
# 
# Supongamos que se quiere ordenar una lista dada de menor a mayor. La idea básica consiste en dividir (conceptualmente) la lista en dos: 
# * una primera sublista que se mantiene siempre ordenada
# * una sublista con los elementos restantes, que están en principio desordenados
# 
# De forma iterada, se extrae el primer elemento de la sublista desordenada y se inserta en el lugar adecuado en la sublista ordenada.
# De esta forma, en cada iteración la sublista ordenada crece en un elemento y la desordenada disminuirá en uno. 
# 
# ¿Cómo inicializar el algortimo? El tamaño inicial de la sublista ordenada será uno y el elemento que la compone será el primer elemento de la lista original ¡que está, por supuesto, ordenado!. El resto de elementos constituyen la lista inicial desordenada.

# In[ ]:


enteros = [20, 1, 4, -1, -10, 0, 1, 6]

for i in range(1, len(enteros)): # Recorre la sublista desordenada
    j = i
    tmp = enteros[i]  # Copia temporal del nuevo elemento
    while j > 0 and enteros[j-1] > tmp: # Bucle que deja un hueco para insertar el nuevo elemento en la sublista ordenada
        enteros[j] = enteros[j-1]
        j -= 1
    enteros[j] = tmp  # Inserta el nuevo elemento

print(enteros)


# Es importante entender que el algoritmo anterior ordena la lista _in situ_. Se trata de dos bucles anidados. El `for` externo _recorre_ todos los elementos, a partir del segundo utilizando el índice ```i```, esto es recorre uno por uno todos los elementos de la sublista desordenada. El bucle interno, por su parte, utiliza un `while` y otro índice ```j``` para recorrer la sublista de los elementos ya ordenados, hasta encontrar el sitio que le corresponde al elemento que debe ser insertado y que está provisionalmente almacenado en ```tmp```. Nótese que mientras no se encuetra la posición adecuado en la sublista ordenada, los elementos de la misma son _recolocados_ apropiadamente *ascendiéndolos* una posición. 
# 
# ¿Cómo modificarías el código previo para que se ordene de mayor a menor?
