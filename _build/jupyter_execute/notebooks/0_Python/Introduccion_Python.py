#!/usr/bin/env python
# coding: utf-8

# # Introducción a Python
# **Autores**: Rogelio Mazaeda Echevarría, Félix Miguel Trespaderne.   

# ## Contenidos
# [Introducción](#Introducción)<br>
# [Instalación y consideraciones prácticas](#Instalación_y_consideraciones_prácticas)<br>
# [El Zen de Python](#El_Zen_de_Python)<br>
# [Cómo ejecutar código Python](#Cómo_ejecutar_código_Python)<br>
# [Bibliografía](#Bibliografía)<br>
# [Licencia de uso](#Licencia_de_uso)

# ***
# <a id='Introducción'></a>

# ## Introducción
# [**Python**](https://www.python.org) fue concebido a finales de los años 80 como un **lenguaje interpretado** orientado a la enseñanza. Con el paso del tiempo, **Python** se ha convertido en una herramienta esencial para todo tipo de programadores, ingenieros e investigadores, tanto en el ámbito académico como industrial.
# 
# El creador del lenguaje fue el informático holandés **Guido van Rossum**, conocido durante muchos años con el *título* de **BDFL** (**B**enevolent **D**ictator **f**or **L**ife). Esto era debido a que Guido tenía asignada la tarea de fijar las directrices sobre la evolución de **Python**, tarea de la que se retiró en 2018. El nombre **Python** se debe a su afición al programa de la BBC *Monty Python's Flying Circus*, del célebre grupo de humoristas británico [**Monty Python**](https://es.wikipedia.org/wiki/Monty_Python).
# 
# El éxito de **Python** reside no sólo en su simplicidad, sino que sobre él se ha construido una enorme cantidad de herramientas disponibles para todo tipo de dominios de aplicación.
# 
# Gran parte de los programas escritos en **Python** en computación científica y ciencia de datos está codificado utilizando el siguiente grupo de paquetes, consolidados casi como estándar:
# 
# - [NumPy](http://numpy.org), permite el almacenamiento y computación eficiente de matrices multidimensionales.
# - [SciPy](http://scipy.org), contiene una enorme colección de herramientas de cálculo numérico.
# - [Pandas](http://pandas.pydata.org), permite manipular, filtrar, agrupar y transformar datos, así como el sencillo acceso a las bases de datos que eventualmente puedan contenerlos.
# - [Matplotlib](http://matplotlib.org), dispone de un conjunto de funciones para la creación de figuras y gráficos de gran calidad.
# - [Scikit-Learn](http://scikit-learn.org), proporciona un paquete de herramientas con los algoritmos más usuales de aprendizaje automático.
# - [IPython/Jupyter Notebook](http://jupyter.org), consisten en un *terminal* **Python** con características avanzadas y un entorno interactivo que permite crear, compartir y editar documentos en los que se puede ejecutar código **Python**, hacer anotaciones, insertar ecuaciones, visualizar resultados y documentar funcionalidades. Este documento es un ejemplo.
# 
# Además, si en un determinado momento alguien necesita de alguna herramienta para realizar algún tipo de tratamiento a un conjunto de datos con los que esté trabajando, es muy probable que, dentro de la amplia *comunidad Python*, esa herramienta ya esté programada y sea accesible en el *dominio público*.
# 
# Obviamente, para aprovechar el poder de este ecosistema de ciencia de datos, es necesario familiarizarse con el lenguaje **Python**.

# ***
# <a id='Instalación_y_consideraciones_prácticas'></a>

# ## Instalación y consideraciones prácticas
# 
# La instalación de **Python** y el conjunto de bibliotecas asociadas que permiten trabajar con computación científica es una tarea simple independientemente del sistema operativo con el que se trabaje.

# ### Python 2 vs Python 3
# 
# Durante el curso usaremos la sintaxis de **Python 3**, que contiene sustantivas mejoras en el lenguaje, y que hacen que el código no sea compatible con el escrito en las diferentes versiones **2.x** de **Python**.
# 
# Aunque Python 3.0 fue lanzado en 2008, su adopción fue lenta, principalmente en el ámbito científico y de desarrollo web. La causa principal se debió sobre todo al enorme esfuerzo en adaptar los paquetes y herramientas ya existentes para que fuesen compatibles con la nueva versión.
# 
# Desde principio del 2014, todos los paquetes relevantes dentro de los ecosistemas de computación científica y de la ciencia de datos ya son plenamente compatibles con ambas sintaxis, por lo que en el ámbito académico se ha optado por utilizar **Python 3** por sus mejores características sintácticas.
# 
# Además, ¡**Python 2** deja de ser mantenido y mejorado desde el 1 de Enero de 2020!

