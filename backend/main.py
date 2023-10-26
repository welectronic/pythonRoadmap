# Contenido de app/main.py

#Creación de un script que calcule el precio total de un carrito de compras basado en una lista de precios (sin descuentos o impuestos).
def calcular_total(lista_precios):
    """
    Calcula el total sumando todos los precios en una lista.
    Para evitar problemas con la precisión de punto flotante, redondeamos el resultado a dos decimales.
    """
    total = sum(lista_precios)
    return round(total, 2)  # Redondear a dos decimales

# Creación de un script que dado el nombre de un producto y su precio, genere una etiqueta de precio en formato de cadena.
def crear_etiqueta(nombre_producto, precio, currency_code="USD"):
    """
    Crea una cadena de texto que representa una etiqueta de precio para un producto.
    """
    return f"Producto: {nombre_producto}, Precio: {currency_code} {precio:.2f}"

# Dado un listado de productos (nombre y precio), crear un script que liste aquellos productos que estén por debajo de un precio determinado
def listar_bajo(lista_productos, precio_maximo):
    productos_bajos = []

    # manejod e lista vacía
    if not lista_productos:
        return productos_bajos
    
    for nombre, precio in lista_productos:
        if precio <= precio_maximo:
            productos_bajos.append(nombre)
    
    return productos_bajos

# Este contenido es solo para probar que las funciones se ejecutan correctamente.
# No es necesario para las pruebas unitarias.
if __name__ == "__main__":
    print(calcular_total([10, 20, 30]))  # Debería imprimir 60
    print(crear_etiqueta("Zapatillas", 59.99))  # Debería imprimir 'Producto: Zapatillas, Precio: $59.99'
