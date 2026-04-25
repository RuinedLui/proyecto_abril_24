import csv 
#creamos listas donde almacenaremos la encuests ya estructurada
encuestados_cliente = []

#asigmamos el archivo csv a una variable para su manipulación
archivo = 'encuesta_restaurantes_10000.csv'
#abrir el archivo csv en modo lectura con encoding utf-8 para evitar problemas con caracteres especiales
with open(archivo, 'r', encoding='utf-8') as archivo_csv:
    #utilizar DictReader para leer el archivo csv y convertir cada fila en un diccionario
    lector_csv = csv.DictReader(archivo_csv)
    #convertir el lector_csv en una lista de diccionarios para facilitar su manipulación
    c = list(lector_csv)
    #recorrer cada diccionario en la lista c
    for fila in c:
        #empezar a identificar los datos de cada cliente parae estructurar la información
        datos = {
            'iden': fila['id'],
            'comida': fila['comida_preferida'],
            'frecuencia': fila['frecuencia_consumo'],
            'gasto': fila['gasto_promedio'],
            'satisfaccion_p': fila['satisfaccion_producto'],
            'satisfaccion_s': fila['satisfaccion_servicio'],
            't_entrega': fila['tiempo_entrega'],
            'p_precio': fila['precio_percepcion'],
            #declaramos la respuesta de recomendaría como un entero para facilitar su manipulación en los reportes
            'recomendaria': int(fila['recomendaria']),
            #transformaremos a un boleean la respuesta de volveria_comprar para facilitar su manipulación en los reportes
            'volveria': fila['volveria_comprar'].strip().lower() == 'true',
            'calificacion': fila['calificacion_general']
        }
        #cada encuestado se presentara como un diccionario con sus datos correspondientes
        encuestados={
            "id": datos['iden'],
            "preferencias": { "comida": datos['comida'], "frecuencia": datos['frecuencia'] },
            "consumo": { "gasto": datos['gasto'] },
            "experiencia": { "producto": datos['satisfaccion_p'], "servicio": datos['satisfaccion_s'], "tiempo": datos['t_entrega'], "precio": datos['p_precio'] },
            "nps": { "recomendacion": datos['recomendaria'], "volveria": datos['volveria'], "general": datos['calificacion'] }
        }
       #se almacena todo en una lista 
        encuestados_cliente.append(encuestados)

        #Ya teniendo la informacion estructura y almacenada en una lista procedemos a hacer los
        #reportes 
         #--------------------------------------------------------------------------------
         #-------------------------------------------------------------------------------
         #--------------------------------------REPORTES--------------------------------------
         #Reporte 1: Cantidad de personas por comida favorita
         #se crea un diccionario para almacenar la cantidad de personas por cada comida favorita
reporte_comida = {}
#se recorre la lista de encuestados para contar la cantidad de personas por cada comida favorita
for encuestado in encuestados_cliente:
             #se obtiene la comida favorita del encuestado en una varible temporal
             comida = encuestado['preferencias']['comida']
             #se valida si la comida ya esta en el diccioario reporte_comida, 
             # si es asi se incrementa el contador
             if comida in reporte_comida:
                 reporte_comida[comida] += 1
                 #si no esta en el diccionario se agrega con un contador inicial de 1
             else:
                 reporte_comida[comida] = 1
#se imprime el reporte de cantidad de personas por comida favorita
print("-----------------------------------REPORTE 1-----------------------------")
print("Reporte 1: Cantidad de personas por comida favorita:")
print("-----------------------------------------------------------------------")
#se recorre el diccionario reporte_comida para imprimir la cantidad de personas por cada comida favorita
#con .items() se obtiene la clave (comida) y el valor (cantidad) 
for comida, cantidad in reporte_comida.items():
    print(f"|{comida}|: {cantidad} personas")
    print("-----------------------------------------------------------------------")
 #------------------------------------------------------------------------------------------------------
 #-------------------------------------REPORTE 2------------------------------------------------ ---  -------------
#REPORTE 2: FRECUENCIA DE CONSUMO
#se crea un diccionario para almacenar la cantidad de personas por cada frecuencia de consumo
reporte_frecuencia = {}
#se recorre la lista de encuestados para contar la cantidad de personas por cada frecuencia de consumo
for encuestado in encuestados_cliente:
    frecuencia = encuestado['preferencias']['frecuencia']
    #se valida si la frecuencia ya esta en el diccioario reporte_frecuencia,
    if frecuencia in reporte_frecuencia:
        reporte_frecuencia[frecuencia] += 1
        #Si no se inicializa 
    else:
        reporte_frecuencia[frecuencia] = 1

