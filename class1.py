#note: instalar la libreria requests como: py -m pip install requests

################ CLASE 1 #################################################################################################
################# THEORY : Part A ########################################################################################
import pandas as pd
import requests
import random as r

# Funcion wget para obtener archivos de una url determinada
# Note: usamos "import wget as w" si estamos en linux
def wget(url):
  r = requests.get(url, allow_redirects=True)
  with open(url[url.rfind('/') + 1::], 'wb') as f:
      f.write(r.content)


# # 0. Obtener los datos de un archivo excel ----------------------------------------------------------------------------
# # ---------------------------------------------------------------------------------------------------------------------
#Descarga del archivo de datos Excel del curso
# wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx")

# data = pd.read_excel("Datos.xlsx") 
# print(data)
# #Note: La variable archivo es de un tipo de dato especial de pandas llamado 'DataFrame'

# # 1. ".loc["index"]" -< Permite obtener la informacion de una fila (indice: n) ----------------------------------------
# # ---------------------------------------------------------------------------------------------------------------------
# alumnoData = data.loc[0] # Accede a la fila 0
# print(alumnoData)
# print(alumnoData["Quimica"]) # Una vez en la fila 0, Accede a la columna "Quimica"

# # 2. Organizar la informacion de "data" usando el metodo to_dict("") -> dict, list, series, split, records, index -----
# # ---------------------------------------------------------------------------------------------------------------------
# # Note: De esta manera convertimos nuestro 'DataFrame' en un diccionario del tipo especificado (list, index, etc)

# # list -> devuelve un diccionario cuyas keys son los nombres de la columnas
# # permite tomar los datos y analizarlos por columna
# lista = data.to_dict("list")
# print(lista)

# # 2.a Promedio de las notas de quimica --------------------------------------------------------------------------------
# # ---------------------------------------------------------------------------------------------------------------------
# promedio = sum(lista["Quimica"]) / len(lista["Quimica"])
# print(promedio)

# # records -> devuelve arrays[] con varios diccionarios{} adentro con varios "key: value" (Nombre: Juan)
# # permite tomar los datos y analizarlos por fila y usando keys por columna
# lista2 = data.to_dict("records")
# print(lista2)

# # 2.b Encontrar un alumno en un array ---------------------------------------------------------------------------------
# # ---------------------------------------------------------------------------------------------------------------------
# for alumno in lista2:
#   if alumno["Nombre"] == "Sol":
#     print("Te encontre!", alumno)

# # 3. Cambiar la indexacion
# data2 = pd.read_excel("Datos.xlsx", index_col="Legajo") 
# print(data2)

# # 3.a Busco alumno por legajo
# alumnoLegajo = data2.loc[34567]
# print(alumnoLegajo)


################ CLASE 1 #################################################################################################
########### Mini Desafio 1 A #############################################################################################

# wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Tabla1.xlsx")

# table1 = pd.read_excel("Tabla1.xlsx") # Read and Get Table
# list1 = table1.to_dict("records") # Create a list (dictionary) per row

# print(table1)

# # Resultado
# print("----- Mini Desafio 1 A -----")
# diffGol = []
# for equip in list1:
#   diffGol.append(equip['Goles a favor'] - equip['Goles en contra'])
#   print(equip['Equipo'],":", equip['Goles a favor'] - equip['Goles en contra'])

# print(diffGol)

################ CLASE 1 #################################################################################################
########### Mini Desafio 1 B #############################################################################################
# list2 = table1.to_dict("list") # Create a list (dictionary) per row
# table2 = pd.read_excel("Tabla1.xlsx", index_col="Puntos") # Read and Get Table
# datoos = table2.to_dict("index")

# #usando list2
# maximo2 = max(list2['Puntos'])
# minimo2 = min(list2['Puntos'])

# #usando list of keys (ambos generan la lista de puntos y luego buscan el max or min en el array)
# datoos.keys()
# maximo = max(datoos.keys())
# minimo = min(datoos.keys())

# # Resultado
# print("\n ----- Mini Desafio 1 B ----- ")
# print("ganador:", datoos[maximo]["Equipo"])
# print("perdedor:", datoos[minimo]["Equipo"])

################ CLASE 1 #################################################################################################
################# THEORY : Part B ########################################################################################

# # 0. Crear DataFrame ---------------------------------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------------------------------------
# # Primero: Creo la estructura de datos
# # Note: La key es el titulo de la columna y el contenido(value) es un array con los items de cada columna


# data3 = {
#   "Personas" : ["Analia Ferreyra" , "Martin Hugo", "Fernando Lorenzo"],
#   "Edad" : [25, 35, 87],
#   "Random" : [],
# }

# for i in range(3):
#   data3["Random"].append( r.randint(1,30) )

# print(data3)

# # Segundo: Creo el DataFram -> pandas.DataFrame(datos)
# dataFrame = pd.DataFrame(data3)
# print(dataFrame)

# # Tercero: Exportamos la información a un archivo llamado "personas.xlsx"
# dataFrame.to_excel("personas.xlsx") 

# # 1. Manipulacion del DataFrame ----------------------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------------------------------------
# datos3 = pd.read_excel("Datos.xlsx") 
# print(datos3)

# # 1.a Acceder a una columna especifica -> [columna o key columna] ------------------------------------------------------
# # ----------------------------------------------------------------------------------------------------------------------
# # Note: Imprime la columna con sus indices y al final el nombre de la columna seleccionada con su tipo de dato
# columnaName = 'Quimica'
# print(datos3[columnaName], "\n")

# # 1.b Acceder a una fila especifica -> .loc[indice o fila key] ---------------------------------------------------------
# # ----------------------------------------------------------------------------------------------------------------------
# # Note: Imprime la fila de la forma key:value (ej: Nombre: Juan, Legajo: 87957)
# indice = 0
# alumno3 = datos3.loc[indice] 
# print(alumno3)

