# Contenido de app/main.py

def calcular_total(lista_precios):
    """
    Calcula el total sumando todos los precios en una lista.
    Para evitar problemas con la precisión de punto flotante, redondeamos el resultado a dos decimales.
    """
    total = sum(lista_precios)
    return round(total, 2)  # Redondear a dos decimales

def crear_etiqueta(nombre_producto, precio):
    """
    Crea una cadena de texto que representa una etiqueta de precio para un producto.
    """
    return f"Producto: {nombre_producto}, Precio: ${precio:.2f}"

# Este contenido es solo para probar que las funciones se ejecutan correctamente.
# No es necesario para las pruebas unitarias.
if __name__ == "__main__":
    print(calcular_total([10, 20, 30]))  # Debería imprimir 60
    print(crear_etiqueta("Zapatillas", 59.99))  # Debería imprimir 'Producto: Zapatillas, Precio: $59.99'