# ### Instalación con Anaconda
# 
# Aunque hay muchas maneras de instalar **Python**, os sugerimos hacerlo a través de la distribución [**Anaconda**](https://www.continuum.io), que es la utilizada por el **Servicio de Informática de la EII** en los ordenadores de laboratorios y aulas.
# 
# **Anaconda** es una distribución libre y abierta de los lenguajes **Python** y [**R**](https://www.r-project.org) (lenguaje que también utilizaréis a lo largo de la titulación en otras asignaturas). Está orientado a simplificar el despliegue y administración de los diversos paquetes de software. Viene acompañada con una extensa colección de miles de paquetes y programas, muchos de ellos preinstalados. Entre estos, algunos que usaremos extensivamente, como [**Jupyter**](https://jupyter.org) y el IDE [**Spyder**](https://www.spyder-ide.org).
# 
# Las diferentes versiones de los paquetes se administran mediante un navegador o con el sistema de gestión de paquetes por línea de comandos [**conda**](https://conda.io).

# ***
# <a id='El_Zen_de_Python'></a>

# ## El Zen de Python
# 
# 
# El Zen de Python es una colección de principios de software que influyen en el diseño del lenguaje de programación **Python**. Es la entrada informativa número 20 de las **Propuestas de Mejoras de Python** ([**PEP20**](https://www.python.org/dev/peps/pep-0020), **P**ython **E**nhancement **P**roposals).
# 
# Se incluye como un *huevo de pascua virtual* en el intérprete de Python, mostrándose al ingresar la instrucción `import this`.

# In[1]:


import this


# Una posible [traducción](https://es.wikipedia.org/wiki/Zen_de_Python) sería:
# 
# * Bello es mejor que feo.
# * Explícito es mejor que implícito.
# * Simple es mejor que complejo.
# * Complejo es mejor que complicado.
# * Plano es mejor que anidado.
# * Espaciado es mejor que denso.
# * La legibilidad es importante.
# * Los casos especiales no son lo suficientemente especiales como para romper las reglas.
# * Sin embargo, la practicidad le gana a la pureza.
# * Los errores nunca deberían pasar silenciosamente.
# * A menos que se silencien explícitamente.
# * Frente a la ambigüedad, evitar la tentación de adivinar.
# * Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
# * A pesar de que esa manera no sea obvia a menos que seas holandés.
# * Ahora es mejor que nunca.
# * A pesar de que nunca es muchas veces mejor que *ahora* mismo.
# * Si la implementación es difícil de explicar, es una mala idea.
# * Si la implementación es fácil de explicar, puede que sea una buena idea.
# * Los espacios de nombres son una gran idea, ¡tengamos más de esos!

# ***
# <a id='Cómo_ejecutar_código_Python'></a>

# ## Cómo ejecutar código Python
# 
# Existen múltiples formas de utilizar **Python** dependiendo de cada situación y tarea. El hecho de ser un lenguaje *interpretado* permite su manejo de forma **interactiva**, de una forma difícilmente alcanzable con otros lenguajes como C, C++, Java, etc.
# 
# Vamos a ver a continuación algunas de las múltiples formas en las que podemos ejecutar código **Python**.

# ### El intérprete de Python
# 
# Es la forma más básica de ejecutar código. Una vez instalado el lenguaje **Python** basta teclear `python` a través de la consola de comandos. 
# 
# >Hay que tener en cuenta que la distribución Anaconda no añade automáticamente la ruta de acceso a **Python** a la variable de entorno *PATH*.
# >Sin embargo, sí que instala una consola de comandos, **Anaconda Prompt**, desde la que se pueden ejecutar directamente no sólo el intérprete de **Python** sino otros programas como **Jupyter**, **Spyder** o el gestor **conda**.
# 
# ```
# (base) C:\Users\migtr>python
# Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>>
# ```
# Una vez que el intérprete está en funcionamiento, podemos comenzar a teclear y ejecutar fragmentos de código. Lo usual es usar este formato para ejecutar secuencias cortas de operaciones, utilizando el intérprete como una potente y versátil calculadora.
# ``` python
# >>> 6*5
# 30
# >>> z = 3
# >>> z + 4
# 7
# ```

# ### El intérprete de IPython
# 
# Otra alternativa es el intérprete de [**IPython**](https://ipython.org/) (**I**nteractive **Python**), incluido en la distribución Anaconda, que posee muchas mejoras respecto al intérprete básico. Se ejecuta tecleando `ipython` en la línea de comandos:
# ```
# (base) C:\Users\migtr>ipython
# Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 7.10.2 -- An enhanced Interactive Python. Type '?' for help.
# ```
# ``` ipython
# In [1]:
# ```
# La principal diferencia entre ambos intérpretes está en el símbolo de la línea de comandos (*prompt*): **Python** usa`>>>` por defecto, mientras que **IPython** usa símbolos numerados, como `In [1]:`.
# 
# Por lo demás, se puede utilizar de la misma forma que el intérprete básico:
# ``` ipython
# In [1]: 6*5
# Out[1]: 30
# 
# In [2]: z = 3
# 
# In [3]: z + 4
# Out[3]: 7
# ```
# Nótese que, además de las entradas, las salidas aparecen numeradas también. 
# 
# **Ipython** posee un amplio abanico de características suplementarias, como los **comandos mágicos**, que iremos descubriendo a través de **Jupyter Notebook** y **Spyder**, ya que estos programas usan **IPython** como parte básica de su funcionamiento.