#se imprime el reporte de cantidad de personas por frecuencia de consumo
print("-----------------------------------REPORTE 2-----------------------------")
print("Reporte 2: Cantidad de personas por frecuencia de consumo:")
print("-----------------------------------------------------------------------")
#se recorre el diccionario reporte_frecuencia para imprimir el resultado
for frecuencia, cantidad in reporte_frecuencia.items():
    print(f"|{frecuencia}|: {cantidad} personas")
    print("-----------------------------------------------------------------------")
    #------------------------------------------------------------------------------------------------------
    #-------------------------------------REPORTE 3------------------------------------------------
    #REPORTE 3: Promedio de gasto
    #Diccionario para almcacenar el promedio de gasto 
reporte_gasto = {}
#se recorre la lista de encuestados para calcular el promedio de gasto
for encuestado in encuestados_cliente:
    gasto = float(encuestado['consumo']['gasto'])
    #se valida si el gasto ya esta en el diccioario reporte_gasto, 
    if 'total_gasto' in reporte_gasto:
        reporte_gasto['total_gasto'] += gasto
        reporte_gasto['contador'] += 1
        #Si no se inicializa 
    else:
        reporte_gasto['total_gasto'] = gasto
        reporte_gasto['contador'] = 1
#se calcula el promedio de gasto dividiendo el total de gasto entre el contador
promedio_gasto = reporte_gasto['total_gasto'] / reporte_gasto['contador']
#se imprime el reporte de promedio de gasto
print("-----------------------------------REPORTE 3-----------------------------")
print("Reporte 3: Promedio de gasto:")
#se imprime el promedio de gasto formateado a 2 decimales con .2f
print(f"El promedio de gasto de los clientes: ${promedio_gasto:.2f}")
#------------------------------------------------------------------------------------------------------
#REPORTE 4: Promedio de satisfacción del producto
reporte_satisfaccion_producto = {}
#se recorre la lista de encuestados para calcular el promedio de satisfacción del producto
for encuestado in encuestados_cliente:
    satisfaccion_p = float(encuestado['experiencia']['producto'])
    # creo la llave total_satisfaccion_p para acumular la suma de las satisfacciones del producto
    # y contador para contar la cantidad de encuestados que respondieron esta pregunta
    if 'total_satisfaccion_p' in reporte_satisfaccion_producto:
        reporte_satisfaccion_producto['total_satisfaccion_p'] += satisfaccion_p
        reporte_satisfaccion_producto['contador'] += 1
        #Si no se inicializa 
    else:
        reporte_satisfaccion_producto['total_satisfaccion_p'] = satisfaccion_p
        reporte_satisfaccion_producto['contador'] = 1
#se calcula el promedio de satisfacción del producto dividiendo el total de satisfacción entre el contador
promedio_satisfaccion_producto = reporte_satisfaccion_producto['total_satisfaccion_p'] / reporte_satisfaccion_producto['contador']
#se imprime el reporte de promedio de satisfacción del producto
print("-----------------------------------REPORTE 4-----------------------------")
print("Reporte 4: Promedio de satisfacción del producto:")
print(f"El promedio de satisfacción del producto: {promedio_satisfaccion_producto:.2f} Sobre 10")
print("-----------------------------------------------------------------------")
#------------------------------REPORTE 5: Promedio de satisfacción del servicio--------------------------------------
reporte_satisfaccion_servicio = {}
#Se repite el mismo proceso que el reporte anterior pero para la satisfacción del servicio
for encuestado in encuestados_cliente:
    satisfaccion_s = float(encuestado['experiencia']['servicio'])
    # creo la llave total_satisfaccion_s para acumular la suma de las satisfacciones del servicio
    if 'total_satisfaccion_s' in reporte_satisfaccion_servicio:
        reporte_satisfaccion_servicio['total_satisfaccion_s'] += satisfaccion_s
        reporte_satisfaccion_servicio['contador'] += 1
        #Si no se inicializa
    else:
        reporte_satisfaccion_servicio['total_satisfaccion_s'] = satisfaccion_s
        reporte_satisfaccion_servicio['contador'] = 1
        #se calcula el promedio de satisfacción del servicio dividiendo el total de satisfacción entre el contador
