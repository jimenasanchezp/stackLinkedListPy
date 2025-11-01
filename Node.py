class Node:
    def __init__(self, value, prev=None):
        self.value = value # guarda el valor del nodo
        self.prev = prev # guarda la referencia al nodo anterior

    def __str__(self):
        # devuelve una representación en cadena del valor del nodo
        return str(self.value)
    