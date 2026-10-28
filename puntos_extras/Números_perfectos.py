print("==================================================")
print("     VERIFICADOR DE NÚMEROS PERFECTOS")
print("==================================================")
print("Ingrese números enteros mayores a 2.")
print("Escriba un número NEGATIVO para terminar el programa.\n")

while True:
    numero = int(input("Ingrese un número: "))
    
   
    if numero < 0:
        print("Saliendo del programa. ¡Mucho éxito con tu estudio!")
        break
        
   
    if numero <= 2:
        print("El número debe ser mayor a 2. Inténtalo de nuevo.\n")
        continue
        
   
    suma_divisores = 0
    
  
    for i in range(1, numero):
        if numero % i == 0:  # Si i es divisor exacto
            suma_divisores += i
            
    
    if suma_divisores == numero:
        print(f"¡El número {numero} ES un número perfecto!\n")
    else:
        print(f"El número {numero} NO es un número perfecto. (Suma de divisores: {suma_divisores})\n")