promedio_satisfaccion_servicio = reporte_satisfaccion_servicio['total_satisfaccion_s'] / reporte_satisfaccion_servicio['contador']
#se imprime el reporte de promedio de satisfacción del servicio
print("-----------------------------------REPORTE 5-----------------------------")
print("Reporte 5: Promedio de satisfacción del servicio:")
print(f"El promedio de satisfacción del servicio: {promedio_satisfaccion_servicio:.2f} Sobre 10")
#------------------------------------------------------------------------------------------------------
#--------------------------------REPORTE 6: DISTRIBUCION DEL TIEMPO DE ENTREGA--------------------------------------
reporte_tiempo_entrega = {}
#CON CICLO FOR RECORREMOS LA LISTA PARA OBTENER LOS DATOS
for encuestado in encuestados_cliente:
    tiempo_entrega = encuestado['experiencia']['tiempo']
    #se valida si el tiempo de entrega ya esta en el diccioario reporte_tiempo_entrega, 
    if tiempo_entrega in reporte_tiempo_entrega:
        reporte_tiempo_entrega[tiempo_entrega] += 1
        #Si no se inicializa 
    else:
        reporte_tiempo_entrega[tiempo_entrega] = 1
        #ORGANIZAMOS Y IMPRIMIMOS EL REPORTE DE DISTRIBUCION DEL TIEMPO DE ENTREGA
print("-----------------------------------REPORTE 6-----------------------------")
print("Reporte 6: Distribución del tiempo de entrega:")
print("-----------------------------------------------------------------------")
#se recorre el diccionario reporte_tiempo_entrega para imprimir los resultados
for tiempo_entrega, cantidad in reporte_tiempo_entrega.items():
    print(f"|{tiempo_entrega}|: {cantidad} personas")
    print("-----------------------------------------------------------------------")
    #------------------------------------------------------------------------------------------------------
    #--------------------------------REPORTE 7: DISTRIBUCION DE LA PERCEPCION DEL PRECIO------------------
    #DECLARAMOS DICCIONARIO  PARA ALMACENAR LOS DATOS
reporte_percepcion_precio = {}
#CON CICLO FOR RECORREMOS LA LISTA PARA OBTENER LOS DATOS
for encuestado in encuestados_cliente:
    #obtenemos la percepcion del precio del encuestado en una variable temporal
    percepcion_precio = encuestado['experiencia']['precio']
    #se repite el proceso anterior 
    if percepcion_precio in reporte_percepcion_precio:
        reporte_percepcion_precio[percepcion_precio] += 1
        #Si no se inicializa 
    else:
        reporte_percepcion_precio[percepcion_precio] = 1
        #ORGANIZAMOS Y IMPRIMIMOS EL REPORTE DE DISTRIBUCION DE LA PERCEPCION DEL PRECIO
print("-----------------------------------REPORTE 7-----------------------------")
print("Reporte 7: Distribución de la percepción del precio:")
#se recorre el diccionario reporte_percepcion_precio para imprimir los resultados   
for percepcion_precio, cantidad in reporte_percepcion_precio.items():
    print(f"|{percepcion_precio}|: {cantidad} personas")
    print("-----------------------------------------------------------------------")
    #------------------------------------------------------------------------------------------------------
    #---------------------------------REPORTE 8:PROMEDIO GENERAL DE SATISFACCION-------------------------------------
reporte_s_general = {}
#CON CICLO FOR RECORREMOS LA LISTA PARA OBTENER LOS DATOS
for encuestado in encuestados_cliente:
    calificacion_general = float(encuestado['nps']['general'])
    #se valida si la calificacion general ya esta en el diccioario reporte_s_general, 
    if 'total_calificacion_general' in reporte_s_general:
        reporte_s_general['total_calificacion_general'] += calificacion_general
        reporte_s_general['contador'] += 1
        #Si no se inicializa 
    else:
        reporte_s_general['total_calificacion_general'] = calificacion_general
        reporte_s_general['contador'] = 1
        #se calcula el promedio general de satisfacción dividiendo el total de calificación general entre el contador
promedio_calificacion_general = reporte_s_general['total_calificacion_general'] / reporte_s_general['contador']
#se imprime el reporte de promedio general de satisfacción
print("-----------------------------------REPORTE 8-----------------------------")
print("Reporte 8: Promedio general de satisfacción:")       
print(f"El promedio general de satisfacción: {promedio_calificacion_general:.2f} Sobre 10")
#------------------------------------------------------------------------------------------------------
#---------------------------------REPORTE 9: PORCENTAJE DE CLIENTES QUE VOLVERIAN------------------------------------------------------
#DECLARAMOS DICCIONARIO PARA ALMACENAR LOS DATOS
reporte_volveria = {}
#CON CICLO FOR RECORREMOS LA LISTA PARA OBTENER LOS DATOS
for encuestado in encuestados_cliente:
    volveria = encuestado['nps']['volveria']
    #se valida si la respuesta de volveria es True o False para contar la cantidad de clientes que volverian o no
    if volveria:
        if 'volveria' in reporte_volveria:
            reporte_volveria['volveria'] += 1
        else:
            reporte_volveria['volveria'] = 1
    else:
        if 'no_volveria' in reporte_volveria:
            reporte_volveria['no_volveria'] += 1
        else:
            reporte_volveria['no_volveria'] = 1
