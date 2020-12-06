#!/usr/bin/env python
# coding: utf-8

# # Introducción a las Clases
# 
# **Autores**: Rogelio Mazaeda Echevarría, Félix Miguel Trespaderne.   

# ## Contenidos
# [Introducción](#Introducción)<br>
# [Concepto de atributo](#Concepto_de_atributo)<br>
# [Ejecución de un objeto clase](#Ejecución_de_un_objeto_clase)<br>
# [Elementos básicos de programación con ficheros](#Ficheros_básico)<br>

# ***
# <a id='Introducción'></a>

# ## Introducción
# El paradigma de la **Programación Orientada a Objetos** permite crear al usuario tipos de datos que empaquetan en una sola entidad reusable **propiedades** (datos) y **comportamientos** (funciones).
# 
# Crear una clase supone crear un **nuevo tipo** de objeto, de tal forma que, a partir de ese momento, podemos definir nuevas variables, nuevas **instancias** de ese nuevo tipo de objeto. 
# 
# Cada instancia de una clase puede tener diferentes **miembros** o **atributos**:
# * **Datos**, **atributos** que permiten caracterizar su **estado**
# * **Métodos**, **atributos función** que permiten obtener información del **estado** y/o modificarlo
# 
# Siguiendo la terminología de C++, en general, los **miembros** de una clase son **públicos**, es decir, pueden accederse *desde el exterior* por otras partes del programa.
# > Cada lenguaje usa una terminología diferente que hace prácticamente imposible una visión unificada del paradigma de la **Programación Orientada a Objetos**. Incluso en el plano puramente teórico, conceptual, no hay consenso sobre lo que son conceptos tales como **Objeto**, **Dato Abstracto**, etc.
# 
# > El propio **tutorial oficial de Python** distingue en unos sitios entre **atributos** y **métodos**, cuando siguiendo la terminología del lenguaje ambos son atributos.  
# 
# > El gran éxito de Python hace que sean accesibles una gran cantidad de cursos, blogs, libros, etc. en los que, sin control, se diseminan cual virus terminologías inexactas. Posiblemente no seamos ajenos en este curso.

# ***
# <a id='Concepto_de_atributo'></a>

# ## Concepto de atributo
# La siguiente línea crea un nuevo tipo de objeto a través de la palabra reservada `class`.

# In[1]:


class ClaseKk: 
    pass

kk = ClaseKk()  # kk es ahora una instancia de la clase ClaseKk


# Si nos interesamos mediante la función nativa `type()` sobre la identidad de `kk` y `ClaseKk` observamos que:
# * `kk` es una **instancia** del nuevo tipo de dato `ClaseKk`
# * `ClaseKk` es una instancia de la clase `type`, igual que los tipos nativos ya conocidos como `int`, `float`, etc.

# In[2]:


for t in kk, ClaseKk, int, float, list, tuple, str:
    print('El tipo de {} es {}.'.format(t, type(t)))


# Nuestra clase `ClaseKk` no es muy divertida. Vamos a crear una nueva clase añadiéndola un **atributo**: el método `__init__()`, un método especial que Python invoca automáticamente tras crearse una nueva instancia.

# In[3]:


class Punto2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Punto2d(10, 3)  # Se invoca a __init__() con argumentos (p, 10, 3)
print(p)
print('Las coordenadas del punto son ({},{}).'.format(p.x, p.y))


# Podemos observar que `print(p)` nos imprime información del objeto y su posición en memoria. Esto es así porque no hemos *enseñado* aún a nuestra clase a imprimir sus instancias.
# 
# Sin embargo, si que hemos podido **acceder** e imprimir dos nuevos **atributos**, `x` e `y` del objeto `p`, utilizando la sintaxis `espacio_de_nombres.nombre` que ya conocemos de los módulos. Esto es así porque los nombres con los que identificamos a los atributos de un objeto de una clase constituyen un espacio de nombres propio de la clase.
# 
# El nombre `self` es una **referencia** al objeto `p` recién creado. La sentencia:
# ```python
# p = Punto2d(10, 3)
# ```
# es **azúcar sintáctico** de la llamada detrás de las bambalinas *`Punto2d(p, 10, 3)`*. Los argumentos reales `(p, 10, 3)` son recogidos por los formales `(self, x, y)` del método `__init__()`. De hecho, el identificador `self` no es sino una convención universalmente aceptada, pero podría usarse cualquier otro identificador.

# Otra forma de ver que `self` y `p` son el mismo objeto es ayudándonos de la función nativa `id()`.

# In[4]:


