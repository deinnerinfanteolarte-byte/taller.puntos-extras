def es_bisiesto(anio: int) -> bool:
    """Contrato: Recibe un año entre 1 y 9999 y devuelve verdadero si es bisiesto; falso en otro caso."""
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def evaluar_dos_anios(anio1: int, anio2: int):
    """Escenario: Hace dos llamadas y compara si comparten la misma condición."""
    res1 = es_bisiesto(anio1)
    res2 = es_bisiesto(anio2)

    misma_condicion = res1 == res2

    
    print(f"Años {anio1} y {anio2} -> Bisiestos: {'verdadero' if res1 else 'falso'}; {'verdadero' if res2 else 'falso'}; misma condición: {'verdadero' if misma_condicion else 'falso'}")


evaluar_dos_anios(1900, 2000)
evaluar_dos_anios(2024, 2023)