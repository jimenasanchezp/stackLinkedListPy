from Node import Node

class MyStack:
    def __init__(self):    #constructor de la pila  
        self.top = None # apunta al nodo superior de la pila
        
    def push(self, value):
        n = Node(value, self.top) # crea un nuevo nodo que apunta al top actual
        self.top = n # actualiza el top para que sea el nuevo nodo
        #self.count += 1 # incrementa el contador de elementos

    def pop(self):
        # elimina y devuelve el valor del nodo superior
        if self.is_empty():
            raise Exception("La pila está vacía.")
        val = self.top.value # guarda el valor del nodo superior
        self.top = self.top.prev # actualiza el top al nodo anterior
        #self.count -= 1 # decrementa el contador de elementos
        return val

    def peek(self):
        if self.is_empty(): # verifica si la pila está vacía
            raise Exception("La pila está vacía.")
        return self.top.value # devuelve el valor del nodo superior sin eliminarlo

    def contains(self, value):
        t = self.top # comienza desde el nodo top
        while t: # recorre la pila
            if t.value == value:
                return True # encuentra el valor
            t = t.prev # avanza al nodo anterior
        return False # no encuentra el valor
    
    def count(self):
        t = self.top
        count = 0
        while t is not None:
            count += 1
            t = t.prev  # Asumiendo que cada nodo tiene un atributo 'prev'
        return count
    
    def clear(self):
        self.top = None # elimina todos los nodos
        self.count = 0 # resetea el contador de elementos


    def is_empty(self):
        # verifica si la pila está vacía
        return self.top is None

    def clear(self):
        self.top = None # elimina todos los nodos
        self.count = 0 # resetea el contador de elementos

    def __len__(self):
        return self.count # devuelve el número de elementos en la pila

    def __str__(self):
        result = [] # lista temporal para almacenar los valores
        current = self.top # comienza desde el nodo top
        while current: # recorre la pila
            result.append(str(current.value))  # agrega el valor del nodo a la lista
            current = current.prev # avanza al nodo anterior
        return "\n".join(result) if result else "(pila vacía)"
        # devuelve una representación en cadena de la pila