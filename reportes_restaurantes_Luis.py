import csv

encuestados = []

with open("encuesta_restaurantes_10000.csv", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        encuestado = {
            "id": int(fila["id"]),                     

            # Reporte 12 necesita saber qué comida prefiere cada persona
            "preferencias": {
                "comida": fila["comida_preferida"]
            },

            # Reportes 8 y 12 usan estos tres puntajes (escala 0-10)
            "satisfaccion": {
                "producto": int(fila["satisfaccion_producto"]),
                "servicio": int(fila["satisfaccion_servicio"]),
                "general":  int(fila["calificacion_general"])
            },

            # Reportes 9, 10 y 11 usan estos dos valores
            "nps": {
                "recomendacion": int(fila["recomendaria"]),          # puntaje 0-10 que determina el segmento NPS
                "volveria":      fila["volveria_comprar"] == "True"  # convierte el string "True"/"False" a booleano
            }
        }

        # Agrega el diccionario del encuestado a la lista general
        encuestados.append(encuestado)

print(f"Total de encuestados cargados: {len(encuestados)}\n")

# Imprime el primer registro para confirmar que la estructura quedó bien
for e in encuestados[:1]:
    print("=" * 40)
    print(f"  ID: {e['id']}")
    for seccion in ("preferencias", "satisfaccion", "nps"):
        print(f"  {seccion}:")
        for clave, valor in e[seccion].items():   # .items() recorre clave y valor a la vez
            print(f"      {clave}: {valor}")
    print("=" * 40 + "\n")


# ─── Reporte 8: Promedio general de satisfacción ──────────────────────────────
def reporte_promedio_satisfaccion(encuestados):
    # contadores para sumar todos los puntajes de cada dimensión
    total_producto = 0
    total_servicio = 0
    total_general  = 0
    n = len(encuestados)

    for e in encuestados:
        # Accede al sub-diccionario "satisfaccion" y suma cada puntaje
        total_producto += e["satisfaccion"]["producto"]
        total_servicio += e["satisfaccion"]["servicio"]
        total_general  += e["satisfaccion"]["general"]

    # Divide cada acumulador entre el total de encuestados para obtener el promedio
    # El promedio combinado promedia las tres dimensiones juntas (n * 3 observaciones)
    return {
        "producto":  round(total_producto / n, 2),
        "servicio":  round(total_servicio / n, 2),
        "general":   round(total_general  / n, 2),
        "combinado": round((total_producto + total_servicio + total_general) / (n * 3), 2)
    }

r8 = reporte_promedio_satisfaccion(encuestados)
print("Reporte 8: Promedio general de satisfacción")
print(f"  Producto : {r8['producto']} / 10")
print(f"  Servicio : {r8['servicio']} / 10")
print(f"  General  : {r8['general']}  / 10")
print(f"  Combinado: {r8['combinado']} / 10\n")


# ─── Reporte 9: Porcentaje de clientes que volverían ─────────────────────────
def reporte_volveria(encuestados):
    volverian = 0   # contador de personas que respondieron "sí volvería"

    for e in encuestados:
        # "volveria" ya es booleano, así que se evalúa directamente
        if e["nps"]["volveria"]:
            volverian += 1

    # Calcula qué porcentaje del total representan los que sí volverían
    porcentaje = round((volverian / len(encuestados)) * 100, 2)

    return {
        "volverian":    volverian,
        "no_volverian": len(encuestados) - volverian,  # el resto no volvería
        "porcentaje":   porcentaje
    }

r9 = reporte_volveria(encuestados)
print("Reporte 9: Clientes que volverían a comprar")
print(f"  Sí volverían : {r9['volverian']} personas ({r9['porcentaje']}%)")
print(f"  No volverían : {r9['no_volverian']} personas ({round(100 - r9['porcentaje'], 2)}%)\n")


# ─── Reportes 10 y 11: NPS + Segmentación ────────────────────────────────────
def calcular_nps(encuestados):
    promotores  = 0
    pasivos     = 0
    detractores = 0

    for e in encuestados:
        puntaje = e["nps"]["recomendacion"]

        # Cada persona cae en un rango según su puntaje
        if puntaje >= 9:
            promotores += 1
        elif puntaje >= 7:
            pasivos += 1
        else:
            detractores += 1

    n = len(encuestados)

    # Porcentaje de cada rango sobre el total
    pct_promotores  = round((promotores  / n) * 100, 2)
    pct_pasivos     = round((pasivos     / n) * 100, 2)
    pct_detractores = round((detractores / n) * 100, 2)

    # NPS = %Promotores - %Detractores (los pasivos no entran)
    nps = round(pct_promotores - pct_detractores, 2)

    return {
        "promotores":      promotores,
        "pasivos":         pasivos,
        "detractores":     detractores,
        "pct_promotores":  pct_promotores,
        "pct_pasivos":     pct_pasivos,
        "pct_detractores": pct_detractores,
        "nps":             nps
    }

r10 = calcular_nps(encuestados)

print("Reporte 10: Cálculo del NPS")
print(f"  Promotores  : {r10['promotores']} personas ({r10['pct_promotores']}%)")
print(f"  Pasivos     : {r10['pasivos']} personas ({r10['pct_pasivos']}%)")
print(f"  Detractores : {r10['detractores']} personas ({r10['pct_detractores']}%)")
print(f"  NPS = {r10['nps']} (%Promotores {r10['pct_promotores']} - %Detractores {r10['pct_detractores']})\n")

# Reporte 11 usa los mismos datos que el 10
print("Reporte 11: Segmentación NPS")
print(f"  Promotores  (9-10): {r10['promotores']}  personas ({r10['pct_promotores']}%)")
print(f"  Pasivos     (7-8) : {r10['pasivos']}  personas ({r10['pct_pasivos']}%)")
print(f"  Detractores (0-6) : {r10['detractores']} personas ({r10['pct_detractores']}%)\n")


# ─── Reporte 12: Comida con mayor y menor satisfacción ───────────────────────
def reporte_satisfaccion_por_comida(encuestados):
    # Diccionario: por cada tipo de comida guarda la suma de puntajes y cuántas personas la eligieron
    acumulado = {}

    for e in encuestados:
        comida  = e["preferencias"]["comida"]
        puntaje = e["satisfaccion"]["general"]

        if comida in acumulado:
            # si la comida ya existe, acumula el puntaje y suma una persona más
            acumulado[comida]["suma"]   += puntaje
            acumulado[comida]["conteo"] += 1
        else:
            # sio es la rimera vez que aparece esta comida inicializa su entrada
            acumulado[comida] = {"suma": puntaje, "conteo": 1}

    # convierte suma/conteo en promedio para cada comida
    promedios = {}
    for comida, datos in acumulado.items():
        promedios[comida] = round(datos["suma"] / datos["conteo"], 2)

    # Busca la comida con el promedio más alto comparando números directamente
    mayor = ""
    mejor_promedio = 0
    for comida, promedio in promedios.items():
        if promedio > mejor_promedio:
            mayor = comida
            mejor_promedio = promedio

    return {"mayor": mayor, "promedio": promedios[mayor]}

r12 = reporte_satisfaccion_por_comida(encuestados)
print("Reporte 12: Comida con mayor satisfacción")
print(f"  {r12['mayor']} con un promedio de {r12['promedio']} / 10\n")