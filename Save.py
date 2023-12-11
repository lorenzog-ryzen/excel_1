import pandas as pd
import datetime
import os
try:
    df_existente = pd.read_excel("Cuentas.xlsx")
except FileNotFoundError:
    df_existente = pd.DataFrame()

fecha_actual = datetime.datetime.now()

formato_personalizado = "%Y-%m-%d %H:%M:%S"
fecha_formateada = fecha_actual.strftime(formato_personalizado)
print("Fecha formateada:", fecha_formateada)
dix={0:'Nombre', 1:"Cantidad",2: "Fecha de vencimiento" }
n=int(input("Cuantos productos desea agregar? ")); i=0
lst=[[],[],[]]
while (i<n):
  for j in range(3):
    lst[j].append(input(f"digite {dix[j]} del producto {i+1} : "))
  i +=1

nuevos_datos = {
    'Fecha de registro': [fecha_formateada[0:10]]*n,
    'Nombre': lst[0],
    'Cantidad': lst[1],
    'Fecha de vencimiento ': lst[2]
}

df_nuevos = pd.DataFrame(nuevos_datos)

df_resultante = pd.concat([df_existente, df_nuevos], ignore_index=True)

print(df_resultante)

# Eliminar el archivo existente si es necesario
archivo_existente="Cuentas.xlsx"
if os.path.exists(archivo_existente):
    os.remove(archivo_existente)

df_resultante.to_excel(archivo_existente, index=False)

print("Archivo actualizado exitosamente.")
