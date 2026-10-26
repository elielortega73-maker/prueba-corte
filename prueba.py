
from principal import Stack
from principal import Accion


def main():
    pila = Stack()

    accion = Accion(1, "Escribir", "Hola")
    pila.push(accion)

    accion = Accion(2, "Agregar palabra", "mundo")
    pila.push(accion)

    accion = Accion(3, "Agregar signo", "!")
    pila.push(accion)

    print("Historial de acciones:")
    pila.print()

    print("\nUltima accion registrada:")
    pila.peek().print()


main()
