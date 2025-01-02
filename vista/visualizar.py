def mostrar_diccionarios(productos, precios, stock):
    """
    Muestra los diccionarios con formato tabular.
    """
    print("=" * 40)
    print("Lista de Productos:")
    print("=" * 40)
    print(f"{'ID':<5}{'Producto':<15}{'Precio':<10}{'Stock':<10}")
    for id_producto in productos:
        print(f"{id_producto:<5}{productos[id_producto]:<15}{precios[id_producto]:<10}{stock[id_producto]:<10}")
    print("=" * 40)
