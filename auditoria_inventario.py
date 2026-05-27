
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Problema 3 - Auditoría de Inventario
# Autor: Richard Mendoza de los Reyes
# MATRIZ DE INVENTARIO
# [Código, Nombre, Stock Actual, Stock Mínimo]

inventario = [
    [101, "Reloj", 4, 10],
    [102, "Cadenas", 12, 10],
    [103, "Pulseras", 3, 8],
    [104, "Anillos", 7, 7],
    [105, "Aretes", 2, 6]
]

# FUNCIÓN PARA CALCULAR LA CANTIDAD A PEDIR


def calcular_cantidad_pedir(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad


# PROGRAMA PRINCIPAL


print("              AUDITORÍA DE INVENTARIO               ")
print("          LISTA DE REABASTECIMIENTO                 ")

print(f"{'ARTÍCULO':<20} {'ESTADO':<25}")

# RECORRER MATRIZ

for articulo in inventario:

    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # FUNCIÓN
    cantidad_pedir = calcular_cantidad_pedir(
        stock_actual,
        stock_minimo
    )

    # IMPRIMIR SI REQUIERE REABASTECIMIENTO
    # O MOSTRAR STOCK OK

    if cantidad_pedir > 0:
        print(f"{nombre:<20} Pedir {cantidad_pedir} unidades")

    else:
        print(f"{nombre:<20} Stock OK")

print("====================================================")
