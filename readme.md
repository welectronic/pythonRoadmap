# Curso de Python: Backend de Ecommerce

## Día 1: Sintaxis básica, variables y tipos de datos

### Contenidos:
1. Introducción al entorno Python: instalación, IDEs y configuración.
2. Sintaxis básica de Python: indentación, comentarios y declaraciones.
3. Tipos de datos básicos: `int`, `float`, `str`, `bool`.
4. Variables y asignación.
5. Operadores básicos: aritméticos, comparación y lógicos.

### Ejercicios:
1. Creación de un script que calcule el precio total de un carrito de compras basado en una lista de precios (sin descuentos o impuestos).
2. Creación de un script que dado el nombre de un producto y su precio, genere una etiqueta de precio en formato de cadena.

---

## Día 2: Control de flujo

### Contenidos:
1. Estructuras condicionales: `if`, `elif`, `else`.
2. Bucles: introducción al bucle `for`, recorriendo listas y cadenas.
3. Uso de `break` y `continue` dentro de bucles.
4. Comprensiones de lista como una forma rápida de generar listas.

### Ejercicios:
1. Dado un listado de productos (nombre y precio), crear un script que liste aquellos productos que estén por debajo de un precio determinado.
2. Creación de un script que, dada una lista de productos, genere una lista de los nombres de productos en mayúsculas usando comprensiones de lista.

---

## Día 3: Manejo de errores y excepciones

### Contenidos:
1. Introducción a errores comunes en Python.
2. Uso de `try`, `except` para manejar excepciones.
3. Bloques `finally` y `else` en el manejo de excepciones.
4. Levantamiento de excepciones con `raise`.
5. Creación de excepciones personalizadas.

### Ejercicios:
1. Creación de un script que simule el proceso de checkout en un ecommerce, pero que pueda generar errores si, por ejemplo, un producto está fuera de stock. Manejar ese error y mostrar un mensaje al usuario.
2. Mejora del script anterior para manejar múltiples tipos de errores: producto fuera de stock, tarjeta de crédito no válida, etc. Utiliza excepciones personalizadas para cada tipo de error.

---

## Proyecto general del backend de ecommerce:
En cada etapa, piensa en cómo cada concepto podría aplicarse a una API para un backend de ecommerce. Por ejemplo:
- Las variables y tipos de datos te ayudarán a definir y manipular la información de productos, usuarios, pedidos, etc.
- Las estructuras de control te permitirán, por ejemplo, aplicar descuentos a ciertos productos si cumplen ciertas condiciones.
- El manejo de errores es fundamental en cualquier backend para manejar situaciones como productos fuera de stock, errores en el pago, entre otros.

Una vez hayas finalizado estos tres días, deberías tener una base sólida de los conceptos fundamentales de Python y cómo se aplican en un contexto de desarrollo backend para ecommerce. A medida que avanzas en tu aprendizaje, irás introduciendo conceptos más avanzados y herramientas específicas para la creación de la API y el manejo de bases de datos.
