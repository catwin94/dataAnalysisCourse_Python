import os as os
import pandas as pd
import requests
import numpy as np
import datetime

def wget(url):
  r = requests.get(url, allow_redirects=True)
  with open(url[url.rfind('/') + 1::], 'wb') as f:
      f.write(r.content)

########### Ejercitacion integradora #####################################################################################
########### Copy #########################################################################################################
def copyFile(fileDataFrame, name):
  # 1. Check si existe el archivo
  n=1
  fileName = f"Copy{n}_{name}.xlsx"
  while (os.path.exists(fileName)): #El archivo existe -> Change name
    n=n+1
    fileName = f"Copy{n}_{name}.xlsx"

  fileDataFrame.to_excel(fileName)  

  # for i in range(4):
  #   fileName = f"Copy{n}_{name}.xlsx"
  #   print(fileName)
  #   # print(f"Copy{n}_{name}.xlsx")
  #   n=n+1
  # fileDataFrame.to_excel()

# data = pd.read_excel("Datos.xlsx")   
# copyFile(data, "archivo")  

########### California Housing ###########################################################################################
# wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/california_housing_train.xlsx")
# archivo = pd.read_excel("california_housing_train.xlsx") 
# pd.set_option("display.max_columns", 9)
# # print(archivo)

# # ¿Cuantas casas hay con valor 'median_house_value' mayor a 80000 tomando de la longitud -120 a -118? Rta: 5466
# rta1 = archivo[( archivo['longitude'] >= -120.0) & ( archivo['longitude'] <= -118.0) & (archivo['median_house_value'] > 80000)].shape[0]
# print(rta1)

# # ¿Cual es el promedio de habitaciones por manzana ('total_rooms') de estas casas(las del filtro)? Rta: 2466.31
# casasFiltradas = archivo[( archivo['longitude'] >= -120.0) & ( archivo['longitude'] <= -118.0) & (archivo['median_house_value'] > 80000)]
# print((casasFiltradas['total_rooms'].sum())/len(casasFiltradas['total_rooms']))
# # print(np.mean(casasFiltradas["total_rooms"]))

# # ¿Cual es la casa más cara? ¿Cuántas hay con este valor? Rta: 500001.0 - 814 
# print(archivo["median_house_value"].max())
# print(archivo[ archivo["median_house_value"] == archivo["median_house_value"].max() ].shape[0])

# # Obtener la media y la varianza de la propiedad 'median_house_value'. Rta: 207300.91 - 13451442293.57
# print(np.mean(archivo["median_house_value"]))
# print(np.var(archivo["median_house_value"]))

########### Llévame en tu bicicleta ######################################################################################
# wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/recorridos-realizados-2021-sample.csv")
# archivo = pd.read_csv("recorridos-realizados-2021-sample.csv", index_col="Fecha de inicio") 
# pd.set_option("display.max_columns", 13)
# # print(archivo)
# # print(archivo.keys())

# # ¿Qué porcentaje de los viajes se completaron en estado NORMAL?
# normal = archivo[archivo["Estado cerrado"] == "NORMAL"].shape[0]
# print(f"Porcentaje de viajes completado en estado NORMAL: {round((normal/archivo.shape[0])*100, 2)} % ")

# # ¿Cuál es la duración promedio de cada viaje? (Los datos están en segundos)
# duracionPromedio = np.mean(archivo["Duración"]) #Usando numpy
# duracionPromedio = archivo["Duración"].mean() #Usando Pandas
# print(f"Duracion promedio: {round(duracionPromedio/60 , 2)} minutos")

# # ¿A qué hora del día se realizaron más viajes? (por ejemplo: de 16hs a 17hs)
# # Note: transformar index en un DatetimeIndex
# archivo.index = pd.to_datetime(archivo.index)
# maximo = 0
# date = ""
# for i in range(24):
#   start = datetime.time(i%24)
#   end = datetime.time((i+1)%24)
#   value = len(archivo.between_time(start_time=str(start), end_time=str(end)))
#   # print(f" {start}-{end}: {value}")
#   if value > maximo:
#     maximo = value
#     date = str(start) + " - " + str(end) 
# print(f"Entre: {date} || maximo numero de viajes: {maximo}")