#se calcula el porcentaje de clientes que volverian con .len() para obtener el total de encuestados y el contador de los que volverian
total_encuestados = len(encuestados_cliente)
#se obtiene la cantidad de clientes que volverian del diccionario reporte_volveria, si no existe se asigna 0 para evitar errores
clientes_volverian = reporte_volveria.get('volveria', 0)
porcentaje_volverian = (clientes_volverian / total_encuestados) * 100
#se imprime el reporte de porcentaje de clientes que volverian
print("-----------------------------------REPORTE 9-----------------------------")
print("Reporte 9: Porcentaje de clientes que volverían:")
print(f"El porcentaje de clientes que volverían: {porcentaje_volverian:.2f}%")
#------------------------------------------------------------------------------------------------------
#---------------------------------REPORTE 10: CALCULO DE NPS------------------------------------------------------    
calculo_nps = {}
# Inicializamos contadores
promotores = 0
pasivos = 0
detractores = 0
total_encuestados = len(encuestados_cliente)
#CON CICLO FOR RECORREMOS LA LISTA PARA OBTENER LOS DATOS DE RECOMENDARIA
for encuestado in encuestados_cliente:
    recomendaria = encuestado['nps']['recomendacion']
    #se valida a que rango de calificación pertenece la respuesta de recomendaría para clasificar al cliente como promotor, pasivo o detractor
    if recomendaria >= 9:
        promotores += 1
    elif recomendaria >= 7:
        pasivos += 1
    else:
        detractores += 1
#se calcula el NPS con la formula: NPS = (%Promotores - %Detractores) / Total de encuestados * 100
porcentaje_promotores = (promotores / total_encuestados) * 100
porcentaje_detractores = (detractores / total_encuestados) * 100
#MOSTRAMOS EL TOTAL DE PROMOTORES, PASIVOS Y DETRACTORESy sus porcentajes
#NOTA: ACA MISMO INCLUI EL REPORTE 11- SEGMENTACION DE PROMOTORES
print("-----------------------------------REPORTE 10 y 11-----------------------------")
print("Reporte 10: Cálculo de NPS:")
print(f"Total de Clientes promotores: {promotores} ({porcentaje_promotores:.2f}%)")
print(f"Total de Clientes pasivos: {pasivos} ({(pasivos / total_encuestados) * 100:.2f}%)")
print(f"Total de Clientes detractores: {detractores} ({porcentaje_detractores:.2f}%)")
#se calcula el NPS restando el porcentaje de detractores al porcentaje de promotores
nps = porcentaje_promotores - porcentaje_detractores
#se imprime el resultado del NPS
print("---------------------------------------------------------------------------")
print(f"El NPS calculado es: {nps:.2f}%")
#imprimimos la conclusion del reporte con respecto al nps negativo
print("-----------------------------------CONCLUSIÓN-----------------------------")
print("El NPS es negativo, lo que indica que hay más detractores que promotores. " )
print("Esto sugiere que la mayoría de los clientes no están satisfechos con el servicio")
#_-----------------------------------------------------------------------------------------------------
#---------------------------------REPORTE 12 COMIDA CON MAYOR SATISFACCION------------------------------------------------------
comida_mayor_Satisfaccion = {}
#CON CICLO FOR RECORREMOS LA LISTA PARA OBTENER LOS DATOS DE COMIDA Y SU SATISFACCION
for encuestado in encuestados_cliente:
    comida = encuestado['preferencias']['comida']
    satisfaccion_producto = float(encuestado['experiencia']['producto'])
    #se valida si la comida ya esta en el diccioario comida_mayor_Satisfaccion, 
    if comida in comida_mayor_Satisfaccion:
        comida_mayor_Satisfaccion[comida]['total_satisfaccion'] += satisfaccion_producto
        comida_mayor_Satisfaccion[comida]['contador'] += 1
        #Si no se inicializa 
    else:
        comida_mayor_Satisfaccion[comida] = {
            'total_satisfaccion': satisfaccion_producto,
            'contador': 1
        }
#se calcula el promedio de satisfacción para cada comida dividiendo el total de satisfacción entre el contador
promedio_satisfaccion_comida = {}
for comida, datoss in comida_mayor_Satisfaccion.items():
    promedio_satisfaccion_comida[comida] = datoss['total_satisfaccion'] / datoss['contador']
#calculamos la comida con mayor satisfacción comparando los promedios de satisfacción de cada comida y almacenando la comida con el mayor promedio
comida_mayor_satisfaccion = None
mayor_satisfaccion = 0
for comida, promedio in promedio_satisfaccion_comida.items():
    if promedio > mayor_satisfaccion:
        mayor_satisfaccion = promedio
        comida_mayor_satisfaccion = comida
