import pandas as pd
import os
from typing import List, Any
def index_byname(name,List):
  k=0
  for subList in (List):
    if subList[1]==name:
      return k
    k += 1
  return -1
try:
    while True:
        df_existente = pd.read_excel("Cuentas.xlsx")
        value_list = df_existente.values.tolist()
        while True:
            print("  1. eliminar registro  "+ " \n "+
                "2. modificar ")
            Opc = input("Que opcion desea? ").strip()
            if Opc == "1" or Opc == "2":
                break
            else:
                print("opcion mal digitada ")

        if Opc.strip() == "1":
            
            while True:
                name=input("Digite el nombre del articulo a eliminar : ")  
                value = index_byname(name, value_list)
                if value>=0:
                    value_list.remove(value_list[value])
                    print("maybe")
                    break
                else:
                    print("el nombre no esta en las cuentas")
            

        elif Opc.strip() == "2":
            while True:
                name=input("Digite el nombre del articulo a modificar: ")   
                value = index_byname(name, value_list)
                if value>=0:
                    break
                else:
                    print("el nombre no esta en las cuentas")

            while True:
                print(" a. Nombre"+ " \n"+
                    " b. Cantidad "+" \n" +
                    " c. Fecha de vencimiento")
                mod = input(f"Que desea modificar de {name} ? (digite a,b o c) ").strip()
                letras = ["a","b","c"]
                if mod in letras :
                    break

            if mod == "a":
                    new_name=input("digite el nuevo nombre: ")
                    value_list[value][1]=new_name
                    pass
            elif mod == "b":
                    cnt=input("Digite la cantidad nueva: ")
                    value_list[value][2]=cnt
                    pass
            elif mod == "c":
                    fchv=input("digite la nueva fecha de vencimiento: ")
                    value_list[value][3]=fchv

                    pass
        dec=input("desea hacer otro cambio?").strip().lower()
        if dec!="si":
            break
    new=pd.DataFrame(value_list,columns= ['Fecha de registro','Nombre','Cantidad','Fecha de vencimiento'])
    archivo_existente="Cuentas.xlsx"
    if os.path.exists(archivo_existente):
        os.remove(archivo_existente)
    new.to_excel("Cuentas.xlsx", index=False)
        
except FileNotFoundError:
    df_existente = pd.DataFrame()

   