class Punto2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(id(self))

        
p = Punto2d(10, 3)  # Se invoca a __init__() con argumentos (p, 10, 3)
print(id(p))


# Si, como Santo Tomás, aún sois incrédulos, podéis verificar que en la llamada `p = Punto2d(10, 3)` se pasan 3 argumentos en lugar de dos. Para ello, observad la excepción que se produce en el siguiente ejemplo:

# In[5]:


p = Punto2d(100, 10, 3)


# La excepción `TypeError` nos avisa de que `__init__()` en la clase `Punto2d`recibe **3 argumentos posicionales** y no 4 como le hemos proporcionado. 
# 
# La referencia al propio objeto `self` siempre va **posicionalmente en primer lugar**.
# > Para los conocedores de C++, y salvando las distancias, el comportamiento es similar a la **palabra reservada** `this`. La ventaja en el caso de C++ es que no es necesario explicitarla (en general) en los métodos de las clases siendo, excepcionalmente en este caso, C++ menos verboso que Python. 

# En Python, los objetos poseen atributos. La función nativa `dir()` nos proporciona una lista de los atributos de un objeto.

# In[7]:


numero = 3
print(dir(numero))


# In[8]:


# Observe como __init__ es un atributo de nuestro objeto Punto2d
# ¡Pero x e y no lo son!
print(dir(Punto2d))


# In[9]:


# Observe como x e y son dos nuevos atributos de nuestro objeto p
# Son atributos propios del objeto p, no de la clase Punto2d
print(dir(p))


# Vemos que el objeto clase `Punto2d` *cede* los nombres de sus atributos a su instancia `p`. 
# 
# Investiguemos realmente qué ocurre en esa cesión. Veamos cual es el tipo del atributo `__init__` según el objeto de que se trate:

# In[6]:


print(type(Punto2d.__init__))
print(type(p.__init__))


# Vemos que son atributos que comparten el nombre, pero son tipos diferentes. 
# 
# Para la clase, el acceso a sus atributos función es el habitual que hemos visto para las funciones. En este caso, para usar el objeto `__init__` deberemos usar tres argumentos, y el primero de ellos tendrá que ser una instancia de la propia clase `Punto2d` u otra que tenga los atributos `x` e `y `.

# In[5]:


class Punto2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
p = Punto2d(5, 6)
print(p.x, p.y)
Punto2d.__init__(p, 3, 4)
print(p.x, p.y)


# Obviamente, la forma que acabamos de usar para `__init__` es absurda. 
# 
# El uso de `__init__()` como **método** nos proporciona una forma estructurada, localizada y legible de incorporar los mismos tipos y nombres de atributos a todas las instancias de una clase.
# 
# Pero si no nos importa volvernos locos (y también a quien lea nuestro código) podemos incorporar atributos a nuestras instancias de otra forma. Véase el ejemplo:

# In[4]:


class Punto2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
p1 = Punto2d(10, 3)
p1.kk = 'Por favor, no hagas esto.'  # p1 tiene ahora un nuevo atributo, kk

print(dir(p1))

p2 = Punto2d(20, 1)  # Obviamente p2 no tiene el atributo kk
print(dir(p2))


# Por tanto, podemos añadir nuevos atributos a un objeto instancia de una clase de esta forma poco usual. Véase que `kk` es un atributo de `p1` pero no de `p2`.

# Para seguir reforzando el concepto de objeto y atributo véase el siguiente ejemplo, en este caso usando una función. Al igual que las clases, las funciones son nuevas instancias creadas por el programador, de la clase `function`.

# In[5]:


import math
def distancia(p1, p2):
    dif_x = p1.x - p2.x
    dif_y = p1.y - p2.y
    return math.sqrt(dif_x**2 + dif_y**2)


p1 = Punto2d(1, 1)
p2 = Punto2d(2, 2)

distancia.valor = distancia(p1, p2)  # Añadimos dinámicamente el atributo valor al objeto distancia
print(distancia.valor)


# Es obvio que este nuevo atributo `valor` de la función `distancia()` no incorpora ningún añadido ventajoso al código. Más bien al contrario, reduce la legibilidad. Sólo es una muestra de cómo a objetos creados por el programador, como nuevas clases y funciones, podemos incorporales *al vuelo* nuevos atributos.

# ¿Qué pasa cuando intentamos usar un atributo de un objeto que no hemos añadido previamente?

# In[11]:


p2.kk


# La excepción `AttributeError` lo deja claro, ¿no?

