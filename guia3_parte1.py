def agregar_medicina(archivo=None):
    lab = -1
    print("Indique el laboratorio en el que desea agregar un nuevo medicamento: \n")
    print("1: Laboratorio 1.")
    print("2: Laboratorio 2.")
    print("Pulse '0' para volver al menú")
    try:
        lab = int(input())
    except ValueError:
        print("Ingrese un número por favor.")
        agregar_medicina()

    if lab == 1:
        archivo = open("Laboratorio_1.txt", "a")
        print("Agregue el nuevo medicamento y sus parámetros: \n")
        cadena = input("Codigo del producto (3 cifras): ")
        cadena2 = input("Nombre del farmaco: ")
        cadena3 = input("Componente principal: ")
        cadena4 = input("Precio de venta (4 cifras): ")
        archivo.write("\n" + "Codigo del producto: " + cadena + "\n")
        archivo.write("Nombre del farmaco: " + cadena2 + "\n")
        archivo.write("Componente principal: " + cadena3 + "\n")
        archivo.write("Precio de venta: " + cadena4 + "\n")
        archivo.close()
        agregar_medicina()

    elif lab == 2:
        archivo = open("Laboratorio_2.txt", "a")
        print("Agregue el nuevo medicamento y sus parámetros: \n")
        cadena = input("Codigo del producto (3 cifras): ")
        cadena2 = input("Nombre del farmaco: ")
        cadena3 = input("Componente principal: ")
        cadena4 = input("Precio de venta (4 cifras): ")
        archivo.write("\n" + "Codigo del producto: " + cadena + "\n")
        archivo.write("Nombre del farmaco: " + cadena2 + "\n")
        archivo.write("Componente principal: " + cadena3 + "\n")
        archivo.write("Precio de venta: " + cadena4 + "\n")
        archivo.close()
        agregar_medicina()

    elif lab == 0:
        print("Volviendo al menú principal. \n")
        menu()

    else:
        print("Ingrese un número de laboratorio válido. \n")
        agregar_medicina()

def consulta_precio(archivo=None):
    lab = -1
    indi = -1
    print("En que laboratorio se encuentra el medicamento: ")
    print("1: Laboratorio 1. ")
    print("2: Laboratorio 2. ")
    print("Pulse '0' para volver al menú")
    try:
        lab = int(input())
    except ValueError:
        print("Ingrese un número por favor.")
        consulta_precio()

    if lab == 1:
        archivo = open("Laboratorio_1.txt", "r")
        print("¿Este medicamento estaba en lista o fue agregado? \n ")
        print("1: En lista. ")
        print("2: Agregado. ")
        print("Pulse '0' para volver al menú")

        try:
            indi = int(input())
        except ValueError:
            print("Ingrese un número por favor.")
            consulta_precio()

        if indi == 1:
            contenido = archivo.readlines()
            med = (input("Ingrese el codigo del medicamento a consultar: "))
            codigos = [contenido[0], contenido[5], contenido[10]]
            precios = [contenido[3], contenido[3+5], contenido[3+10]]
            if med == codigos[0][21:24]:
                print("El precio del medicamento es:", precios[0][17:21], "pesos")
                archivo.close()
                consulta_precio()
            elif med == codigos[1][21:24]:
                print("El precio del medicamento es:", precios[1][17:21], "pesos")
                archivo.close()
                consulta_precio()

            elif med == codigos[2][21:24]:
                print("El precio del medicamento es:", precios[2][17:21], "pesos")
                archivo.close()
                consulta_precio()
            else:
                print("Ingrese un codigo que este en la lista original.")
                consulta_precio()
            archivo.close()
        elif indi == 2:
            contenido = archivo.readlines()
            add = 0
            add2 = 5
            add1 = int(input("Número de medicamentos recientemente ingresados: "))
            if add1 == 0:
                print("Ingrese un número solo si hay medicamentos agregados. ")
                consulta_precio()
            med = (input("Ingrese el codigo del medicamento a consultar: "))

            while add != add1:
                if med == contenido[0+10+add2][21:24]:
                    print("El precio del medicamento es", contenido[3+10+add2][17:21], "pesos")
                    archivo.close()
                    consulta_precio()
                else:
                    add = add + 1
                    add2 = add2 + 5
        elif indi == 0:
            print("Volviendo al menú principal. \n")
            menu()
        else:
            print("Ingrese un número válido. ")
            consulta_precio()

    elif lab == 2:
        archivo = open("Laboratorio_2.txt", "r")
        print("¿Este medicamento estaba en lista o fue agregado? \n ")
        print("1: En lista. ")
        print("2: Agregado. ")
        print("Pulse '0' para volver al menú")

        try:
            indi = int(input())
        except ValueError:
            print("Ingrese un número por favor.")
            consulta_precio()

        if indi == 1:
            contenido = archivo.readlines()
            med = (input("Ingrese el codigo del medicamento a consultar: "))
            codigos = [contenido[0], contenido[5], contenido[10]]
            precios = [contenido[3], contenido[3+5], contenido[3+10]]
            if med == codigos[0][21:24]:
                print("El precio del medicamento es:", precios[0][17:21], "pesos")
                archivo.close()
                consulta_precio()
            elif med == codigos[1][21:24]:
                print("El precio del medicamento es:", precios[1][17:21], "pesos")
                archivo.close()
                consulta_precio()

            elif med == codigos[2][21:24]:
                print("El precio del medicamento es:", precios[2][17:21], "pesos")
                archivo.close()
                consulta_precio()
            else:
                print("Ingrese un codigo que este en la lista original.")
                consulta_precio()

        elif indi == 2:
            contenido = archivo.readlines()
            add = 0
            add2 = 5
            add1 = int(input("Número de medicamentos recientemente ingresados: "))
            if add1 == 0:
                print("Ingrese un número solo si hay medicamentos agregados. ")
                consulta_precio()
            med = (input("Ingrese el codigo del medicamento a consultar: "))

            while add != add1:
                 if med == contenido[0+10+add2][21:24]:
                    print("El precio del medicamento es", contenido[3+10+add2][17:21], "pesos")
                    archivo.close()
                    consulta_precio()
                 else:
                    add = add + 1
                    add2 = add2 + 5
        elif indi == 0:
            print("Volviendo al menú principal. \n")
            menu()
        else:
            print("Ingrese un número válido. ")
            consulta_precio()

    elif lab == 0:
        print("Volviendo al menú principal. \n")
        menu()
    else:
        print("Ingrese un número de laboratorio válido")
        consulta_precio()


