import csv 
import pathlib
import json

def leer_csv_login(ruta_archivo):
  datos = []
  ruta = pathlib.Path(ruta_archivo)

  with open(ruta, newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
      debe_funcionar = fila["debe_funcionar"].lower() == "true"
      datos.append((fila["usuario"], fila["clave"], debe_funcionar, fila["descripcion"]))

  return datos

def leer_json_productos(ruta_archivo):
  with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    productos = json.load(archivo)
  
  return productos