# ### Guiones (scripts)
# 
# A partir de cierto número de líneas (u órdenes), ejecutar fragmentos de código paso a paso es engorroso, poco práctico y sujeto a errores. En estos casos, tener almacenado en un fichero la secuencia de órdenes y ejecutarlas en un único paso es la forma lógica de proceder.
# 
# Por convención, los guiones **Python** tienen la extensión ***.py**.
# 
# Un archivo, editado por ejemplo con el **Bloc de notas**, llamado *ejemplo.py* podría ser el siguiente:
# ``` python
# # Comentario: este archivo contiene un ejemplo de guion
# print("Ejecutándose ejemplo.py")
# x = 5
# y = 3
# print("El resultado de 5 + 3 es", x + y)
# ```
# Para ejecutar este guion, debemos situarnos en el mismo directorio y teclear `python ejemplo.py` en la línea de comandos:
# ```
# (base) C:\Users\migtr>python ejemplo.py
# Ejecutándose ejemplo.py
# El resultado de 5 + 3 es 8
# ```
# Una alternativa a:
# 1. la utilización de un editor más o menos convencional de textos 
# 2. el uso de la línea de comandos para ejecutar el guion
# 
# es utilizar un **Entorno de Desarrollo Integrado**, **IDE** (**I**ntegrated **D**evelopment **E**nvironment). **Spyder** es un ejemplo de esta alternativa: entre otros componentes posee un editor con herramientas tan útiles como *autocompletado* de código, terminales **IPython**, *explorador* de variables, *depurador*, *chequeo* de inconsistencias, etc.

# ### Jupyter Notebook
# 
# **Jupyter Notebook** es un entorno interactivo que permite combinar en un mismo documento código con otros elementos, tales como texto enriquecido, imágenes, enlaces, etc. **Jupyter** es un nombre que proviene de *jugar* con los nombres de los lenguajes **Ju**lia, **Py**thon y **R**, pilares de muchos desarrollos en la computación científica y la ciencia de datos. También es un homenaje a los **cuadernos** de Galileo que registran el decubrimiento de los satélites de Júpiter. 
# 
# Inicialmente los **cuadernos** (**notebooks**) formaban parte del proyecto **IPython**, de ahí que en muchas fuentes bibliográficas aparezcan mencionados como **IPython notebooks**. A partir de cierto momento, el [**Proyecto IPython**](https://ipython.org/) se desgajó, de tal forma que en el [**Proyecto Jupyter**](https://jupyter.org/) se integraron los componentes que debían ser *agnósticos* respecto al lenguaje.
# 
# Los **cuadernos** se ejecutan localmente en un navegador sin necesidad de estar conectado a Internet. Tienen la extensión **.ipynb** (**i**nteractive **py**thon **n**ote**b**ook).
# 
# La aplicación **Jupyter Notebook** tiene un componente fundamental, el **núcleo** (**kernel**), encargado de ejecutar el código contenido en el documento. Por defecto, se ejecuta el **núcleo IPython**, pero existen núcleos para otros muchos lenguajes. 
# 
# Los *notebooks* están basando su éxito no sólo en su utilidad como herramienta de desarrollo, sino como un extraordinario medio de compartir el trabajo científico o el material académico a través de una narrativa interactiva que mezcla código, texto, datos, etc.

# ***
# <a id='Bibliografía'></a>

# ## Bibliografía
# Este cuaderno está basado en los dos primeros cuadernos introductorios del libro de **Jake Vanderplas**:
# > A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1.
# 
# La versión *notebook* del libro está disponible en [**GitHub**](https://github.com/jakevdp/WhirlwindTourOfPython).

# ***
# <a id='Licencia_de_uso'></a>

# ## Licencia de uso
# <a rel="license" href="https://creativecommons.org/share-your-work/public-domain/cc0"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/p/zero/1.0/88x31.png" /></a><br />  
# <a rel="license" href="https://creativecommons.org/share-your-work/public-domain/cc0">Creative Commons Public Domain CC0</a>.

# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# ../1_Expresiones_operadores_y_tipos_de_datos/Expresiones_operadores_y_tipos_de_datos
# ```
# 
