#Función para las fechas encontradas
def obtenerSegmentos(cadena: str) -> list:
    segmentos = [] #Lista vacía para las fechas encontradas
    palabras = cadena.split() #Separar la cadena de texto
    for i in range(len(palabras)): #Ciclo for para la longitud de las palabra
        #Se realiza un condicional para cuando comience por recibido
        if palabras[i] == "Received:":
            segmento = [] #Lista vacía para agrupar las fechas encontradas
            #Indentar por cada aparicón antes del -0500 o de GMT
            while palabras[i] != "-0500" and palabras[i] != "(GMT)":
                segmento.append(palabras[i]) #Se agregan los elementos encontrados a la lista
                i += 1 #Se actualiza el ciclo while
            segmentos.append(segmento) #Se agregan los elementos a la lista de segmentos
    return segmentos #Retornamos la función

#Función para obtener la cantidad de mensaje por día
def obtenerCantidadMensajesPorDia(segmentos: list) -> dict:
    #Diccionario para la cantidad de mensajes y relacionarlas con el día
    cantidadMensajes = {}
    #Ciclo for para  iterar cada fecha
    for segmento in segmentos:
        dia = int(segmento[segmento.index('Jan') - 1]) #Se accede un elemento anterior al elemento Jan
        #Condiciona para verificar si el día se encuentra en la cantidad de mensajes y se actualiza el diccionario
        if dia in cantidadMensajes:
            cantidadMensajes[dia] += 1
        else:
            cantidadMensajes[dia] = 1
    return cantidadMensajes #Se retorna la función

#Llamar las funciones e imprimir el resultado    
if __name__ == "__main__":
    archivo = 'mbox-short (1).txt' #Nombrar al texto con una variable
    with open(archivo, "r") as archivoTexto: #Abrir el archivo y leerlo
        cadena = archivoTexto.read() #Declarar la variable cadena con el texto
        #Llamar las funciones definidas anteriormente
        segmentos = obtenerSegmentos(cadena)
        cantidadMensajes = obtenerCantidadMensajesPorDia(segmentos)
        #Ciclo for para imprimir cada día y la cantidad de mensajes respectiva
        for dia, cantidad in cantidadMensajes.items():
            print("El día " + str(dia) + " de enero de 2008 se enviaron " + str(cantidad) + " mensajes")