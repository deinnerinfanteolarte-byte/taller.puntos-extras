def evaluar_temperatura_incubacion():
    print("==================================================")
    print("  SISTEMA DE CONTROL DE INCUBACIÓN DE TORTUGAS")
    print("==================================================")
    
    # Contadores para llevar la estadística de las mediciones
    total_registros = 0
    cant_bajas = 0
    cant_normales = 0
    cant_altas = 0
    
    while True:
        entrada = input("\nIngrese la temperatura registrada (°C) o escriba 'salir' para terminar: ")
        
        # Condición para salir del bucle
        if entrada.lower() == 'salir':
            print("\n--- RESUMEN DE LA JORNADA ---")
            print(f"Total de mediciones realizadas: {total_registros}")
            print(f"Temperaturas T. baja: {cant_bajas}")
            print(f"Temperaturas T. normal: {cant_normales}")
            print(f"Temperaturas T. alta: {cant_altas}")
            print("Saliendo del sistema de monitoreo. ¡Hasta pronto!")
            break
            
        # Conversión de texto a número decimal
        temperatura = float(entrada)
        total_registros += 1
        
        # Evaluación de rangos y conteo automático
        if temperatura < 26.0:
            print("T. baja")
            cant_bajas += 1
        elif 26.0 <= temperatura <= 34.0:
            print("T. normal")
            cant_normales += 1
        else:
            print("T. alta")
            cant_altas += 1

# Ejecución del programa
if __name__ == "__main__":
    evaluar_temperatura_incubacion()