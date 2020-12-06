.. highlight:: cpp

Elección del bucle apropiado
############################

Las estructuras ``for``, ``do - while`` y ``while`` se pueden transformar
entre sí de forma relativamente sencilla.

.. code-block:: cpp

   for (int i = 0; i < 10; ++i)
   {
      sentencias;
   }

   //equivale a

   int i = 0;
   while (i < 10)
   {
      sentencias;
      ++i;
   }

Por ello, al programador novel suele surgirle la duda de cúal elegir para una
determinada tarea. Sin embargo, las pautas son simples haciéndonos las
siguientes preguntas:

* ¿Se conoce el número de iteraciones a realizar de antemano?

   * **SI**: la opción a elegir es usar un bucle ``for``
   * **NO**: entonces debemos hacernos una nueva pregunta:

      * ¿Se ejecutará al menos una vez el bloque de sentencias asociado al bucle? 

         * **SI**: deberemos utilizar un bucle ``do - while``
         * **NO**: el bucle ``while`` debería ser la elección.

