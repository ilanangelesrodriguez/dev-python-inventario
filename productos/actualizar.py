def actualizar_producto(productos, precios, stock):
    """
    Actualiza los datos de un producto existente.
    """
    try:
        id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
        if id_actualizar in productos:
            print("Deje en blanco los campos que no desee actualizar.")
            nuevo_nombre = input(f"Nombre actual ({productos[id_actualizar]}): ").strip()
            nuevo_precio = input(f"Precio actual ({precios[id_actualizar]}): ").strip()
            nuevo_stock = input(f"Stock actual ({stock[id_actualizar]}): ").strip()

            if nuevo_nombre:
                productos[id_actualizar] = nuevo_nombre
            if nuevo_precio:
                precios[id_actualizar] = float(nuevo_precio)
            if nuevo_stock:
                stock[id_actualizar] = int(nuevo_stock)

            print("Producto actualizado exitosamente.")
        else:
            print("Error: El ID ingresado no existe.")
    except ValueError:
        print("Error: Asegúrese de ingresar valores válidos.")