def editar_medicina(archivo=None):
    ed = -1
    print("El medicamento a editar se encuentra en el: ")
    print("1: Laboratorio 1. ")
    print("2: Laboratorio 2. ")
    print("Pulse '0' para volver al menú")

    try:
        ed = int(input())
    except ValueError:
        print("Ingrese un número por favor")
        editar_medicina()

    if ed == 1:
        archivo = open("Laboratorio_1.txt", "r")
        texto = archivo.read()
        print("Ingrese lo que desea editar: ")
        cam = input()
        print("Ingrese lo editado a continuación: ")
        re = input()

        texto = texto.replace(cam, re)
        archivo.close()

        archivo = open("Laboratorio_1.txt", "w")
        archivo.write(texto)
        archivo.close()
        editar_medicina()

    elif ed == 2:
        archivo = open("Laboratorio_2.txt", "r")
        texto = archivo.read()
        print("Ingrese lo que desea editar: ")
        cam = input()
        print("Ingrese lo editado a continuación: ")
        re = input()

        texto = texto.replace(cam, re)
        archivo.close()

        archivo = open("Laboratorio_2.txt", "w")
        archivo.write(texto)
        archivo.close()
        editar_medicina()

    elif ed == 0:
        print("Volviendo al menú principal. \n")
        menu()

    else:
        print("Ingrese un número válido. \n")
        editar_medicina()


def informacion_labs(archivo=None):
    num = -1
    print("Indique cual es el laboratorio del cual quiere saber su información: ")
    print("1: Laboratorio 1. ")
    print("2: Laboratorio 2. ")
    print("Pulse '0' para volver al menú")
    try:
        num = int(input())
    except ValueError:
        print("Ingrese un número por favor")

    if num == 1:
        archivo_1 = open("Laboratorios.txt", "r")
        linea_nombre = archivo_1.readlines()
        mensaje = (linea_nombre[0] + linea_nombre[1])
        print(mensaje)

        archivo_2 = open("Laboratorio_1.txt", "r")
        linea_lab = archivo_2.readline()
        print(linea_lab, end="")
        while linea_lab != "":
             linea_lab = archivo_2.readline()
             print(linea_lab, end="")
        print(" ")

        archivo_1.close()
        archivo_2.close()
        informacion_labs()

    elif num == 2:
        archivo_1 = open("Laboratorios.txt", "r")
        linea_nombre = archivo_1.readlines()
        mensaje = (linea_nombre[3] + linea_nombre[4])
        print(mensaje)

        archivo_2 = open("Laboratorio_2.txt", "r")
        linea_lab = archivo_2.readline()
        print(linea_lab, end="")
        while linea_lab != "":
             linea_lab = archivo_2.readline()
             print(linea_lab, end="")
        print(" ")

        archivo_1.close()
        archivo_2.close()
        informacion_labs()

    elif num == 0:
        print("Volviendo al menú principal. \n")
        menu()

    else:
        print("Ingrese un número válido. \n")
        informacion_labs()


def menu():
    choice = -1
    print("                    Menú principal de base de datos                            ")
    print("Farmacéutica G.H.F ")
    print("¿Que desea? Ingrese el dígito de su opción: ")
    print("1: Agregar un medicamento a la base de datos. ")
    print("2: Consultar el precio de un medicamento en específico. ")
    print("3: Editar la información de un medicamento. ")
    print("4: Información de los laboratorios asociados. ")
    print("Pulse '0' para salir de la base de datos. ")
    try:
        choice = int(input())
    except ValueError:
        print("Ingrese un número por favor.")

    if choice == 0:
        print("Gracias por utilizar la base de datos. ")
        print("Nos vemos en otra ocasión, ten un buen día. ")
        quit()
    elif choice == 1:
        print("Ok, vamos a agregar un nuevo medicamento. ")
        agregar_medicina()
    elif choice == 2:
        print("Ok, vamos a consultar los precios de los medicamentos. ")
        consulta_precio()
    elif choice == 3:
        print("Ok, editemos la información de algún medicamento. ")
        editar_medicina()
    elif choice == 4:
        print("Ok, miremos la información de los laboratorios asociados. ")
        informacion_labs()
    else:
        print("Ingrese un dígito disponible. \n")
        menu()

if __name__ == '__main__':
    menu()
