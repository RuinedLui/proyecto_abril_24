import csv

encuestados = []

with open("encuesta_restaurantes_10000.csv", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        encuestado = {
            "id": int(fila["id"]),
            "preferencias": {
                "Comida preferida": fila["comida_preferida"],
                "Frecuencia de consumo": fila["frecuencia_consumo"]
            },
            "consumo": {
                "Gasto promedio": float(fila["gasto_promedio"])
            },
            "experiencia": {
                "Producto": int(fila["satisfaccion_producto"]),
                "Servicio": int(fila["satisfaccion_servicio"]),
                "Tiempo de entrega": fila["tiempo_entrega"],
                "Precio": fila["precio_percepcion"]
            },
            "nps": {
                "Recomendación": int(fila["recomendaria"]),
                "Volvería a comprar": fila["volveria_comprar"] == "True",
                "general": int(fila["calificacion_general"])
            }
        }

        encuestados.append(encuestado)

print(f"Total de encuestados cargados: {len(encuestados)}\n")
for encuestado in encuestados[:1]:
    print("=" * 40)
    print(f"  ID: {encuestado['id']}")
    print(f"  preferencias:")
    for clave, valor in encuestado["preferencias"].items():
        print(f"      {clave}: {valor}")
    print(f"  consumo:")
    for clave, valor in encuestado["consumo"].items():
        print(f"      {clave}: {valor}")
    print(f"  experiencia:")
    for clave, valor in encuestado["experiencia"].items():
        print(f"      {clave}: {valor}")
    print(f"  nps:")
    for clave, valor in encuestado["nps"].items():
        print(f"      {clave}: {valor}")
    print("=" * 40)
    print()


#Reporte 1: Cantidad de personas por comida preferida
def reporte_comida_preferida(encuestados):
    personas_por_comida = {}

    for encuestado in encuestados:
        comida = encuestado["preferencias"]["Comida preferida"]

        if comida in personas_por_comida:
            personas_por_comida[comida] += 1
        else:
            personas_por_comida[comida] = 1

    return personas_por_comida
    
reporte1 = reporte_comida_preferida(encuestados)
print("Reporte 1: Cantidad de personas por comida preferida")
for comida, cantidad in reporte1.items():
    print(f"  {comida}: {cantidad} personas prefieren esta comida")
