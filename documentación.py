
"""
PROYECTO: HISTORIAL DE ACCIONES MEDIANTE UNA PILA

1. ABSTRACCION DE LA ESTRUCTURA EN EL CONTEXTO

El contexto seleccionado es el historial de acciones de un
editor de texto. Se utiliza una pila para registrar acciones
como escribir palabras o agregar signos de puntuacion.

La pila funciona bajo el principio LIFO (Last In, First Out),
que significa que la ultima accion agregada es la primera
en retirarse.

Correspondencia:
- Accion: objeto de la clase Accion.
- push(): agrega una accion a la pila.
- pop(): retira la ultima accion registrada.
- peek(): consulta la accion ubicada en la cima.
- isEmpty(): comprueba si la pila esta vacia.
- clear(): elimina todas las acciones.
- top: referencia a la cima de la pila.
- next: enlaza una accion con el siguiente nodo.

2. DOCUMENTACION DEL CONTEXTO

El problema consiste en almacenar las acciones realizadas
por un usuario y permitir consultarlas en orden inverso.

Cada accion contiene:
- id: identificador de la accion.
- descripcion: nombre de la operacion realizada.
- texto: contenido relacionado con la accion.
- next: referencia al siguiente nodo.

La clase Stack administra las acciones mediante una pila
enlazada. Cada nueva accion se coloca en la cima y puede
consultarse o retirarse utilizando sus operaciones.

Procedimiento:
1. Crear una pila vacia.
2. Crear objetos de la clase Accion.
3. Registrar las acciones mediante push().
4. Mostrar el historial con print().
5. Retirar acciones con pop() cuando sea necesario.

3. UTILIZACION DE LA IMPLEMENTACION

El archivo Stack.py contiene las clases Accion y Stack.
El archivo principal.py importa ambas clases y utiliza
sus metodos para registrar y mostrar las acciones.

La operacion push() agrega un nodo en la cima.
La operacion pop() retira el nodo superior.
La operacion peek() consulta el nodo superior.
La operacion isEmpty() comprueba si existen elementos.
La operacion clear() elimina todos los nodos.
La operacion print() muestra las acciones almacenadas.

4. JUSTIFICACION DE LA ESTRUCTURA

Se utiliza una pila porque el historial debe procesarse
siguiendo el principio LIFO.

Por ejemplo, si se registra primero "Hola", despues
"mundo" y finalmente "!", la primera accion que se
retirara sera la que contiene el signo "!".

5. CONCLUSION

La pila enlazada permite administrar un historial de
acciones de forma organizada y eficiente. Este proyecto
demuestra el uso de nodos, referencias y las operaciones
principales de una pila en Python.

Nota: el programa registra y muestra las acciones, pero
no modifica directamente un editor de texto real.
"""
