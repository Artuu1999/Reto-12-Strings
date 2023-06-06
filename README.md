# Reto #12 Strings
Espero que se encuentren excelente estimados lectores, en el presente repositorio haremos varios ejemplos de código en Python utilizando lo aprendido acerca de los Strings dentro de nuestra clase de programación de computadores.

## Métodos Strings Python

### - endswith:
Verifica si una cadena termina en un sufijo determinado, siendo de caracter booleano, es decir, da como resultado True o False
```sh
cadenaTexto.endswith("sufijo")
```

### -- startswith:
Verifica si una cadena empieza con un prefijo determinado, siendo de caracter booleano, es decir, da como resultado True o False
```sh
cadenaTexto.endswith("prefijo")
```

### -- isalpha:
Indica si una cadena contiene únicamente letras del alfabeto; es de caracter booleano, es decir, da como resultado True o False
```sh
cadenaTexto.isalpha()
```

### -- isalnum:
Determina si una cadena específica contiene únicamente letras del alfabeto y números, también es de carácter booleano
```sh
cadenaTexto.isalnum()
```

### -- isdigit:
Determina si una cadena específica contiene únicamente números, Es de carácter booleano, indicando False o True
```sh
cadenaTexto.isdigit()
```

### -- isspace:
Verifica si una cadena de texto contiene únicamente carácteres de espacio o en blanco, su tipo es booleano
```sh
cadenaTexto.isspace()
```

### -- istitle:
Determina si una cadena de texto en el código tiene el formato de título, es decir la primera letra en mayúscula y las demás en minúscula, devulve False o True
```sh
cadenaTexto.istitle()
```

### -- islower:
Indica si todos los caracteres de una cadena son letras del alfabeto minúsculas, son boolenos.
```sh
cadenaTexto.islower()
```

### -- isupper:
Este método de caracter booleano indica si todos los caracteres de una cadena de texto son letras mayúsculas
```sh
cadena1.isupper()
```

## Ejemplos:
A continución se tendrá que procesar el siguiente archivo en Visual Studio Code <a href="https://drive.google.com/file/d/1lGmlAz157fIDp2zk95KInTSJguZusI91/view?usp=sharing">archivo</a>

## Ejemplo No. 1
Diseñar un código el cual determine la cantidad de vocales que contiene el archivo procesado anteriormente.
El código solución es el siguiente:
```sh
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
```
De la siguiente manera se ve el código funcionando:

![image](https://github.com/Artuu1999/Reto-12-Strings/assets/124615034/5bb7c9a9-043d-4a54-9b5c-e69f433d3699)


## Ejemplo No. 2
Diseñar un código el cual al ejecutarse determine la cantidad de consonantes que contiene el archivo procesado anteriormente.
El siguiente código soluciona el problema descrito anteriormente:
```sh
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
```
Al ejecutarse se evidencia de la siguiente manera:

![image](https://github.com/Artuu1999/Reto-12-Strings/assets/124615034/cec98c7a-9dc5-4120-94a4-26695205c068)


## Ejemplo No. 3
Diseñar un programa en python que indique las 50 palabras que más se  repiten en el texto.
A continuación el código solución en Python:
```sh
def obtenerPalabrasFrecuentes():
    archivo = 'mbox-short (1).txt' # Nombrar al texto con una variable
    with open(archivo, "r") as archivoTexto: # Abrir el archivo y leerlo
        dicpalabras = {}

        for line in archivoTexto:
            linea = line.split()
            for palabra in linea:
                if palabra in dicpalabras:
                    dicpalabras[palabra] += 1
                else:
                    dicpalabras[palabra] = 1

        listadepalabras = list(dicpalabras.items())
        listadepalabras.sort(key=lambda x: x[1], reverse=True)
        c50palabras = listadepalabras[:50]

        return c50palabras

# Llamar a la función y imprimir el resultado    
if __name__ == "__main__":
    palabras_frecuentes = obtenerPalabrasFrecuentes()
    print("Palabras que más aparecen:")
    for palabra, veces in palabras_frecuentes:
        print(palabra, ":", veces)

```
Así se ve el programa al ejecutarse

## Ejemplo No. 4
Crear un programa en Python que extraiga la cantidad de mensajes recibidos por destinatorio
El código solución es el siguiente:
```sh
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
```
Al correr el programa se evidencia así:

![image](https://github.com/Artuu1999/Reto-12-Strings/assets/124615034/7488feee-99a8-49db-ad24-fd77a02aa2ec)


## Ejemplo No. 5
Diseñar un código que de como resultado la cantidad de mensajes enviados por día, del texto procesado anteriormente.
La solución a dicho problema:
```sh
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
```
Ejecutando el programa se ve de la siguiente manera:

![image](https://github.com/Artuu1999/Reto-12-Strings/assets/124615034/684aa04b-22a0-483a-8dc6-0a40476412fb)


## Fin
Hasta acá llega nuestro camino en el presente repo, espero que haya sido de tu interés, si encuentras algún error o alguna inconsistencia, no dudes en contactarme y hacermela saber.
Muchas Gracias por tu atención.

   **"Nunca digas nunca, porque los límites, al igual que los miedos, son a menudo solo una ilusión "**
         - Michael Jordan
