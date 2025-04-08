def decimal_to_roman(decimal):
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    if not isinstance(decimal, int) or decimal <= 0 or decimal > 3999:
        raise ValueError("Número debe estar entre 1 y 3999")
    
    resultado = ""
    for valor, simbolo in valores:
        while decimal >= valor:
            resultado += simbolo
            decimal -= valor
    return resultado

if __name__ == "__main__":
    try:
        print("Conversor a números romanos")
        numero = int(input("Ingrese un número (1-3999): "))
        print(f"Romano: {decimal_to_roman(numero)}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except KeyboardInterrupt:
        print("\nPrograma terminado")