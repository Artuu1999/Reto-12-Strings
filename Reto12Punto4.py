# Función para hallar el correo en cuestión
def obtenerCorreo(linea):
    #Buscar en cada línea 5 indices después de la palabra from que es en donde inicia el correo
    inicio = linea.find('from ') + 5
    #Indicar el fin cuando se acabe el correo
    fin = linea.find(' ', inicio)
    correo = linea[inicio:fin] #Asignar a la variable correo desde el incio del correo hasta el final de este mismo
    return correo #Retornar la función

#Se crea una funación para obtener los destinatarios, con un argumento al que se le relacionara con el texto
def obtenerDestinatarios(archivo):
    #Se crea un diccionario en el que se almacenará los destinatarios
    destinatarios = {}
    #Con dicho método se abre el archivo en cuestión y se lee
    with open(archivo, 'r') as texto:
        #Se itera sobre cada línea del archivo
        for linea in texto:
            #Condicional por si aparece la palabra Received, que significa recibido
            if linea.startswith('Received:'):
                #Se llama la función para obtener el correo y se asocia a la variable correo
                correo = obtenerCorreo(linea)
                #Condicional por el valor es válido
                if correo:
                    #Se ubica en el diccionario vacío creado las claves de los correo y por cada apareción sumar 1 en el valor
                    destinatarios[correo] = destinatarios.get(correo, 0) + 1
    return destinatarios #Retornar la función

#Llamar las funciones e imprimir el resultado    
if __name__ == "__main__":
    archivo = 'mbox-short (1).txt' #Nombrar al texto con una variable
    frecuenciaDestinatarios = obtenerDestinatarios(archivo) #Llamar la dunción para obtener el diccionario de destinatarios
    print("Los destinarios con su respectiva cantidad de mensajes recibidos son:")
    #Ciclo for para cada elemento del diccionario e imprimer su clave y su valor
    for correo, cantidad in frecuenciaDestinatarios.items():
        print(""+str(correo)+": "+str(cantidad)+"")