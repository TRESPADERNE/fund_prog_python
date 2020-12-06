.. highlight:: cpp

Salto incondicional ``break``
#############################

Supongamos un programa cuya introducción de datos debe interrumpirse
cuando se cumpla una de las dos
condiciones preestablecidas siguientes:

* El número de datos introducido supera un valor máximo.
* Se cumple una determinada condición, en cuyo caso abandonaremos la
  introducción de datos.

Veamos dos alternativas, una sin usar ``break`` y otra utilizándolo.

.. raw:: latex

  \newpage

**Ejemplo con** ``while`` **sin usar** ``break``

.. code-block:: cpp

  // Suma de los números positivos introducidos: sin break 

  #include <iostream>
  using namespace std;

  int main()
  {
    int num_datos;
    cout << "Número máximo de datos a leer: ";
    cin >> num_datos;
    int i{}, dato{}, suma{}; // A cero con inicialización uniforme
    while (i < num_datos && dato >= 0)
    {
      cout << "Introduzca un dato (negativo para finalizar): ";
      cin >> dato;
      if (dato >= 0)
      {
        suma += dato;
        ++i;
      }
    }
    
    if (i > 0)
    {
      cout << "Se han introducido " << i << " datos válidos.\n";
      cout << "La suma de los datos introducidos es " << suma << ".\n";
    }
    else
      cout << "No se han introducido datos válidos.\n";
  }

`Edita, compila y ejecuta el código <https://repl.it/@fundprogeiiuva/break1>`_

Al final del tema anterior sugeríamos que antes de usar un determinado
tipo de bucle debíamos preguntarnos sobre si conocíamos el número de
iteraciones a realizar de antemano.

En este ejemplo, la respuesta podría
ser **NO**, si prevemos que el usuario no completará todos los posibles
valores a introducir, es decir, el bucle ``while`` terminará al evaluarse
la expresión ``dato >= 0`` a ``false``.

Sin embargo, podríamos adoptar una postura más *optimista* y pensar que
el usuario introducirá todos los posibles valores y, por tanto, la salida
del bucle ``while`` será debida a la evaluación de la expresión
``i < num_datos`` a ``false``. Y en este supuesto es donde el bucle ``for``
parece más oportuno.

Veámoslo en la siguiente versión del programa.

.. raw:: latex

  \newpage

**Ejemplo con** ``for`` **usando** ``break``

.. code-block:: cpp

  // Suma de los números positivos introducidos: usando break 

  #include <iostream>
  using namespace std;

  int main()
  {
    int num_datos;
    cout << "Número máximo de datos a leer: ";
    cin >> num_datos;

    int i{}, suma{}; // A cero con inicialización uniforme

    for (i = 0; i < num_datos; ++i)
    {
      cout << "Introduzca un dato (negativo para finalizar): ";
      int dato;
      cin >> dato;
      if (dato < 0)
        break;
      suma += dato;
    }
    
    if (i > 0)
    {
      cout << "Se han introducido " << i << " datos válidos.\n";
      cout << "La suma de los datos introducidos es " << suma << ".\n";
    }
    else
      cout << "No se han introducido datos válidos.\n";
  }

`Edita, compila y ejecuta el código <https://repl.it/@fundprogeiiuva/break2>`_

En este ejemplo, la sentencia ``break`` permite contemplar el caso
en el que el usuario no complete la introducción de todos los valores,
al introducir un valor negativo. 

El salto incondicional ``break`` ha sido considerado en muchos ámbitos,
sobre todo relacionados con la docencia, una mala práctica de programación. 

La realidad es que, en muchos casos, el uso de ``break`` facilita
la legibilidad del código y, por ello, es recomendable su uso.

Vamos a ver cómo un bucle ``for`` es lo suficientemente versátil para
permitir una tercera versión del ejemplo, sin usar ``break``. 

.. raw:: latex

  \newpage

**Ejemplo con** ``for`` **sin usar** ``break``

.. code-block:: cpp

  // Suma de los números positivos introducidos
  // Con for sin usar break 

  #include <iostream>
  using namespace std;

  int main()
  {
    int num_datos;
    cout << "Número máximo de datos a leer: ";
    cin >> num_datos;

    int i{}, suma{}, dato{}; // A cero con inicialización uniforme
    for (i = 0; i < num_datos && dato >= 0; ++i)
    {
      cout << "Introduzca un dato (negativo para finalizar): ";
      cin >> dato;
      if (dato >= 0)
        suma += dato;
      else
        --i; // Para compensar el ++i de fin de bloque for
    }
    
    if (i > 0)
    {
      cout << "Se han introducido " << i << " datos válidos.\n";
      cout << "La suma de los datos introducidos es " << suma << ".\n";
    }
    else
      cout << "No se han introducido datos válidos.\n";
  }

`Edita, compila y ejecuta el código <https://repl.it/@fundprogeiiuva/break3>`_

Esta versión es, sin lugar a dudas, *desafortunada*. Los bucles ``for``
es preferible usarlos con una condición de salida simple. Además, como
el incremento del contador ``i``
se produce al final del bucle, debemos decrementarlo en caso de
salida prematura por dejar de cumplirse la condición ``dato >= 0``.

Centinelas
**********

El uso de la sentencia ``break`` suele venir acompañada en muchos problemas del
uso de una variable **centinela**, también denominada **testigo** o **bandera**.

Habitualmente la variable **centinela** tiene un tipo booleano y nos permite
discriminar cuando la finalización de un bucle se ha debido o no a un salto
incondicional.