#se imprime el reporte de comida con mayor satisfacción
print("-----------------------------------REPORTE 12-----------------------------")
print("Reporte 12: Comida con mayor satisfacción del producto")
print(f"La comida con mayor satisfacción del producto es: {comida_mayor_satisfaccion} con un promedio de satisfacción de {mayor_satisfaccion:.2f} Sobre 10")
#------------------------------------------------------------------------------------------------------
#------------------------REPORTE 13 COMIDA CON MENOR SATISFACCION------------------------------------------------------
#DICCIONARIO PARA ALMCACENEAR NDATOS
comida_menor_Satisfaccion = {}
#REUTILIZAMOS LA LOGICA ANTERIOR UBICAMENTE CAMBIANDO EL OBJETIVO 
#DE CALCULAR LA COMIDA CON MENOR SATISFACCION EN LUGAR DE LA MAYOR
for encuestado in encuestados_cliente:
    comida = encuestado['preferencias']['comida']
    satisfaccion_producto = float(encuestado['experiencia']['producto'])
    if comida in comida_menor_Satisfaccion:
        comida_menor_Satisfaccion[comida]['total_satisfaccion'] += satisfaccion_producto
        comida_menor_Satisfaccion[comida]['contador'] += 1
    else:
        comida_menor_Satisfaccion[comida] = {
            'total_satisfaccion': satisfaccion_producto,
            'contador': 1
        }
promedio_satisfaccion_comida_menor = {}
for comida, datoss in comida_menor_Satisfaccion.items():
    promedio_satisfaccion_comida_menor[comida] = datoss['total_satisfaccion'] / datoss['contador']
comida_menor_satisfaccion = None
# Inicializamos con un valor alto para asegurarnos de que cualquier promedio de satisfacción será menor que este valor inicial
menor_satisfaccion = 11

for comida, promedio in promedio_satisfaccion_comida_menor.items():
  #si el promedio de satisfacción de la comida actual es menor que el valor almacenado en menor_satisfacción,
  #  se actualiza el valor de menor_satisfacción y se almacena el nombre de la comida con menor satisfacción

    
    if promedio < menor_satisfaccion:
        menor_satisfaccion = promedio
        comida_menor_satisfaccion = comida

