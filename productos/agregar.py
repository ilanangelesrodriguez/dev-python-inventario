def agregar_producto(productos, precios, stock):
    """
    Agrega un nuevo producto a los diccionarios.
    """
    try:
        nuevo_id = max(productos.keys()) + 1
        nombre = input("Ingrese el nombre del producto: ").strip()
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese el stock del producto: "))

        productos[nuevo_id] = nombre
        precios[nuevo_id] = precio
        stock[nuevo_id] = cantidad

        print("Producto agregado exitosamente.")
    except ValueError:
        print("Error: Asegúrese de ingresar valores válidos.")
