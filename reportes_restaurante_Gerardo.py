import csv 

with open("encuesta_restaurantes_10000.csv", 'r', encoding='utf-8') as archivo:
    reader = csv.DictReader(archivo)
    filas = list(reader)

encuestados = []

for fila in filas:
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
            "volveria": fila["volveria_comprar"].strip().lower() == "true",
            "general": int(fila["calificacion_general"])
        }
    }
    encuestados.append(encuestado)
cantidad_total = len(encuestados)


# Reporte 1 - Cantidad de personas por comida preferida

print("=" * 55)
print("Reporte 1 - Cantidad de personas por comida preferida")
print("=" * 55)

comidas = {}
for encuestado in encuestados:
    comida = encuestado["preferencias"]["comida"]
    if comida in comidas:
        comidas[comida] += 1
    else:
        comidas[comida] = 1

comidas_ordenadas = sorted(comidas.items(), key=lambda x: x[1], reverse=True)

print(f"{'Comida':<22} {'Cantidad':>10} {'Porcentaje':>12}")
print("-" * 47)
for comida, cantidad in comidas_ordenadas:
    porcentaje = (cantidad / cantidad_total) * 100
    print(f"{comida:<22} {cantidad:>10} {porcentaje:>11.2f}%")
print("-" * 47)
print(f"{'TOTAL':<22} {cantidad_total:>10} {'100.00%':>12}")
        

# Reporte 2 - Frecuencia de consumo

print("\n" + "=" * 55)
print("Reporte 2 - Frecuencia de consumo")
print("=" * 55)

frecuencias = {}
for encuestado in encuestados:
    frecuencia = encuestado["preferencias"]["frecuencia"]
    if frecuencia in frecuencias:
        frecuencias[frecuencia] += 1
    else:
        frecuencias[frecuencia] = 1

frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

print(f"{'Frecuencia':<22} {'Cantidad':>10} {'Porcentaje':>12}")
print("=" * 47)
for frecuencia, cantidad in frecuencias_ordenadas:
    porcentaje = (cantidad / cantidad_total) * 100
    print(f"{frecuencia:<22} {cantidad:>10} {porcentaje:>11.2f}%")
print("-" * 47)
print(f"{'TOTAL':<22} {cantidad_total:>10} {'100.00%':>12}")
        

# Reporte 3 - Promedio de gasto 

print("\n" + "=" * 55)
print("Reporte 3 - Promedio de gasto")
print("=" * 55)

suma_gasto = 0.0
for encuestado in encuestados:
    suma_gasto += encuestado["consumo"]["gasto"]

promedio_gasto = suma_gasto / cantidad_total

print(f"{'Indicador':<30} {'Valor':>12}")
print("-" * 55)
print(f"{'Total encuestados':<30} {cantidad_total:>12}")
print(f"{'Suma total de gastos':<30} {round(suma_gasto, 2):>12}")
print(f"Gasto promedio: {round(promedio_gasto, 2):>12}")
print("=" * 55)


# Reporte 4 - Promedio de satisfaccion del producto

print("\n" + "=" * 55)
print("Reporte 4 - Promedio de satisfaccion del producto")
print("=" * 55)

sat_producto = {}

for encuestado in encuestados:
    comida = encuestado["preferencias"]["comida"]
    producto = encuestado["experiencia"]["producto"]

    if comida not in sat_producto:
        sat_producto[comida] = {"suma": 0.0, "conteo": 0}

    sat_producto[comida]["suma"] += producto
    sat_producto[comida]["conteo"] += 1

sat_producto_ord = sorted(
    sat_producto.items(),
    key=lambda x: x[1]["suma"] / x[1]["conteo"],
    reverse=True
)

print(f"{'Comida':<25} {'Encuestados':>12} {'Prom. Satisfaccion':>20}")
print("-" * 60)
for comida, datos in sat_producto_ord:
    promedio = datos["suma"] / datos["conteo"]
    print(f"{comida:<25} {datos['conteo']:>12} {round(promedio, 2):>20}")
print("-" * 60)

# Promedio general final
suma_total = sum(d["suma"] for _, d in sat_producto.items())
conteo_total = sum(d["conteo"] for _, d in sat_producto.items())
print(f"{'PROMEDIO GENERAL':<25} {conteo_total:>12} {round(suma_total / conteo_total, 2):>20}")
print("=" * 55)


# Reporte 5 - Promedio de satisfaccion del servicio

