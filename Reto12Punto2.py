#Definir una función para contar las consonantes en un string
def contadorConsonantes(texto: str)->int:
    contador = 0 #Inicializamos el contador de consonantes en 0
    # Realizar un condicional relacionado a la aparición de las consonantes
    for archivo in texto: 
        if archivo in "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz": #Indentar por cada elemento de aquel string que aparezca
            contador += 1 #Actulizar el contador por cada aparición de consonante
    return contador #Retornar el contador

#Llamar las funciones e imprimir el resultado    
if __name__ == "__main__":
    #Abrir el archivo en cuestión
    with open("mbox-short (1).txt", "r") as file:
     #Imprimir la función de contador de consonantes relacionada al archivo procesado
     print("La cantidad de consonantes en el texto procesado es de: "+str(contadorConsonantes(file.read()))+"")