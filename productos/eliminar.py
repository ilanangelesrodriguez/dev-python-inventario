def eliminar_producto(productos, precios, stock):
    """
    Elimina un producto de los diccionarios.
    """
    try:
        id_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
        if id_eliminar in productos:
            productos.pop(id_eliminar)
            precios.pop(id_eliminar)
            stock.pop(id_eliminar)
            print("Producto eliminado exitosamente.")
        else:
            print("Error: El ID ingresado no existe.")
    except ValueError:
        print("Error: Ingrese un ID válido.")