print("\n" + "=" * 55)
print("Reporte 5 - Promedio de satisfaccion del servicio")
print("=" * 55)

suma_servicio = 0.0
for encuestado in encuestados:
    suma_servicio += encuestado["experiencia"]["servicio"]

promedio_servicio = suma_servicio / cantidad_total

print(f"{'Indicador':<30} {'Valor':>12}")
print("-" * 45)
print(f"{'Total encuestados':<30} {cantidad_total:>12}")
print(f"{'Promedio Satisfaccion servicio':<30} {round(promedio_servicio, 2):>12}")
print("=" * 55)


# Reporte 6 - Distribución del tiempo de entrega

print("\n" + "=" * 55)
print("Reporte 6 - Distribución del tiempo de entrega")
print("=" * 55)

tiempos = {}
for encuestado in encuestados:
    tiempo = encuestado["experiencia"]["tiempo"]
    if tiempo in tiempos:
        tiempos[tiempo] += 1
    else: 
        tiempos[tiempo] = 1

tiempos_ordenados = sorted(tiempos.items(), key=lambda x: x[1], reverse=True)

print(f"{'Tiempo de entrega':<22} {'Cantidad':>10} {'Porcentaje':>12}")
print("-" * 47)
for tiempo, cantidad in tiempos_ordenados:
    porcentaje = (cantidad / cantidad_total) * 100
    print(f"{tiempo:<22} {cantidad:>10} {porcentaje:>11.2f}%")
print("-" * 47)
print(f"{'TOTAL':22} {cantidad_total:>10} {'100.00%':>12}")


# Reporte 7 - Distribución de percepción de precios

print("\n" + "=" * 55)
print("Reporte 7 - Distribución del tiempo de entrega")
print("=" * 55)

precios = {}

for encuestado in encuestados:
    precio = encuestado["experiencia"]["precio"]
    if precio in precios:
        precios[precio] += 1
    else: 
        precios[precio] = 1

precios_ordenados = sorted(precios.items(), key=lambda x: x[1], reverse=True)

print(f"{'Percepcion de precio':<22} {'Cantidad':>10} {'Porcentaje':>12}")
print("-" * 47)
for precio, cantidad in precios_ordenados:
    porcentaje = (cantidad / cantidad_total) * 100
    print(f"{precio:<22} {cantidad:>10} {porcentaje:>11.2f}%")
print("-" * 47)
print(f"{'TOTAL':<22} {cantidad_total:>10} {'100.00%':>12}")


# Reporte 8 - Promedio general de satisfacción

print("\n" + "=" * 55)
print("Reporte 8 - Promedio general de satisfacción")
print("=" * 55)

suma_general = 0.0
for encuestado in encuestados:
    suma_general += encuestado["nps"]["general"]

promedio_general = suma_general / cantidad_total

print(f"{'Indicador':<30} {'Valor':>12}")
print('-' * 45)
print(f"{'Total encuestados':<30} {cantidad_total:>12}")
print(f"{'Promedio calificacion general':<30} {round(promedio_general, 2):>12}")
print("=" * 55)

# Reporte 9 - Porcentaje de clientes que volverían

print("\n" + "=" * 55)
print("Reporte 9 - Porcentaje de clientes que volverían")
print("=" * 55)

volveria_si = 0
volveria_no = 0

for encuestado in encuestados:
    if encuestado["nps"]["volveria"]:
        volveria_si += 1
    else:
        volveria_no += 1

pct_si = (volveria_si / cantidad_total) * 100
pct_no = (volveria_no / cantidad_total) * 100

print(f"{'Categoría':<22} {'Cantidad':>10} {'Porcentaje':>12}")
print("-" * 47)
print(f"{'Sí volvería':<22} {volveria_si:>10} {pct_si:>11.2f}%")
print(f"{'No volvería':<22} {volveria_no:>10} {pct_no:>11.2f}%")
print("-" * 47)
print(f"{'TOTAL':<22} {cantidad_total:>10} {'100.00%':>12}")


# Reporte 10 - Cálculo del NPS

print("\n" + "=" * 55)
print("Reporte 10 - Cálculo del NPS")
print("=" * 55)

promotores = 0
pasivos = 0 
detractores = 0 

for encuestado in encuestados: 
    rec = encuestado["nps"]["recomendacion"]
    if rec >= 9:
        promotores += 1
    elif rec >= 7:
        pasivos += 1
    else:
        detractores += 1