Un ejemplo clásico es la determinación de si un número es primo.

.. raw:: latex

  \newpage

**Ejemplo: determinar si un número es primo (versión 1)**

.. code-block:: cpp

  // Determina si un número entero es primo. (Versión 1)
  #include <iostream>
  using namespace std;

  int main()
  {
    int numero;
    do
    {
      cout << "Deme un entero positivo mayor que 1: ";
      cin >> numero;
      if (numero < 1)
        cout << " El valor introducido no es válido.\n";
    }
    while (numero < 1);
    
    bool es_primo{true};  // Variable centinela o bandera
    for (int divisor = 2; divisor < numero ; ++divisor)
    {
      if (numero % divisor == 0)
      {
        es_primo = false;
        break;
      }
    }

    cout << "El número " << numero;
    if (es_primo)
      cout << " es primo.\n";
    else
      cout << " no es primo.\n";
  }

`Edita, compila y ejecuta el código <https://repl.it/@fundprogeiiuva/break4>`_

Una advertencia: existen formas más eficientes de realizar la tarea propuesta;
el código anterior debe verse como un intento inicial.

La estrategia consiste en determinar, mediante un bucle, todos los posibles
divisores *legítimos*, rango ``[2, numero-1]``, que harían que se pudiera
decidir que el número no es primo.

Nótese que el bucle tiene una especie de carácter asimétrico:

* para concluir que el número es primo, se debe llevar el bucle hasta su
  conclusión, investigando todos los posibles divisores, sin hallar ningún
  divisor exacto.
* para concluir que el número no es primo, basta con encontrar el primer
  divisor exacto.

La variable **centinela** ``es_primo`` es la encargada de poner de
manifiesto cuál de las dos situaciones se ha producido.

.. raw:: latex

  \newpage

Por supuesto, el lenguaje nos brinda otras opciones para programar
el problema anterior sin usar ``break``. Como vimos anteriormente,
basta incorporar la condición de activación de la salida incondicional
a la expresión de la condición del ``for``.

**Ejemplo: determinar si un número es primo (versión 2)**

.. code-block:: cpp

  // Determina si un número entero es primo. (Versión 2)
  // Sin usar break
  #include <iostream>
  using namespace std;

  int main()
  {
    int numero;
    do
    {
      cout << "Deme un entero positivo mayor que 1: ";
      cin >> numero;
      if (numero < 1)
        cout << " El valor introducido no es válido.\n";
    }
    while (numero < 1);
    
    bool es_primo{true};  // Variable centinela o bandera
    for (int divisor = 2; divisor < numero && es_primo; ++divisor)
      if (numero % divisor == 0)
        es_primo = false;

    cout << "El número " << numero;
    if (es_primo)
      cout << " es primo.\n";
    else
      cout << " no es primo.\n";
  }

`Edita, compila y ejecuta el código <https://repl.it/@fundprogeiiuva/break5>`_

Dejamos al alumno transformar este ejemplo usando ``while`` en lugar
de ``for``.

En los ejemplos anteriores hemos utilizado una variable *ad hoc* para
el **centinela**. En muchos problemas no es estrictamente necesario
utilizarlas. Sin embargo, su uso suele mejorar la legibilidad del código.

.. raw:: latex

  \newpage

Así, el ejemplo de la determinación de si un número es primo permite usar
la variable ``divisor`` como centinela.

**Ejemplo: determinar si un número es primo (versión 3)**

.. code-block:: cpp

  // Determina si un número entero es primo. (Versión 3)
  // Sin usar centinela explícito
  #include <iostream>
  using namespace std;

  int main()
  {
    int numero;
    do
    {
      cout << "Deme un entero positivo mayor que 1: ";
      cin >> numero;
      if (numero < 1)
        cout << " El valor introducido no es válido.\n";
    }
    while (numero < 1);
    
    int divisor{2};
    for (; divisor < numero; ++divisor)
      if (numero % divisor == 0)
        break;

    cout << "El número " << numero;
    if (divisor == numero)
      cout << " es primo.\n";
    else
      cout << " no es primo.\n";
  }

`Edita, compila y ejecuta el código <https://repl.it/@fundprogeiiuva/break6>`_

Véase como nuestro centinela ``divisor`` se define e inicializa fuera del
bucle y, por tanto, podemos dejar vacía esa parte del bucle ``for``.

.. raw:: latex

  \newpage

Para terminar con esta panoplia de ejemplos, véase una última
implementación con ``while`` muy compacta.

**Ejemplo: determinar si un número es primo (versión 4)**

.. code-block:: cpp

  // Determina si un número entero es primo. (Versión 3)
  // Con while sin usar centinela explícito
  #include <iostream>
  using namespace std;

  int main()
  {
    int numero;
    do
    {
      cout << "Deme un entero positivo mayor que 1: ";
      cin >> numero;
      if (numero < 1)
        cout << " El valor introducido no es válido.\n";
    }
    while (numero < 1);
    
    int divisor{2};
    while (numero % divisor)
        ++divisor;

    cout << "El número " << numero;
    if (divisor == numero)
      cout << " es primo.\n";
    else
      cout << " no es primo.\n";
  }

`Edita, compila y ejecuta el código <https://repl.it/@fundprogeiiuva/break7>`_

Nótese que la salida del bucle está garantizada ya que cuando
``divisor`` alcanza el valor ``numero``, la expresión ``numero % divisor``
se evalúa a ``false``.

Decidir cuál de las implementaciones vistas es *superior* es cuestión de
debate.

