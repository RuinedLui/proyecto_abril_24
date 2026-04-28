import csv

# ─────────────────────────────────────────────
# 1. LECTURA Y CONSTRUCCIÓN DE ESTRUCTURAS
# ─────────────────────────────────────────────

encuestados = []

with open("encuesta_restaurantes_10000.csv", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        encuestado = {
            "id": int(fila["id"]),
            "preferencias": {
                "comida": fila["comida_preferida"],
                "frecuencia": fila["frecuencia_consumo"]
            },
            "consumo": {
                "gasto": float(fila["gasto_promedio"])
            },
            "experiencia": {
                "producto": int(fila["satisfaccion_producto"]),
                "servicio": int(fila["satisfaccion_servicio"]),
                "tiempo": fila["tiempo_entrega"],
                "precio": fila["precio_percepcion"]
            },
            "nps": {
                "recomendacion": int(fila["recomendaria"]),
                "volveria": fila["volveria_comprar"] == "True",
                "general": int(fila["calificacion_general"])
            }
        }
        encuestados.append(encuestado)

total = len(encuestados)

# ─────────────────────────────────────────────
# REPORTE 1: Cantidad de personas por comida preferida
# ─────────────────────────────────────────────

conteo_comida = {}
for e in encuestados:
    comida = e["preferencias"]["comida"]
    if comida in conteo_comida:
        conteo_comida[comida] += 1
    else:
        conteo_comida[comida] = 1

print("=" * 55)
print("REPORTE 1: Cantidad de personas por comida preferida")
print("=" * 55)
for comida, cantidad in sorted(conteo_comida.items(), key=lambda x: -x[1]):
    print(f"  {comida:<20} {cantidad:>5} personas")

# ─────────────────────────────────────────────
# REPORTE 2: Frecuencia de consumo
# ─────────────────────────────────────────────

conteo_frecuencia = {}
for e in encuestados:
    freq = e["preferencias"]["frecuencia"]
    if freq in conteo_frecuencia:
        conteo_frecuencia[freq] += 1
    else:
        conteo_frecuencia[freq] = 1

print("\n" + "=" * 55)
print("REPORTE 2: Frecuencia de consumo")
print("=" * 55)
for freq, cantidad in sorted(conteo_frecuencia.items(), key=lambda x: -x[1]):
    pct = cantidad / total * 100
    print(f"  {freq:<20} {cantidad:>5} ({pct:.1f}%)")

# ─────────────────────────────────────────────
# REPORTE 3: Promedio de gasto
# ─────────────────────────────────────────────

suma_gasto = 0
for e in encuestados:
    suma_gasto += e["consumo"]["gasto"]
promedio_gasto = suma_gasto / total

print("\n" + "=" * 55)
print("REPORTE 3: Promedio de gasto por consumo")
print("=" * 55)
print(f"  Promedio general: ${promedio_gasto:.2f}")

# ─────────────────────────────────────────────
# REPORTE 4: Promedio de satisfacción del producto
# ─────────────────────────────────────────────

suma_prod = 0
for e in encuestados:
    suma_prod += e["experiencia"]["producto"]
promedio_prod = suma_prod / total

print("\n" + "=" * 55)
print("REPORTE 4: Promedio de satisfacción del producto")
print("=" * 55)
print(f"  Promedio: {promedio_prod:.2f} / 10")

# ─────────────────────────────────────────────
# REPORTE 5: Promedio de satisfacción del servicio
# ─────────────────────────────────────────────

suma_serv = 0
for e in encuestados:
    suma_serv += e["experiencia"]["servicio"]
promedio_serv = suma_serv / total

print("\n" + "=" * 55)
print("REPORTE 5: Promedio de satisfacción del servicio")
print("=" * 55)
print(f"  Promedio: {promedio_serv:.2f} / 10")

# ─────────────────────────────────────────────
# REPORTE 6: Distribución del tiempo de entrega
# ─────────────────────────────────────────────

conteo_tiempo = {}
for e in encuestados:
    t = e["experiencia"]["tiempo"]
    if t in conteo_tiempo:
        conteo_tiempo[t] += 1
    else:
        conteo_tiempo[t] = 1

print("\n" + "=" * 55)
print("REPORTE 6: Distribución del tiempo de entrega")
print("=" * 55)
for t, cantidad in sorted(conteo_tiempo.items(), key=lambda x: -x[1]):
    pct = cantidad / total * 100
    print(f"  {t:<20} {cantidad:>5} ({pct:.1f}%)")

# ─────────────────────────────────────────────
# REPORTE 7: Distribución de percepción de precios
# ─────────────────────────────────────────────

conteo_precio = {}
for e in encuestados:
    p = e["experiencia"]["precio"]
    if p in conteo_precio:
        conteo_precio[p] += 1
    else:
        conteo_precio[p] = 1

print("\n" + "=" * 55)
print("REPORTE 7: Distribución de percepción de precios")
print("=" * 55)
for p, cantidad in sorted(conteo_precio.items(), key=lambda x: -x[1]):
    pct = cantidad / total * 100
    print(f"  {p:<20} {cantidad:>5} ({pct:.1f}%)")

# ─────────────────────────────────────────────
# REPORTE 8: Promedio general de satisfacción
# ─────────────────────────────────────────────

suma_general = 0
for e in encuestados:
    suma_general += e["nps"]["general"]
promedio_general = suma_general / total

print("\n" + "=" * 55)
print("REPORTE 8: Promedio general de satisfacción")
print("=" * 55)
print(f"  Promedio: {promedio_general:.2f} / 10")

# ─────────────────────────────────────────────
# REPORTE 9: Porcentaje de clientes que volverían
# ─────────────────────────────────────────────

volverian = 0
for e in encuestados:
    if e["nps"]["volveria"]:
        volverian += 1
pct_volverian = volverian / total * 100

print("\n" + "=" * 55)
print("REPORTE 9: Clientes que volverían a comprar")
print("=" * 55)
print(f"  Sí volverían: {volverian} ({pct_volverian:.1f}%)")
print(f"  No volverían: {total - volverian} ({100 - pct_volverian:.1f}%)")

# ─────────────────────────────────────────────
# REPORTE 10 & 11: NPS y Segmentación
# ─────────────────────────────────────────────

promotores = 0
pasivos = 0
detractores = 0

for e in encuestados:
    rec = e["nps"]["recomendacion"]
    if rec >= 9:
        promotores += 1
    elif rec >= 7:
        pasivos += 1
    else:
        detractores += 1

pct_promotores = promotores / total * 100
pct_pasivos = pasivos / total * 100
pct_detractores = detractores / total * 100
nps = pct_promotores - pct_detractores

print("\n" + "=" * 55)
print("REPORTE 10: Cálculo del NPS")
print("=" * 55)
print(f"  NPS = {nps:.1f}")

print("\n" + "=" * 55)
print("REPORTE 11: Segmentación de clientes")
print("=" * 55)
print(f"  Promotores  (9-10): {promotores:>5} ({pct_promotores:.1f}%)")
print(f"  Pasivos     (7-8):  {pasivos:>5} ({pct_pasivos:.1f}%)")
print(f"  Detractores (0-6):  {detractores:>5} ({pct_detractores:.1f}%)")

# ─────────────────────────────────────────────
# REPORTE 12 & 13: Comida con mayor y menor satisfacción
# ─────────────────────────────────────────────

satisfaccion_comida = {}
conteo_comida2 = {}

for e in encuestados:
    comida = e["preferencias"]["comida"]
    sat = (e["experiencia"]["producto"] + e["experiencia"]["servicio"] + e["nps"]["general"]) / 3
    if comida in satisfaccion_comida:
        satisfaccion_comida[comida] += sat
        conteo_comida2[comida] += 1
    else:
        satisfaccion_comida[comida] = sat
        conteo_comida2[comida] = 1

promedio_sat_comida = {}
for comida in satisfaccion_comida.keys():
    promedio_sat_comida[comida] = satisfaccion_comida[comida] / conteo_comida2[comida]

comida_max = max(promedio_sat_comida, key=lambda x: promedio_sat_comida[x])
comida_min = min(promedio_sat_comida, key=lambda x: promedio_sat_comida[x])

print("\n" + "=" * 55)
print("REPORTE 12: Comida con mayor satisfacción")
print("=" * 55)
print(f"  {comida_max} — Promedio: {promedio_sat_comida[comida_max]:.2f}")

print("\n" + "=" * 55)
print("REPORTE 13: Comida con menor satisfacción")
print("=" * 55)
print(f"  {comida_min} — Promedio: {promedio_sat_comida[comida_min]:.2f}")

# ─────────────────────────────────────────────
# REPORTE 14: Relación entre gasto y satisfacción
# ─────────────────────────────────────────────

rangos_gasto = {"Bajo ($0-$33)": [], "Medio ($34-$66)": [], "Alto ($67-$100)": []}

for e in encuestados:
    gasto = e["consumo"]["gasto"]
    sat = (e["experiencia"]["producto"] + e["experiencia"]["servicio"] + e["nps"]["general"]) / 3
    if gasto <= 33:
        rangos_gasto["Bajo ($0-$33)"].append(sat)
    elif gasto <= 66:
        rangos_gasto["Medio ($34-$66)"].append(sat)
    else:
        rangos_gasto["Alto ($67-$100)"].append(sat)

print("\n" + "=" * 55)
print("REPORTE 14: Relación entre gasto y satisfacción")
print("=" * 55)
for rango, valores in rangos_gasto.items():
    prom = sum(valores) / len(valores) if valores else 0
    print(f"  {rango:<22} Satisfacción promedio: {prom:.2f}")

# ─────────────────────────────────────────────
# REPORTE 15: Frecuencia vs satisfacción
# ─────────────────────────────────────────────

frec_sat = {}
frec_cnt = {}
for e in encuestados:
    freq = e["preferencias"]["frecuencia"]
    sat = (e["experiencia"]["producto"] + e["experiencia"]["servicio"] + e["nps"]["general"]) / 3
    if freq in frec_sat:
        frec_sat[freq] += sat
        frec_cnt[freq] += 1
    else:
        frec_sat[freq] = sat
        frec_cnt[freq] = 1

print("\n" + "=" * 55)
print("REPORTE 15: Frecuencia de consumo vs satisfacción")
print("=" * 55)
for freq in frec_sat.keys():
    prom = frec_sat[freq] / frec_cnt[freq]
    print(f"  {freq:<15} Satisfacción promedio: {prom:.2f}")

# ─────────────────────────────────────────────
# REPORTE 16: Precio vs recomendación
# ─────────────────────────────────────────────

precio_rec = {}
precio_cnt = {}
for e in encuestados:
    precio = e["experiencia"]["precio"]
    rec = e["nps"]["recomendacion"]
    if precio in precio_rec:
        precio_rec[precio] += rec
        precio_cnt[precio] += 1
    else:
        precio_rec[precio] = rec
        precio_cnt[precio] = 1

print("\n" + "=" * 55)
print("REPORTE 16: Percepción de precio vs recomendación")
print("=" * 55)
for precio in precio_rec.keys():
    prom = precio_rec[precio] / precio_cnt[precio]
    print(f"  Precio {precio:<10} Recomendación promedio: {prom:.2f}")

# ─────────────────────────────────────────────
# REPORTE 17: Tiempo de entrega vs satisfacción
# ─────────────────────────────────────────────

tiempo_sat = {}
tiempo_cnt = {}
for e in encuestados:
    tiempo = e["experiencia"]["tiempo"]
    sat = (e["experiencia"]["producto"] + e["experiencia"]["servicio"] + e["nps"]["general"]) / 3
    if tiempo in tiempo_sat:
        tiempo_sat[tiempo] += sat
        tiempo_cnt[tiempo] += 1
    else:
        tiempo_sat[tiempo] = sat
        tiempo_cnt[tiempo] = 1

print("\n" + "=" * 55)
print("REPORTE 17: Tiempo de entrega vs satisfacción")
print("=" * 55)
for tiempo in tiempo_sat.keys():
    prom = tiempo_sat[tiempo] / tiempo_cnt[tiempo]
    print(f"  {tiempo:<15} Satisfacción promedio: {prom:.2f}")

# ─────────────────────────────────────────────
# REPORTE 18: Ranking de comidas más consumidas
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("REPORTE 18: Ranking de comidas más consumidas")
print("=" * 55)
ranking = sorted(conteo_comida.items(), key=lambda x: -x[1])
for i, (comida, cantidad) in enumerate(ranking, 1):
    pct = cantidad / total * 100
    print(f"  {i}. {comida:<20} {cantidad:>5} ({pct:.1f}%)")

# ─────────────────────────────────────────────
# REPORTE 19: Promedio general por tipo de comida
# ─────────────────────────────────────────────

datos_comida = {}
for e in encuestados:
    comida = e["preferencias"]["comida"]
    if comida not in datos_comida:
        datos_comida[comida] = {
            "gasto": [], "producto": [], "servicio": [],
            "recomendacion": [], "general": []
        }
    for key in datos_comida[comida].keys():
        if key == "gasto":
            datos_comida[comida][key].append(e["consumo"]["gasto"])
        elif key in ("producto", "servicio"):
            datos_comida[comida][key].append(e["experiencia"][key])
        else:
            datos_comida[comida][key].append(e["nps"][key])

print("\n" + "=" * 55)
print("REPORTE 19: Promedio general por tipo de comida")
print("=" * 55)
print(f"  {'Comida':<20} {'Gasto':>7} {'Prod':>6} {'Serv':>6} {'Rec':>6} {'Gen':>6}")
print("  " + "-" * 53)
for comida, vals in sorted(datos_comida.items()):
    g = sum(vals["gasto"]) / len(vals["gasto"])
    p = sum(vals["producto"]) / len(vals["producto"])
    s = sum(vals["servicio"]) / len(vals["servicio"])
    r = sum(vals["recomendacion"]) / len(vals["recomendacion"])
    gn = sum(vals["general"]) / len(vals["general"])
    print(f"  {comida:<20} ${g:>6.1f} {p:>6.2f} {s:>6.2f} {r:>6.2f} {gn:>6.2f}")

# ─────────────────────────────────────────────
# REPORTE 20: Perfil del cliente promedio
# ─────────────────────────────────────────────

comida_freq = max(conteo_comida, key=lambda x: conteo_comida[x])
frecuencia_freq = max(conteo_frecuencia, key=lambda x: conteo_frecuencia[x])
tiempo_freq = max(conteo_tiempo, key=lambda x: conteo_tiempo[x])
precio_freq = max(conteo_precio, key=lambda x: conteo_precio[x])

print("\n" + "=" * 55)
print("REPORTE 20: Perfil del cliente promedio")
print("=" * 55)
print(f"  Comida preferida:        {comida_freq}")
print(f"  Frecuencia de consumo:   {frecuencia_freq}")
print(f"  Gasto promedio:          ${promedio_gasto:.2f}")
print(f"  Satisfacción producto:   {promedio_prod:.2f}/10")
print(f"  Satisfacción servicio:   {promedio_serv:.2f}/10")
print(f"  Tiempo de entrega:       {tiempo_freq}")
print(f"  Percepción de precio:    {precio_freq}")
print(f"  Calificación general:    {promedio_general:.2f}/10")
print(f"  Volvería a comprar:      {'Sí' if pct_volverian >= 50 else 'No'} ({pct_volverian:.1f}%)")
print(f"  NPS del restaurante:     {nps:.1f}")

print("\n" + "=" * 55)
