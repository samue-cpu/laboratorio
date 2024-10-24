
#ejercicio 1

def procesar_texto():
    while True:
        nombre_archivo = input("Ingrese el nombre del archivo (incluya la extensión .txt): ")
        try:
            with open(nombre_archivo, "a") as archivo:
                nuevo_texto = input("Ingrese el texto que desea agregar: ")
                archivo.write(nuevo_texto + "\n")
            print(f"El texto se ha agregado al archivo {nombre_archivo}")
            break
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe. Intente nuevamente.")

if __name__ == "__main__":
    procesar_texto()
    
    ###############
#ejercicio 3
#############

def buscador_de_palabras():
    nombre_archivo = input("Ingrese el nombre del archivo (incluya la extensión .txt): ")
    palabra_buscada = input("Ingrese la palabra a buscar: ")

    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            for i, linea in enumerate(lineas):
                if palabra_buscada in linea:
                    print(f"Línea {i+1}: {linea.strip()}")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe. Intente nuevamente.")

if __name__ == "__main__":
    buscador_de_palabras()
    
##############
#ejercicio 9
########

import datetime

def registrar_evento(tipo_evento, mensaje):
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro = f"{fecha_hora} - {tipo_evento}: {mensaje}\n"
    with open("registro.txt", "a") as archivo_registro:
        archivo_registro.write(registro)

if __name__ == "__main__":
    registrar_evento("inicio de sesión", "Usuario 'admin' inició sesión.")
    registrar_evento("error", "Error al conectar con la base de datos.")