pct_promotores = (promotores / cantidad_total) * 100
pct_pasivos = (pasivos / cantidad_total) * 100 
pct_detractores = (detractores / cantidad) * 100

nps = round(pct_promotores - pct_detractores, 2) 

print(f"{'Segmento':<22} {'Cantidad':>10} {'Porcentaje'}")
print("-" * 47)
print(f"{'Promotores (9-10)':<22} {promotores:>10} {pct_promotores:>11.2f}%")
print(f"{'Pasivos (7-8)':<22} {pasivos:>10} {pct_pasivos:>11.2f}%")
print(f"{'Detractores (0-6)':<22} {detractores:>10} {pct_detractores:>11.2f}%")
print("-" * 47)
print(f"{'NPS = %Promotores - %Detractores':<35} {nps:>8}")
print("=" * 55)


# Reporte 11 - Segmentación: promotores, pasivos, detractores

print("\n" + "=" * 55)
print("Reporte 11 - Segmentación: promotores, pasivos, detractores")
print("=" * 55)

segmentos_comida = {}

for encuestado in encuestados:
    comida = encuestado["preferencias"]["comida"]
    rec = encuestado["nps"]["recomendacion"]

    if comida not in segmentos_comida:
        segmentos_comida[comida] = {"promotores": 0, "pasivos": 0, "detractores": 0, "total": 0}

    segmentos_comida[comida]["total"] += 1

    if rec >= 9:
        segmentos_comida[comida]["promotores"] += 1
    elif rec >= 7: 
        segmentos_comida[comida]["pasivos"] += 1
    else:
        segmentos_comida[comida]["detractores"] += 1

print(f"{'Comida':<18} {'Total':>6} {'Prom%':>7} {'Pas%':>7} {'Det%':>7} {'NPS':>7}")
print("-" * 57)

for comida, datos in segmentos_comida.items():
    n = datos["total"]
    p = round((datos["promotores"] / n) * 100, 1)
    pa = round((datos["pasivos"] / n) * 100, 1)
    d = round((datos["detractores"] / n) * 100, 1)
    nps_comida = round(p - d, 1)
    print(f"{comida:<18} {n:>6} {p:>7} {pa:>7} {d:>7} {nps_comida:>7}")

print("=" * 55)

# Reporte 12 - Comida con mayor satisfacción

print("\n" + "=" * 55)
print("Reporte 12 - Comida con mayor satisfacción")
print("=" * 55)

sat_por_comida = {}

for encuestado in encuestados:
    comida = encuestado["preferencias"]["comida"]
    if comida not in sat_por_comida:
        sat_por_comida[comida] = {'suma': 0, 'conteo': 0}
    sat_por_comida[comida]["suma"] += encuestado["nps"]["general"]
    sat_por_comida[comida]["conteo"] += 1

mejor_comida = None
mejor_promedio = -1.0

for comida, datos in sat_por_comida.items():
    prom = datos["suma"] / datos["conteo"]
    if prom > mejor_promedio:
        mejor_promedio = prom
        mejor_comida = comida

print(f"Comida con mayor satisfaccion: {mejor_comida}")
print(f"Promedio de calificacion general: {round(promedio_general, 2)}")
print("=" * 55)


# Reporte 13 - Comida con menor satisfaccion

print("\n" + "=" * 55)
print("Reporte 13 - Comida con menor satisfacción")
print("=" * 55)

peor_comida = None
peor_promedio = float("inf")

for comida, datos in sat_por_comida.items():
    prom = datos["suma"] / datos["conteo"]
    if prom < peor_promedio:
        peor_promedio = prom
        peor_comida   = comida

print(f"Comida con menor satisfacción: {peor_comida}")
print(f"Promedio de calificación general: {round(peor_promedio, 2)}")
print("=" * 55)

#  Reporte 14 - Relación entre gasto y satisfacción

print("\n" + "=" * 55)
print("Reporte 14 - Relación entre gasto y satisfacción")
print("=" * 55)

# Agrupamos por nivel de satisfacción general (1-10)
gasto_por_sat = {}

for encuestado in encuestados:
    sat   = encuestado["nps"]["general"]
    gasto = encuestado["consumo"]["gasto"]

    if sat not in gasto_por_sat:
        gasto_por_sat[sat] = {"suma": 0.0, "conteo": 0}

    gasto_por_sat[sat]["suma"]   += gasto
    gasto_por_sat[sat]["conteo"] += 1

