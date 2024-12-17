from select_operation import select_operation


def main():
    print("Este progama es una calculadora basica.")
    print("Puedes sumar, restar, multiplicar y dividir")

    while True:
        operation = input("Ingresa la operacion en una sola linea (o la tecla q para salir): ")

        if operation.lower() == "q":
            break

        try:
            result = select_operation(operation)
            print(f"result= {result}")

        except (ValueError, IndexError):
            print("La operacion ingresada no es valida. Intente de nuevo.")


if __name__ == "__main__":
    main()