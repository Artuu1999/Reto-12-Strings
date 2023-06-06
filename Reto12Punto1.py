#Definir una función para contar las vocales en un string
def contadorVocales(texto: str)->int:
    contador = 0 #Inicializamos el contador de voacles en 0
    # Realizar un condicional relacionado a la apareción de las vocales
    for archivo in texto: 
        if archivo in "AaEeIiOoUu": #Indentar por cada elemento de aquel string que aparezca
            contador += 1 #Actulizar el contador por cada aparición de vocal
    return contador #Retornar el contador     

#Llamar las funciones e imprimir el resultado    
if __name__ == "__main__":
    #Abrir el archivo en cuestión
    with open("mbox-short (1).txt", "r") as file:
     #Imprimir la función de contador de Vocales relacionada al archivo procesado
     print("La cantidad de vocales en el texto procesado es de: "+str(contadorVocales(file.read()))+"")