# # ¿Cuántas estaciones diferentes fueron utilizadas?
# estacionesPartida = set(archivo["Id de estación de inicio"].unique())
# estacionesLlegada = set(archivo["Id de estación de fin de viaje"].unique())
# estacionesUsadas = estacionesPartida | estacionesLlegada
# print(f"Estaciones utilizadas: {len(estacionesUsadas)}")

# # Para cada estación utilizada como inicio de un viaje, imprimirlas ordenadas por cantidad de viajes que iniciaron de la misma.
# frecuencia = archivo["Nombre de estación de inicio"].value_counts(ascending=False)
# print(frecuencia)

########### El tiempo es dinero ##########################################################################################
# wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Finanzas.xlsx")

# #Note: Tenemos un excel con dos hojas, la primera corresponde a "Usuarios" la segunda a "Transferencias"
# usuarios_archivo = pd.read_excel("Finanzas.xlsx", "Usuarios",index_col="Usuario") #leemos los usuarios "indexados" por su nombre
# transferencias_archivo = pd.read_excel("Finanzas.xlsx", "Transferencias")
# # print(usuarios_archivo)
# # print(transferencias_archivo)

# def trasferenceUpdate(emisor, receptor, monto):
#   usuarios_archivo.loc[emisor]["Presupuesto"]= usuarios_archivo.loc[emisor]["Presupuesto"] - monto
#   usuarios_archivo.loc[receptor]["Presupuesto"]= usuarios_archivo.loc[receptor]["Presupuesto"] + monto

# lista = transferencias_archivo.to_dict("index")
# for operationNb, data in lista.items():
#   trasferenceUpdate(data["Emisor"], data["Receptor"], data["Monto"])
#   transferencias_archivo.at[operationNb,'Efectuada'] = "Yes" # update transference state

# # Save data in a new excel file (two differents sheets)
# with pd.ExcelWriter("usuarios_actualizados.xlsx") as writer:
#   usuarios_archivo.to_excel(writer, sheet_name='Usuarios')
#   transferencias_archivo.to_excel(writer, sheet_name='Transferencias')

# print(usuarios_archivo)
# print(transferencias_archivo)

########### Buscando la $ ################################################################################################
# archivo = pd.read_excel("california_housing_train.xlsx") 
# pd.set_option("display.max_columns", 9)
# paso = .5

# lats = np.arange(32.5,42.5,paso)
# lons = np.arange(-124.3,113.3,paso) 
# maximoValor = 0
# maximaLat = 0
# maximaLon = 0

# archivo = archivo[ archivo["households"] > 100 ]
# for latitud in lats:
#   for longitud in lons:
#     cuadrado = archivo[ (archivo["latitude"] >= latitud) & (archivo["latitude"] < (latitud + paso)) & (archivo["longitude"] >= longitud) & (archivo["longitude"] < (longitud + paso))]

#     media = np.mean(cuadrado["median_house_value"])
#     if media > maximoValor:
#       maximoValor = media
#       maximaLat = latitud
#       maximaLon = longitud

# print(f"El valor maximo es: {maximoValor} y se ubica en: lat: {maximaLat} y long: {maximaLon}")  

########### Unificación de bases de datos ################################################################################

# wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/lista1.csv" ) # primera lista de clientes
# wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/lista2.csv")
# # segunda lista de clientes
# wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/lista_final.csv")
# # ejemplo de como tiene que quedar (las columnas pueden quedar en otro orden! salvo la primera)

# archivo1 = pd.read_csv("lista1.csv", index_col="Mail")
# archivo2 = pd.read_csv("lista2.csv", index_col="Mail")
archivo1 = pd.read_csv("lista1.csv")
archivo2 = pd.read_csv("lista2.csv")
archivo3 = pd.read_csv("lista_final.csv")
merged = pd.merge(left=archivo1.astype(object), right=archivo2.astype(object), how="outer").fillna("-")

listafinal = pd.DataFrame(merged)
listafinal.to_csv("listaFinal.csv", index = False)

# frames = [archivo1, archivo2]
# # resultado = pd.concat(frames, ignore_index=True)
# resultado = archivo1.append(archivo2, sort=False, ignore_index=True)
# print(resultado,"\n")