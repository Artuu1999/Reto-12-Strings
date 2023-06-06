#Definimos una función para hallar la palabras más frecuentes
def obtenerPalabrasFrecuentes():
    archivo = 'mbox-short (1).txt'  # Nombrar al texto con una variable
    with open(archivo, "r") as archivoTexto:  # Abrir el archivo y leerlo
        palabrasFrecuentes = {} #Crear un diccionario vacio en el que se incluirá los elementos
        for line in archivoTexto: #Ciclo for para iterar sobre cada línea del texto
            linea = line.split() #Separar el texto
            for palabra in linea: #Ciclo for para iterar sobre cada palabra en la línea
                #Condicional para verificar aparición y actualizar con cada aparición
                if palabra in palabrasFrecuentes:
                    palabrasFrecuentes[palabra] += 1
                else:
                    palabrasFrecuentes[palabra] = 1
        #Convertir el diccionario en una lista
        frecuencia = list(palabrasFrecuentes.items())
        #Ordenar la lista por frecuencia de manera descendente
        frecuencia.sort(key=lambda x: x[1], reverse=True)
        listadoPalabras = frecuencia[:50] #Obtener las 50 palabras más frecuentes
        return listadoPalabras #Retornar la función
    
# Llamar a la función y imprimir el resultado    
if __name__ == "__main__":
    #Llamar la función definida anteriormente
    palabrasFrecuentes = obtenerPalabrasFrecuentes()
    print("Las palabras más frecuentes en el texto son las siguientes:")
    #Ciclo for para imprimir clave y valor del diccionario de palabrasFrecuentes
    for palabra, veces in palabrasFrecuentes:
        print(" "+str(palabra)+": "+str(veces)+"")