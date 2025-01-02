from productos.actualizar import actualizar_producto
from productos.agregar import agregar_producto
from productos.eliminar import eliminar_producto
from vista import mostrar_diccionarios

def menu():
    """
    Función principal del programa.
    """
    productos = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
    precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
    stock = {1: 50, 2: 45, 3: 30, 4: 15}

    while True:
        mostrar_diccionarios(productos, precios, stock)
        print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
        try:
            opcion = int(input("Elija opción: "))
            if opcion == 1:
                agregar_producto(productos, precios, stock)
            elif opcion == 2:
                eliminar_producto(productos, precios, stock)
            elif opcion == 3:
                actualizar_producto(productos, precios, stock)
            elif opcion == 4:
                print("Gracias por usar el programa. ¡Hasta luego!")
                break
            else:
                print("Error: Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Error: Ingrese un número válido.")


if __name__ == "__main__":
    menu()