print("-----------------------------------REPORTE 13-----------------------------")
print("Reporte 13: Comida con menor satisfacción del producto")
print(f"La comida con menor satisfacción es: {comida_menor_satisfaccion} con un promedio de {menor_satisfaccion:.2f} sobre 10")
print("-------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------
#-REPORTR 14 REALACION EMNTRE GASTO Y SATISFACCION DEL PRODUCTO------------------------------------------------------
relacion_gasto_satisfaccion = {}
#UTILIZAMOS CICLO FOR NUEVAMENTE
#utilizaremos un rango de gasto para agrupar los datos y
# facilitar la interpretación de la relación entre gasto y satisfacción del producto
#gasto bajo sera entre 1 y 49, gasto medio entre 49 y 99, y gasto alto mayor a 100
for encuestado in encuestados_cliente:
    gasto = float(encuestado['consumo']['gasto'])
    satisfaccion_producto = float(encuestado['experiencia']['producto'])
    #se clasifica el gasto en bajo, medio o alto y se almacena la satisfacción del producto correspondiente a cada rango de gasto
    if gasto < 50:
        categoria_gasto = 'Bajo 0-49'
    elif gasto < 100:
        categoria_gasto = 'Medio 50-99'
    else:
        categoria_gasto = 'Alto 100+'
    #se valida si la categoría de gasto ya esta en el diccioario relacion_gasto_satisfaccion,
    if categoria_gasto in relacion_gasto_satisfaccion:
        relacion_gasto_satisfaccion[categoria_gasto]['total_satisfaccion'] += satisfaccion_producto
        relacion_gasto_satisfaccion[categoria_gasto]['contador'] += 1
    else:
        relacion_gasto_satisfaccion[categoria_gasto] = {
            'total_satisfaccion': satisfaccion_producto,
            'contador': 1
        }
#se calcula el promedio de satisfacción del producto para cada categoría de gasto dividiendo el total de satisfacción entre el contador
promedio_satisfaccion_gasto = {}
#se recorre el diccionario relacion_gasto_satisfaccion para calcular el promedio de satisfacción del producto
#  para cada categoría de gasto
for categoria_gasto, datoss in relacion_gasto_satisfaccion.items():
    promedio_satisfaccion_gasto[categoria_gasto] = datoss['total_satisfaccion'] / datoss['contador']
#se imprime el reporte de relación entre gasto y satisfacción del producto
print("-----------------------------------REPORTE 14-----------------------------")
print("Reporte 14: Relación entre gasto y satisfacción del producto")
for categoria_gasto, promedio in promedio_satisfaccion_gasto.items():
    print(f"Categoría de gasto: {categoria_gasto} - Promedio de satisfacción del producto: {promedio:.2f} sobre 10")
    #------------------------------------------------------------------------------------------------------
# REPORTE 15: FRECUENCIA VS SATISFACCIÓN
# =====================================================================
frecuencia_satisfaccion = {}

# Recorremos la lista para obtener los datos
for encuestado in encuestados_cliente:
    frecuencia = encuestado['preferencias']['frecuencia']
    satisfaccion_general = float(encuestado['nps']['general'])
    
    # Agrupamos por frecuencia
    if frecuencia in frecuencia_satisfaccion:
        frecuencia_satisfaccion[frecuencia]['total_satisfaccion'] += satisfaccion_general
        frecuencia_satisfaccion[frecuencia]['contador'] += 1
    else:
        frecuencia_satisfaccion[frecuencia] = {
            'total_satisfaccion': satisfaccion_general,
            'contador': 1
        }

# Calculamos 
promedio_satisfaccion_frecuencia = {} 
for frecuencia, datoss in frecuencia_satisfaccion.items():
    promedio_satisfaccion_frecuencia[frecuencia] = datoss['total_satisfaccion'] / datoss['contador']

# Imprimimos 
print("-----------------------------------REPORTE 15-----------------------------")
print("Reporte 15: Relación entre Frecuencia de Consumo y SatisfaccióN")
print("-------------------------------------------------------------------------")
for frecuencia, promedio in promedio_satisfaccion_frecuencia.items():
    print(f"| Frecuencia: {frecuencia} | Promedio General: {promedio:.2f} sobre 10")
print("-------------------------------------------------------------------------")
#=================================================================================================
#REPORTE 16:PRECIO VS RECOMENDACION
precio_recomendacion = {}
# Recorremos la lista para obtener los datos
for encuestado in encuestados_cliente:
    precio_percepcion = encuestado['experiencia']['precio']
    recomendacion = encuestado['nps']['recomendacion']
    
    # Agrupamos por percepción de precio
    if precio_percepcion in precio_recomendacion:
        precio_recomendacion[precio_percepcion]['total_recomendacion'] += recomendacion
        precio_recomendacion[precio_percepcion]['contador'] += 1
    else:
        precio_recomendacion[precio_percepcion] = {
            'total_recomendacion': recomendacion,
            'contador': 1
        }
# Calculamos el promedio de recomendación para cada percepción de precio
promedio_recomendacion_precio = {}
for precio_percepcion, datoss in precio_recomendacion.items():
    promedio_recomendacion_precio[precio_percepcion] = datoss['total_recomendacion'] / datoss['contador']
# Imprimimos el reporte de relación entre percepción de precio y recomendación
print("-----------------------------------REPORTE 16-----------------------------")
print("Reporte 16: Relación entre Percepción de Precio y Recomendación")
print("-------------------------------------------------------------------------")
for precio_percepcion, promedio in promedio_recomendacion_precio.items():
    print(f"| Percepción de Precio: {precio_percepcion} | Promedio de Recomendación: {promedio:.2f} sobre 10")
print("-------------------------------------------------------------------------")
#=================================================================================================
#REPORTE 17: TIEMPO DE ENTREGA VS SATISFACCIÓN DEL SERVICIO
tiempo_satisfaccion_servicio = {}
# Recorremos la lista para obtener los datos
for encuestado in encuestados_cliente:
    tiempo_entrega = encuestado['experiencia']['tiempo']
    satisfaccion_servicio = float(encuestado['experiencia']['servicio'])
    
    # Agrupamos por tiempo de entrega
    if tiempo_entrega in tiempo_satisfaccion_servicio:
        tiempo_satisfaccion_servicio[tiempo_entrega]['total_satisfaccion'] += satisfaccion_servicio
        tiempo_satisfaccion_servicio[tiempo_entrega]['contador'] += 1
        #
    else:
        tiempo_satisfaccion_servicio[tiempo_entrega] = {
            'total_satisfaccion': satisfaccion_servicio,
            'contador': 1
        }
# Calculamos el promedio de satisfacción del servicio para cada tiempo de entrega
promedio_satisfaccion_tiempo = {}
for tiempo_entrega, datoss in tiempo_satisfaccion_servicio.items():
    promedio_satisfaccion_tiempo[tiempo_entrega] = datoss['total_satisfaccion'] / datoss['contador']
# Imprimimos el reporte de relación entre tiempo de entrega y satisfacción del servicio
print("-----------------------------------REPORTE 17-----------------------------")
print("Reporte 17: Relación entre Tiempo de Entrega y Satisfacción del Servicio")
print("-------------------------------------------------------------------------")
for tiempo_entrega, promedio in promedio_satisfaccion_tiempo.items():
    print(f"| Tiempo de Entrega: {tiempo_entrega} | Promedio de Satisfacción del Servicio: {promedio:.2f} sobre 10")
#REPORTE 18 RANKING DE COMIDA MAS CONSUMIDAS
# REPORTE 18 RANKING DE COMIDA MAS CONSUMIDAS
ranking_comida_consumida = {}

# Recorremos la lista para obtener los datos
for encuestado in encuestados_cliente:
    comida = encuestado['preferencias']['comida']
    
    # Contamos la cantidad de veces que se consume cada comida
    if comida in ranking_comida_consumida:
        ranking_comida_consumida[comida] += 1
    else:
        ranking_comida_consumida[comida] = 1

# ==============================================================
# NUEVA FORMA DE ORDENAR (Sin lambda)
# ==============================================================
# 1. Creamos una lista temporal donde ponemos (cantidad, comida)
c_ranking= []
for comida, cantidad in ranking_comida_consumida.items():
    c_ranking.append((cantidad, comida))

# 2. Ordenamos la lista temporal por cantidad de forma descendente
c_ranking.sort(reverse=True)
# 3. Creamos el ranking final con la comida y su cantidad ordenada
ranking_final = []
for cantidad, comida in c_ranking:
    ranking_final.append((comida, cantidad))
# Imprimimos el ranking de comida más consumida
print("-----------------------------------REPORTE 18-----------------------------")
print("Reporte 18: Ranking de Comida Más Consumida")
print("-------------------------------------------------------------------------")

# 1. Creamos nuestra variable para el lugar
posicion = 1 

for comida, cantidad in ranking_final:
    # 2. Agregamos la variable 'posicion' al print
    print(f"| {posicion}º Lugar | Comida: {comida} | Cantidad de Consumo: {cantidad} personas")
    
    # 3. Le sumamos 1 para que en la siguiente vuelta sea el lugar corresdpondiente
    posicion += 1 

print("-------------------------------------------------------------------------")
#=================================================================================================
#REPORTE 19 PROMEDIO GENERAL POR TIPO DE COMIDA
promedio_general_comida = {}
# Recorremos la lista para obtener los datos
for encuestado in encuestados_cliente:
    comida = encuestado['preferencias']['comida']
    calificacion_general = float(encuestado['nps']['general'])
    
    # Agrupamos por tipo de comida
    if comida in promedio_general_comida:
        promedio_general_comida[comida]['total_calificacion'] += calificacion_general
        promedio_general_comida[comida]['contador'] += 1
    else:
        promedio_general_comida[comida] = {
            'total_calificacion': calificacion_general,
            'contador': 1
        }
# Calculamos el promedio general para cada tipo de comida
promedio_general_por_comida = {}
for comida, datoss in promedio_general_comida.items():
    promedio_general_por_comida[comida] = datoss['total_calificacion'] / datoss['contador']
# Imprimimos el reporte de promedio general por tipo de comida
print("-----------------------------------REPORTE 19-----------------------------")
print("Reporte 19: Promedio General por Tipo de Comida")
print("-------------------------------------------------------------------------")
for comida, promedio in promedio_general_por_comida.items():
    print(f"| Comida: {comida} | Promedio General: {promedio:.2f} sobre 10")
print("-------------------------------------------------------------------------")
#=================================================================================================
# REPORTE 20: PERFIL DEL CLIENTE PROMEDIo
perfil_cliente_promedio = {}
total_encuestados = len(encuestados_cliente)

# 1. Variables para sumar promedios numéricos
suma_gasto = 0
suma_satisfaccion_producto = 0
suma_satisfaccion_servicio = 0
suma_recomendaria = 0
suma_volveria = 0
suma_calificacion_general = 0

# 2. Diccionarios para contar los textos y sacar el más repetido
conteo_comida = {}
conteo_frecuencia = {}
conteo_tiempo = {}
conteo_precio = {}

# Recorremos los datos
for encuestado in encuestados_cliente:
    # Sumamos los valores numéricos
    suma_gasto += float(encuestado['consumo']['gasto'])
    suma_satisfaccion_producto += float(encuestado['experiencia']['producto'])
    suma_satisfaccion_servicio += float(encuestado['experiencia']['servicio'])
    suma_recomendaria += float(encuestado['nps']['recomendacion'])
    suma_calificacion_general += float(encuestado['nps']['general'])
    
    if str(encuestado['nps']['volveria']).strip().lower() == 'true':
        suma_volveria += 1

    # Contamos las variables de texto
    comida = encuestado['preferencias']['comida']
    frecuencia = encuestado['preferencias']['frecuencia']
    tiempo = encuestado['experiencia']['tiempo']
    precio = encuestado['experiencia']['precio']

    conteo_comida[comida] = conteo_comida.get(comida, 0) + 1
    conteo_frecuencia[frecuencia] = conteo_frecuencia.get(frecuencia, 0) + 1
    conteo_tiempo[tiempo] = conteo_tiempo.get(tiempo, 0) + 1
    conteo_precio[precio] = conteo_precio.get(precio, 0) + 1

# 3. Calculamos la comida nuevamente con ciclos for simples
max_c = 0
for c, cant in conteo_comida.items():
    if cant > max_c: 
        max_c = cant
        perfil_cliente_promedio['comida_favorita'] = c

max_f = 0
for f, cant in conteo_frecuencia.items():
    if cant > max_f: 
        max_f = cant
        perfil_cliente_promedio['frecuencia_consumo'] = f

max_t = 0
for t, cant in conteo_tiempo.items():
    if cant > max_t: 
        max_t = cant
        perfil_cliente_promedio['tiempo_entrega'] = t

max_p = 0
for p, cant in conteo_precio.items():
    if cant > max_p: 
        max_p = cant
        perfil_cliente_promedio['precio_percepcion'] = p

# 4. Calculamos los promedios numéricos
perfil_cliente_promedio['gasto_promedio'] = suma_gasto / total_encuestados
perfil_cliente_promedio['satisfaccion_producto_promedio'] = suma_satisfaccion_producto / total_encuestados
perfil_cliente_promedio['satisfaccion_servicio_promedio'] = suma_satisfaccion_servicio / total_encuestados
perfil_cliente_promedio['recomendacion_promedio'] = suma_recomendaria / total_encuestados
perfil_cliente_promedio['volveria_promedio'] = (suma_volveria / total_encuestados) * 100
perfil_cliente_promedio['calificacion_general_promedio'] = suma_calificacion_general / total_encuestados

# Imprimimos los resultados
print("-----------------------------------REPORTE 20-----------------------------")
print("Reporte 20: Perfil del Cliente Promedio")
print("-------------------------------------------------------------------------")
print(f"Comida Favorita : {perfil_cliente_promedio['comida_favorita']}")
print(f"Frecuencia de Consumo ): {perfil_cliente_promedio['frecuencia_consumo']}")
print(f"Tiempo de Entrega : {perfil_cliente_promedio['tiempo_entrega']}")
print(f"Percepción del Precio : {perfil_cliente_promedio['precio_percepcion']}")
print(f"Gasto Promedio: ${perfil_cliente_promedio['gasto_promedio']:.2f}")
print(f"Satisfacción del Producto Promedio: {perfil_cliente_promedio['satisfaccion_producto_promedio']:.2f} sobre 10")
print(f"Satisfacción del Servicio Promedio: {perfil_cliente_promedio['satisfaccion_servicio_promedio']:.2f} sobre 10")
print(f"Recomendación Promedio: {perfil_cliente_promedio['recomendacion_promedio']:.2f} sobre 10")
print(f"Volvería a Comprar Promedio: {perfil_cliente_promedio['volveria_promedio']:.2f}%")
print(f"Calificación General Promedio: {perfil_cliente_promedio['calificacion_general_promedio']:.2f} sobre 10")
print("-------------------------------------------------------------------------")
# =================================================================================================
# CONCLUSIONES FINALES AUTOMÁTICAS
# =================================================================================================
print("=========================================================================")
print(" 📊 CONCLUSIONES FINALES DEL ANÁLISIS DE DATOS")
print("=========================================================================")
print("1. ALERTA CRÍTICA DE LEALTAD (NPS):")
print("   El NPS resultó profundamente negativo (-45.8%). Esto indica que")
print("   Urge una revisión en la calidad general del restaurante.")
print("")
print("2. RETENCIÓN EN RIESGO:")
print("   Apenas el 49.99 % de los encuestados afirma que volvería a comprar.")
print("   El negocio está perdiendo a la mitad de los clientes que lo visitan.")
print("   Tambien los niveles de satisfaccion en general son bajos")
print("")
print("")
print("4. OPORTUNIDAD DE MEJORA:")
print("   Los Hot Dogs y Hamburguesas son los productos mejor calificados (arriba")
print("   de 5.0). Deberían promocionarse más para mejorar la satisfacción general.")
print("=========================================================================")