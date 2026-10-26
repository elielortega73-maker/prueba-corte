
class Accion:
    def __init__(self, id, descripcion, texto):
        self.id = id
        self.descripcion = descripcion
        self.texto = texto
        self.next = None

    def print(self):
        print(f"[ID={self.id}|ACCION={self.descripcion}|"
              f"TEXTO={self.texto}]")


class Stack:
    def __init__(self):
        self.top = None

    def push(self, nueva):
        nueva.next = self.top
        self.top = nueva

    def pop(self):
        if self.isEmpty():
            return None
        accion = self.top
        self.top = self.top.next
        accion.next = None
        return accion

    def peek(self):
        return None if self.isEmpty() else self.top

    def isEmpty(self):
        return self.top is None

    def clear(self):
        acciones = []
        while not self.isEmpty():
            acciones.append(self.pop())
        return acciones

    def print(self):
        actual = self.top
        while actual is not None:
            actual.print()
            actual = actual.next
