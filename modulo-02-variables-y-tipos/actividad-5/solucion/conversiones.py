texto_entero = "3"
texto_decimal = "3.5"
numero = 42

print("texto_entero:", texto_entero, "tipo:", type(texto_entero))
texto_entero = int(texto_entero)
print("texto_entero:", texto_entero, "tipo:", type(texto_entero))


print("texto_decimal:", texto_decimal, "tipo:", type(texto_decimal))
texto_decimal = float(texto_decimal)
print("texto_decimal:", texto_decimal, "tipo:", type(texto_decimal))

print("numero:", numero, "tipo:", type(numero))
numero = str(numero)
print("numero:", numero, "tipo:", type(numero))