# Contenido de tests/test_main.py
import unittest
from app import main  # Importar el módulo que queremos probar

class TestMainFunctions(unittest.TestCase):
    def test_calcular_total(self):
        # Lista de casos de prueba. Cada caso es una tupla donde el primer elemento es la entrada
        # y el segundo elemento es la salida esperada.
        casos_prueba = [
            ([10.0, 20.0, 30.0], 60.0),
            ([5.99, 12.5, 3.49], 21.98),
            ([15.0, 23.0], 38.0),
            ([99.99, 0.01], 100.0),
            ([49.5, 49.5, 10.0], 109.0),
            ([], 0.0),  # Prueba para lista vacía
            ([29.99], 29.99),  # Prueba para lista con un elemento
            ([11.11, 11.11, 11.11, 11.11, 11.11], 55.55),
            ([2.5, 2.5, 5.0, 15.0], 25.0),
            ([19.99, 20.01, 39.99], 79.99)
        ]

        # Prueba cada caso utilizando subTest para agruparlos bajo la misma prueba unitaria.
        for i, (entrada, salida_esperada) in enumerate(casos_prueba):
            with self.subTest(i=i):
                self.assertEqual(main.calcular_total(entrada), salida_esperada)
        
        casos_prueba = [
            (("Zapatillas", 59.99), "Producto: Zapatillas, Precio: $59.99"),
            (("Camisa", 25.99), "Producto: Camisa, Precio: $25.99"),
            (("Pantalones", 39.49), "Producto: Pantalones, Precio: $39.49"),
            (("Gorra", 15.00), "Producto: Gorra, Precio: $15.00"),
            (("Vestido", 49.99), "Producto: Vestido, Precio: $49.99"),
            (("Calcetines", 5.99), "Producto: Calcetines, Precio: $5.99"),
            (("Guantes", 23.50), "Producto: Guantes, Precio: $23.50"),
            (("Bufanda", 12.00), "Producto: Bufanda, Precio: $12.00"),
            (("Chaqueta", 89.90), "Producto: Chaqueta, Precio: $89.90"),
            (("Jeans", 44.50), "Producto: Jeans, Precio: $44.50")
        ]

        for i, (entrada, salida_esperada) in enumerate(casos_prueba):
            with self.subTest(i=i):
                nombre, precio = entrada  # Desempacar la entrada en sus variables correspondientes
                self.assertEqual(main.formatear_producto(nombre, precio), salida_esperada)


# Esto permite ejecutar las pruebas desde la línea de comando
if __name__ == '__main__':
    unittest.main()