gasto_por_sat_ord = sorted(gasto_por_sat.items())

print(f"{'Satisfacción':<15} {'Encuestados':>12} {'Gasto promedio':>15}")
print("-" * 45)
for sat, datos in gasto_por_sat_ord:
    prom = datos["suma"] / datos["conteo"]
    print(f"{sat:<15} {datos['conteo']:>12} {round(prom, 2):>15}")
print("=" * 55)



# Reporte 15 - Frecuencia vs satisfacción

print("\n" + "=" * 55)
print("Reporte 15 - Frecuencia de consumo vs satisfacción")
print("=" * 55)

frec_vs_sat = {}

for encuestado in encuestados:
    frec = encuestado["preferencias"]["frecuencia"]
    sat  = encuestado["nps"]["general"]

    if frec not in frec_vs_sat:
        frec_vs_sat[frec] = {"suma": 0.0, "conteo": 0}

    frec_vs_sat[frec]["suma"]   += sat
    frec_vs_sat[frec]["conteo"] += 1

frec_vs_sat_ord = sorted(frec_vs_sat.items(), key=lambda x: x[1]["suma"] / x[1]["conteo"], reverse=True)

print(f"{'Frecuencia':<22} {'Encuestados':>12} {'Sat. promedio':>14}")
print("-" * 51)
for frec, datos in frec_vs_sat_ord:
    prom = datos["suma"] / datos["conteo"]
    print(f"{frec:<22} {datos['conteo']:>12} {round(prom, 2):>14}")
print("=" * 55)



# Reporte 16 - Precio vs recomendación

print("\n" + "=" * 55)
print("Reporte 16 - Percepción de precio vs recomendación")
print("=" * 55)

precio_vs_rec = {}

for encuestado in encuestados:
    precio = encuestado["experiencia"]["precio"]
    rec    = encuestado["nps"]["recomendacion"]

    if precio not in precio_vs_rec:
        precio_vs_rec[precio] = {"suma": 0.0, "conteo": 0}

    precio_vs_rec[precio]["suma"]   += rec
    precio_vs_rec[precio]["conteo"] += 1

precio_vs_rec_ord = sorted(precio_vs_rec.items(), key=lambda x: x[1]["suma"] / x[1]["conteo"], reverse=True)

print(f"{'Percepción precio':<22} {'Encuestados':>12} {'Rec. promedio':>14}")
print("-" * 51)
for precio, datos in precio_vs_rec_ord:
    prom = datos["suma"] / datos["conteo"]
    print(f"{precio:<22} {datos['conteo']:>12} {round(prom, 2):>14}")
print("=" * 55)



# Reporte 17 - Tiempo de entrega vs satisfacción

print("\n" + "=" * 55)
print("Reporte 17 - Tiempo de entrega vs satisfacción")
print("=" * 55)

tiempo_vs_sat = {}

for encuestado in encuestados:
    tiempo = encuestado["experiencia"]["tiempo"]
    sat    = encuestado["nps"]["general"]

    if tiempo not in tiempo_vs_sat:
        tiempo_vs_sat[tiempo] = {"suma": 0.0, "conteo": 0}

    tiempo_vs_sat[tiempo]["suma"]   += sat
    tiempo_vs_sat[tiempo]["conteo"] += 1

tiempo_vs_sat_ord = sorted(tiempo_vs_sat.items(), key=lambda x: x[1]["suma"] / x[1]["conteo"], reverse=True)

print(f"{'Tiempo de entrega':<22} {'Encuestados':>12} {'Sat. promedio':>14}")
print("-" * 51)
for tiempo, datos in tiempo_vs_sat_ord:
    prom = datos["suma"] / datos["conteo"]
    print(f"{tiempo:<22} {datos['conteo']:>12} {round(prom, 2):>14}")
print("=" * 55)



# Reporte 18 - Ranking de comidas más consumidas

print("\n" + "=" * 55)
print("Reporte 18 - Ranking de comidas más consumidas")
print("=" * 55)

ranking = sorted(comidas.items(), key=lambda x: x[1], reverse=True)

print(f"{'#':<4} {'Comida':<22} {'Cantidad':>10} {'Porcentaje':>12}")
print("-" * 51)
for i, (comida, cantidad) in enumerate(ranking, start=1):
    porcentaje = (cantidad / cantidad_total) * 100
    print(f"{i:<4} {comida:<22} {cantidad:>10} {porcentaje:>11.2f}%")
print("=" * 55)



