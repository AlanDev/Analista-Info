import csv

def calcular_total_ventas(archivo_csv):
  suma_venta = 0
  try:
    with open (archivo_csv,'r' ) as archivo:
      lectura = csv.reader(archivo , delimiter=';')
      next(lectura)
      
      for line in lectura: 
        suma_venta += float(line[7])

  except FileNotFoundError:
    print(f"Error:El archivo {archivo_csv} no fue encontrado")
  except ValueError:
    print("Error: Se encontro un valor no numero")
  except Exception as error:
    print("Error inesperado:{error}")
  else:
    return suma_venta
  finally:
    print("Hola soy el Finallly")


archivo = "ventas.csv"
suma_total = calcular_total_ventas(archivo)

if suma_total:
    print(f'Suma total: {suma_total:.2f}')