# Hagamos un poco de magia. Puesto que nuestra clase `Punto2d` es un objeto creado por nosotros, ¿podemos añadirle un atributo función? ¡Por supuesto!

# In[6]:


Punto2d.distancia = distancia  # Añadimos el atributo distancia, que es una función, a la clase Punto2d

p1 = Punto2d(1, 4)
p2 = Punto2d(4, 8)
d = p1.distancia(p2)

print(d)
print(dir(Punto2d))
print('\nEl tipo del atributo distancia de la clase `Punto2d` es {}.'.format(type(Punto2d.distancia)))
print('\nEl tipo del atributo distancia de una instancia de la clase `Punto2d` es {}.'.format(type(p1.distancia)))


# Vemos que el atributo `distancia` ya está en la lista de atributos de `Punto2d` y es del tipo `function`. Pero desde el punto de vista de la instancia `p1`, como ya hemos hablado antes, es un método.
# 
# La forma correcta y legible de incorporar el método `distancia` es en el momento de definir la clase.

# In[7]:


get_ipython().run_line_magic('reset', '-f')
import math

class Punto2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distancia(self, p2):  # self juega ahora el papel de p1 en el ejemplo anterior
        dif_x = self.x - p2.x
        dif_y = self.y - p2.y
        return math.sqrt(dif_x**2 + dif_y**2)

    
p1 = Punto2d(1, 4)
p2 = Punto2d(4, 8)
d = p1.distancia(p2)  # Esta llamada es el azucar sintáctico de la llamada d = distancia(p1, p2)

print(d)


# Para finalizar, veamos un ejemplo de cómo invocar al atributo función `distancia` de la clase `Punto2d`.

# In[ ]:


p1 = Punto2d(1, 4)
p2 = Punto2d(4, 8)
Punto2d.distancia(p1, p2)
print(d)


# Dado que lo normal es invocar a los atributos funciones de una clase a a través de las instancias de esa clase, nos referiremos en lo que sigue a estos atributos como **métodos**.

# ***
# <a id='Ejecución_de_un_objeto_clase'></a>

# ## Ejecución de un objeto clase
# Veamos con un ejemplo una diferencia esencial entre la definición de una función y la de una clase. Ejecute la siguiente celda.

# In[8]:


def mi_funcion():
    print('Dentro de la función `mi_funcion`.')
    
    
class ClaseKk:
    x = 10
    print('Dentro de la clase `ClaseKk`.')
    

print('El valor del atributo `x` de la `ClaseKk` es {}.'.format(ClaseKk.x))


# Como ya sabemos, el cuerpo de una función sólo se ejecuta cuando se invoca a la función. Sin embargo, el cuerpo de una clase se ejecuta de forma inmediata, **¡una única vez!**.
# 
# Entonces, ¿se ejecutan los métodos dentro de una clase?

# In[11]:


class ClaseKk:
    print('Dentro de la clase `ClaseKk`.')
    
    def mi_metodo():
        print('Dentro de `mi_metodo` sin argumentos.')


# Como parece lógico, nada ocurre al ejecutarse el cuerpo de la clase respecto a `mi_metodo`. Realmente, no estamos definiendo una nueva variable en el espacio de nombres global, como ocurre en el ejemplo anterior con `mi_funcion`. Lo que estamos haciendo es definir un nuevo atributo de la clase `ClaseKk`.
# 
# Para ejecutar el método `mi_metodo()` necesitamos invocarlo:

# In[10]:


ClaseKk.mi_metodo()  # Invocamos al atributo mi_metodo, en este caso como una función


# Este atributo `mi_metodo`, ¿será accesible desde una instancia de la clase?

# In[12]:


kk = ClaseKk()
kk.mi_metodo()


# Obviamente no. Ya hemos dicho que `kk.mi_metodo()` es el azucar sintáctico de `mi_metodo(kk)` y el método que hemos definido no tiene argumentos.

# Modifiquemos ahora la clase `ClaseKk` para poder usar `mi_metodo` cómo un método de una instancia de la clase:

# In[13]:


class ClaseKk:
    print('Dentro de la clase `ClaseKk`.')
    
    def mi_metodo(self):
        print('Dentro de `mi_metodo` con un argumento.')

        
kk = ClaseKk()
kk.mi_metodo()


# Resumiendo, la invocación de un método por parte de una instancia de un objeto funciona de la siguiente forma:
# > Cuando se invoca a un atributo que no es un dato, se busca en el objeto clase correspondiente un atributo con el mismo nombre. Si se encuentra, se crea un método. La lista de argumentos se modifica incorporando en la primera posición a la propia instancia.