# # 1.c Acceder a una fila,columna o columna,fila ------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------------------------------------
# # Podemos ingresar primero a la fila y luego a la columna:
# indice = 0
# alumno3 = datos3.loc[indice] 
# print(alumno3['Matematica'])

# # Podemos ingresar primero a la columna y luego a la fila:
# indice = 0
# matematica = datos3['Matematica']
# print(matematica[indice])

# # 2. Archivos CSV ------------------------------------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------------------------------------
# # Importamos los datos 
# url = "https://covid.ourworldindata.org/data/ecdc/full_data.csv"
# wget(url)

# 2.1 Leemos nuestro archivo y configuramos PANDAS para que nos muestre los datos de interes -----------------------------
# ------------------------------------------------------------------------------------------------------------------------
# df = pd.read_csv("full_data.csv")
# pd.set_option("display.max_columns", 10) # Maxima cantidad de columnas que se muestran 

# ------------------------------------- SetUp PANDAS ---------------------------------------------------------------------
# pd.set_option("display.max_columns", 10) # Maxima cantidad de columnas que se muestran 
# ------------------------------------- Atributos del DataFrame-----------------------------------------------------------
# dataFrame.shape -> Nos devuelve el tamaño como (nb filas, nb columnas)
# dataFrame.size -> Nos devuelve el numero de celdas o filas (nb filas)
# ------------------------------------- Metodos del DataFrame-------------------------------------------------------------
# dataFrame.info() -> Nos da informacion de que hay en cada columna 
# dataFrame["columnName"].max() -> Nos devuelve el maximo de una columna especifica
# dataFrame["columnName"].sum() -> Nos devuelve la suma de los datos de una columna especifica
# ------------------------------------- Seleccion Excluyente--------------------------------------------------------------
# dataFrame[ d["col"] > 100 ]
# dataFrame[ d["name"] > "N" | d["Quimica"] > 21 ] -> Concatenacion de multiples condiciones "|" OR  "&" AND
# Las condiciones siguien el siguiente formato:
#       "dataframe[ propiedad ]"    "Condicion(>/</<=/...)"   "(número a comparar)"




# print(df.shape) # .shape -> Nos devuelve el tamaño como (nb filas, nb columnas)
# print(df.size) # .size -> Nos devuelve el numero de celdas o filas (nb filas)
# print(df.info()) # .info() -> Nos da informacion de que hay en cada columna 
# print(df[ df["new_cases"] == df["new_cases"].max() ]) # Me devuelve la fila en donde los nuevos casos son iguales al maximo numero de casos
# # Defino mi dataFrame igual al anterior, pero eliminando o exluyendo los datos de la fila World (para tener solo lo de paises)
# df = df[ df["location"] != "World" ]
# print(df[ df["new_cases"] == df["new_cases"].max() ])

################ CLASE 1 #################################################################################################
########### Mini Desafio 2 A #############################################################################################
# data = pd.read_excel("Datos.xlsx") 
# print("Promedio de Quimica:", data['Quimica'].sum() / len(data["Quimica"]))

################ CLASE 1 #################################################################################################
########### Mini Desafio 2 B #############################################################################################
# data = pd.read_excel("Datos.xlsx") 

# def promediosf(dataFrame, indice):
#   # return print("Alumno:",dataFrame.loc[indice]["Nombre"],dataFrame.loc[indice]["Apellido"],"\nQuimica:", dataFrame.loc[indice]["Quimica"], "\nMatematica:", dataFrame.loc[indice]["Matematica"], "\nFisica:", dataFrame.loc[indice]["Fisica"])
#   return print("Alumno:",dataFrame.loc[indice]["Nombre"],dataFrame.loc[indice]["Apellido"],"\nPromedio:", (dataFrame.loc[indice]["Quimica"] + dataFrame.loc[indice]["Matematica"] + dataFrame.loc[indice]["Fisica"])/3)

# print(data)
# promediosf(data, 0)  

################ CLASE 1 #################################################################################################
########### Otras operaciones y Filtrado #################################################################################
# data = pd.read_excel("Datos.xlsx") 
# print(data)

# # Operaciones
# promedios = (data['Quimica'] + data['Matematica'] + data['Fisica']) / 3
# print('\nTodos los promedios')
# print(promedios)
# print('El promedio maximo es', promedios.max())

# # Filtrado (Filtra y mantiene su indice original)
# aprobados = data[ data['Quimica'] >= 4 ]
# print("\nAprobados en Quimica:\n")
# print(aprobados)

# reprobaron = data[ (data['Quimica'] < 4) | (data['Matematica'] < 4) | (data['Fisica'] < 4) ]
# print("Reprobaron al menos una materia:")
# print(reprobaron)

# wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos2.xlsx")
# datos2 = pd.read_excel("Datos2.xlsx") 
# print("Datos:\n")
# print(datos2)

# datos2_matematica = datos2[ (datos2['Matematica'].notna()) & (datos2['Matematica'] != 'A')  ]
# # Note: .notna() -> Si el valor es NaN devuelve false, sino true (ya sea letra o numero)

# datos2_matematica = datos2_matematica['Matematica'] # Nos quedamos con la columna de interés
# print((datos2['Matematica'].notna()))
# print('Notas validas en Matematica: ')
# print(datos2_matematica)

################ CLASE 1 #################################################################################################
########### Mini Desafio 3 ###############################################################################################
# data = pd.read_excel("Datos.xlsx")
# print(data,"\n") 

# data = data[ data['Matematica'] > 4 ]
# promedioGeneral = data['Quimica'] + data['Matematica'] + data['Fisica']
# print(promedioGeneral)