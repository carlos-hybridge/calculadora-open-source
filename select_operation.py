from dividir import dividir
from multiplicacion import multiplicacion
from resta import resta
from sumar import sumar


def select_operation(operacion):

    try:
        # Detectar la operación ingresada
        if "+" in operacion:
            a, b = map(float, operacion.split("+"))
            resultado = sumar(a, b)
        elif "-" in operacion:
            a, b = map(float, operacion.split("-"))
            resultado = resta(a, b)
        elif "*" in operacion:
            a, b = map(float, operacion.split("*"))
            resultado = multiplicacion(a, b)
        elif "/" in operacion:
            a, b = map(float, operacion.split("/"))
            resultado = dividir(a, b)
        else:
            return "Operación no válida"

        return f"Resultado: {resultado}"

    except ValueError:
        return "Error: Ingresa una operación válida con dos números"
