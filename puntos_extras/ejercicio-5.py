def comprobar_multiplos(num1: int, divisor: int) -> tuple[bool, bool]:

    if divisor == 0:
        res1 = False
    else:
        res1 = num1 % divisor == 0

   
    if num1 == 0:
        res2 = False
    else:
        res2 = divisor % num1 == 0

    return res1, res2



v1, v2 = 12, 4
r1, r2 = comprobar_multiplos(v1, v2)
print(f"Valores {v1} y {v2}")
print(f"{v1} múltiplo de {v2}: {'verdadero' if r1 else 'false'}; {v2} múltiplo de {v1}: {'falso' if r2 else 'verdadero'}")

v1, v2 = 0, 5
r1, r2 = comprobar_multiplos(v1, v2)
print(f"\nValores {v1} y {v2}")
print(f"{v1} múltiplo de {v2}: {'verdadero' if r1 else 'falso'}; {v2} múltiplo de {v1}: {'falso' if r2 else 'verdadero'}")