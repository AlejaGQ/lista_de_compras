lista_compras = []

while True:
    #Opciones de Menú
    print("\nMenú de opciones:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Mostrar lista")
    print("4. Salir")

    #Obtener información del usuario
    opcion_usuario = input("Selecciona una de las 4 opciones: ")

    #Agregar artículo
    if opcion_usuario =="1":
        articulo = input("Ingrese el nombre del artículo: ")
        lista_compras.append(articulo)
        print(f"Artículo '{articulo}' agregado a la lista.")

    #Eliminar artículo 
    elif opcion_usuario =="2":
        articulo = input("Ingrese el nombre del artículo a eliminar: ")
        if articulo in lista_compras:
            lista_compras.remove(articulo)
            print(f"Artículo '{articulo}' eliminado de la lista")
        else:
            print(f"Artículo '{articulo}' no encontrado en la lista")
    
    #Mostrar lista
    elif opcion_usuario == "3":
        if lista_compras:
            print("\nLista de compras:")
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")
        else:
            print("La lista de compras está vacía")

    #Salir 
    if opcion_usuario == "4":
        print("Saliendo del programa")
        break

    #Para opción no válida
    else: 
        print("Opción no válida por favor marca una opción entre 1 y 4")

        