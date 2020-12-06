.. highlight:: cpp

Introducción
############

Los **saltos incondicionales** son sentencias que permiten **interrumpir**
la secuencia natural de ejecución.

C++ dispone de 4 tipos de saltos incondicionales:

* ``break``: Sale de forma automática del último bucle abierto
  (``for``, ``while``, ``do while``) o de una sentencia ``switch``. 
* ``continue``: Da un salto hasta el final del último bucle abierto.
  (Apenas se usa y no lo utilizaremos en el curso)
* ``goto``: Salta a una línea **etiquetada** del programa.
  (No es recomendable usarlo y no lo utilizaremos en el curso)
* ``return``: Salida de una función, pudiendo devolver un valor 
  (Se verá más adelante cuando estudiemos funciones)

Nos centraremos en este tema en el salto incondicional ``break``.


