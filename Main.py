from Contact import Contact
from Stack import MyStack


def menu():
    stack = MyStack()

    while True:
        print("\n===== MENÚ PILA =====")
        print("1. Agregar (Push)")
        print("2. Quitar (Pop)")
        print("3. Mostrar pila")
        print("4. Ver tope (Peek)")
        print("5. Buscar un valor específico (Contains)")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        # agregar contacto
        if opcion == "1":
            try:
                id = int(input("ID del contacto: "))
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                contacto = Contact(id, nombre, telefono)
                stack.push(contacto)
                print("Contacto agregado correctamente.")
            except Exception as e:
                print(f" Error: {e}")

        # eliminar contacto
        elif opcion == "2":
            try:
                eliminado = stack.pop()
                print(f"Se quitó: {eliminado}")
            except Exception as e:
                print(f" {e}")

        # mostrar pila
        elif opcion == "3":
            print("\n Contenido de la pila:")
            print(stack)

        # ver tope
        elif opcion == "4":
            try:
                print(f"Elemento en el tope: {stack.peek()}")
            except Exception as e:
                print(f"{e}")

        # buscar id específico
        elif opcion == "5":
            try:
                id_buscar = int(input("ID del contacto a buscar: "))
                contacto_buscar = Contact(id_buscar, "", "")
                if stack.contains(contacto_buscar):
                    print("El contacto SÍ se encuentra en la pila.")
                else:
                    print("El contacto NO se encuentra en la pila.")
            except Exception as e:
                print(f"{e}")

        # salir
        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intenta nuevamente.")


if __name__ == "__main__":
    menu()
