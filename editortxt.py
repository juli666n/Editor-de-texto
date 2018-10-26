while True:
    opcion = input("Ingrese 1 para escribir y generar un archivo .txt\nIngrese 2 para leer un archivo .txt\n")
    if opcion == 1:
        nombrew = raw_input("Ingrese el nombre del archivo\n")
        texto=open(nombrew + ".txt","w")
        contenido=raw_input("Ingrese el texto que quiere guardar en un archivo .txt\n")
        texto.write(contenido)
        texto.close()
    elif opcion == 2:
        nombrel = raw_input("Ingrese el nombre del archivo que desea leer. Recuerde que el archivo debe estar en la misma carpeta del programa\n")
        textol=open(nombrel,"r")
        print textol.read()
        print ("\n")
    else :
        print ("Opcion no valida. Ingrese una opcion valida")
