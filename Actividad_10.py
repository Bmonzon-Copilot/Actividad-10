def invertir_texto(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return invertir_texto(cadena[1:]) + cadena[0]

def calcula_suma(numero):
    if numero==1:
        return 1
    else:
        return numero + calcula_suma(numero-1)

import time
def cuenta_regresiva(segundo):
    if segundo == 0:
        return
    print(segundo)
    time.sleep(1)
    cuenta_regresiva(segundo-1)

def suma_digitos(numero):
    if numero == 0:
        return 0
    else:
        return numero%10+suma_digitos(numero//10)

def contar_digito(numero):
    if numero<10:
        return 1
    else:
        return 1+contar_digito(numero//10)



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
        elif opcion=="2":
            num= int(input("ingrese un numero: "))
            print("La suma es: ",calcula_suma(num))
        elif opcion=="3":
            seg=int(input("Ingrese un numero positivo: "))
            print("Cuenta regresiva...")
            cuenta_regresiva(seg)
        elif opcion=="4":
            num= int(input("Ingrese un numero para sumar sus digitos: "))
            print("La suma de los digitos es: ",suma_digitos(num))
        elif opcion=="5":
            num=int(input("Ingrese un numero positivo: "))
            print("la cantidad de digitos es: ",contar_digito(num))
        elif opcion=="6":
            print("Saliendo...")
            break
        else:
            print("Opcion Invalida")




menu()
