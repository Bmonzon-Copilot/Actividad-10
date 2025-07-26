def invertir_texto(cadena):
      if len(cadena)==0:
          return ""
      else:
          invertir_texto(cadena[1:])+cadena[0]

def menu():
    while True:
        print("\n******MENU******")
        print("1. Invertir una cadena de texto")
        print("2. Calcular la suma de los primeros N números naturales")
        print("3. Imprimir una cuenta regresiva desde N hasta 1")
        print("4. Sumar los dígitos de un número")
        print("5. Contar cuántos dígitos tiene un número")
        print("6. Salir")
        opcion = input("Ingrese una opcion: ").strip()

        if opcion=="1":
            palabra = input("ingrese una plabra para invertirla: ")
            print("Cadena invertida:", invertir_texto(palabra))



menu()
