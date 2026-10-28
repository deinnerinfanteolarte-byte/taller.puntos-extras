print("==================================================")
print("     VERIFICADOR DE NÚMEROS NARCISISTAS")
print("==================================================")
print("Ingrese números enteros mayores que 0.")
print("El programa termina si ingresa 0 o un número negativo.\n")

while True:
    entrada = input("Ingrese un número: ")
    
    numero = int(entrada)
    
  
    if numero <= 0:
        print("Saliendo del programa. ¡Mucho éxito estudiando este fin de semana!")
        break
        
   
    cantidad_digitos = len(entrada)
    
  
    suma_narcisista = 0
    temp = numero
    
    while temp > 0:
        digito = temp % 10         
        suma_narcisista += digito ** cantidad_digitos  
        temp = temp // 10          
    # Paso 3: Comprobar si es narcisista
    if suma_narcisista == numero:
        print(f"¡El número {numero} ES un número narcisista!\n")
    else:
        print(f"El número {numero} NO es un número narcisista. (Suma obtenida: {suma_narcisista})\n")