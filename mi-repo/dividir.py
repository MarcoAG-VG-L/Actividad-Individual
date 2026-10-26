def dividir(a: int, b: int) -> float:
    return a / b


def main():
    try:
        a = int(input("Indique un número a dividir: "))
        b = int(input("Indique un número de divisor: "))
        print(dividir(a, b))
    except ValueError:
        print("Error: debe introducir números enteros.")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")


if __name__ == "__main__":
    main()
