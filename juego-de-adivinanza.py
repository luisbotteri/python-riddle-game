import random

def jugar():

    numero_secreto = random.randint(0,100)
    adivinado = False
    cantidad_de_intentos = 0
    cantidad_max_de_intentos = 7

    print("¡Bienvenido/a al juego de adivinar el número secreto!")
    print("Para empezar, escriba 'Sí'.")

    palabra_de_acceso = input().strip().lower().replace("í", "i")

    if palabra_de_acceso != "si":
        print("El juego no se inició.")
        return
    else:
        
        print("¡Empezemos!")   

        while not adivinado and cantidad_de_intentos < cantidad_max_de_intentos:
            try:
                numero = int(input("Introduce un número del 0 al 100. Debe ser un número entero: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue
            if numero == numero_secreto:
                print("¡Felicitaciones, has adivinado el número secreto!")
                adivinado = True
            elif numero < numero_secreto:
                print("El número es mayor que el número ingresado recientemente.")
            else:
                print("El número es menor al número ingresado recientemente.")

            cantidad_de_intentos += 1    

        if cantidad_de_intentos >= cantidad_max_de_intentos:
            print("¡Game over! Has excedido el límite de intentos.")

    while True:
        jugar()
        print("¿Deseas volver a jugar? (Sí/No)") 
        continuar = input().strip().lower().replace("í", "i")      
        if continuar != "si":
            print("Gracias por haber jugado. ¡Hasta la próxima!")
            break
