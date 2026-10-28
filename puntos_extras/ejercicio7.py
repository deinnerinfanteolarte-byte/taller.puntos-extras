def es_perfecto(n: int) -> bool:
    """Contrato: Recibe un entero n entre 1 y 10000 y devuelve verdadero si n es perfecto, falso en otro caso."""
    if n <= 1:
        return False

    suma_divisores = 0
   
    for d in range(1, n):
        if n % d == 0:
            suma_divisores += d

    return suma_divisores == n


def evaluar_dos_numeros_perfectos(num1: int, num2: int):
    """Escenario: Realiza dos llamadas y presenta los retornos por separado."""
    res1 = es_perfecto(num1)
    res2 = es_perfecto(num2)

    print(f"Números {num1} y {num2} -> Perfectos: {'verdadero' if res1 else 'falso'}; {'verdadero' if res2 else 'falso'}")


evaluar_dos_numeros_perfectos(6, 1)
evaluar_dos_numeros_perfectos(28, 12)