# Reporte 19 - Promedio general por tipo de comida

print("\n" + "=" * 55)
print("Reporte 19 - Promedio general por tipo de comida")
print("=" * 55)

por_comida_completo = {}

for encuestado in encuestados:
    comida = encuestado["preferencias"]["comida"]

    if comida not in por_comida_completo:
        por_comida_completo[comida] = {
            "suma_producto": 0.0,
            "suma_servicio": 0.0,
            "suma_rec":      0.0,
            "suma_general":  0.0,
            "suma_gasto":    0.0,
            "conteo":        0
        }

    por_comida_completo[comida]["suma_producto"] += encuestado["experiencia"]["producto"]
    por_comida_completo[comida]["suma_servicio"] += encuestado["experiencia"]["servicio"]
    por_comida_completo[comida]["suma_rec"]      += encuestado["nps"]["recomendacion"]
    por_comida_completo[comida]["suma_general"]  += encuestado["nps"]["general"]
    por_comida_completo[comida]["suma_gasto"]    += encuestado["consumo"]["gasto"]
    por_comida_completo[comida]["conteo"]        += 1

resultados_19 = []
for comida, datos in por_comida_completo.items():
    n = datos["conteo"]
    if n > 0:
        resultados_19.append({
            "comida":        comida,
            "conteo":        n,
            "prom_producto": round(datos["suma_producto"] / n, 2),
            "prom_servicio": round(datos["suma_servicio"] / n, 2),
            "prom_rec":      round(datos["suma_rec"]      / n, 2),
            "prom_general":  round(datos["suma_general"]  / n, 2),
            "prom_gasto":    round(datos["suma_gasto"]    / n, 2),
        })

resultados_19 = sorted(resultados_19, key=lambda x: x["prom_general"], reverse=True)

print(f"{'Comida':<18} {'N':>5} {'Prod.':>6} {'Serv.':>6} {'Rec.':>6} {'Gral.':>6} {'Gasto':>8}")
print("-" * 58)
for r in resultados_19:
    print(
        f"{r['comida']:<18} {r['conteo']:>5} "
        f"{r['prom_producto']:>6} {r['prom_servicio']:>6} "
        f"{r['prom_rec']:>6} {r['prom_general']:>6} {r['prom_gasto']:>8}"
    )
print("=" * 55)



# Reporte 20 - Perfil del cliente promedio

print("\n" + "=" * 55)
print("Reporte 20 - Perfil del cliente promedio")
print("=" * 55)

# Comida más frecuente
comida_top = max(comidas.items(), key=lambda x: x[1])[0]

# Frecuencia más común
frecuencia_top = max(frecuencias.items(), key=lambda x: x[1])[0]

# Tiempo de entrega más común
tiempo_top = max(tiempos.items(), key=lambda x: x[1])[0]

# Percepción de precio más común
precio_top = max(precios.items(), key=lambda x: x[1])[0]

# Promedios generales
suma_prod = suma_serv = suma_rec2 = suma_gen2 = 0.0
volveria_count = 0

for encuestado in encuestados:
    suma_prod      += encuestado["experiencia"]["producto"]
    suma_serv      += encuestado["experiencia"]["servicio"]
    suma_rec2      += encuestado["nps"]["recomendacion"]
    suma_gen2      += encuestado["nps"]["general"]
    if encuestado["nps"]["volveria"]:
        volveria_count += 1

print(f"  {'Comida preferida más común':<35} {comida_top}")
print(f"  {'Frecuencia de consumo más común':<35} {frecuencia_top}")
print(f"  {'Gasto promedio':<35} ${round(suma_gasto / cantidad_total, 2)}")
print(f"  {'Satisfacción producto (promedio)':<35} {round(suma_prod / cantidad_total, 2)}")
print(f"  {'Satisfacción servicio (promedio)':<35} {round(suma_serv / cantidad_total, 2)}")
print(f"  {'Tiempo de entrega más común':<35} {tiempo_top}")
print(f"  {'Percepción de precio más común':<35} {precio_top}")
print(f"  {'Recomendación promedio':<35} {round(suma_rec2 / cantidad_total, 2)}")
print(f"  {'Calificación general promedio':<35} {round(suma_gen2 / cantidad_total, 2)}")
print(f"  {'% que volvería a comprar':<35} {round((volveria_count / cantidad_total) * 100, 2)}%")
print(f"  {'NPS calculado':<35} {nps}")
print("=" * 55)







    
    








