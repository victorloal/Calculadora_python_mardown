from Calculadora_python_mardown.calculadora import Calculadora 
class MainCalculator:
    """Clase principal que maneja la interacción con el usuario y utiliza la calculadora."""

    def __init__(self):
        """Constructor de la clase MainCalculator."""
        self.calculadora = Calculadora()

    def ejecutar_calculadora(self):
        """Ejecuta la calculadora y maneja la interacción con el usuario."""
        print("Selecciona una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        

        opcion = input("Ingresa el número de la operación que deseas realizar: ")
        while True:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                break 
            except ValueError:
                print("Error: Ingresa números válidos, Intente de nuevo.")

        if opcion == '1':
            resultado = self.calculadora.suma(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == '2':
            resultado = self.calculadora.resta(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == '3':
            resultado = self.calculadora.multiplicacion(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == '4':
            resultado = self.calculadora.division(num1, num2)
            print(f"Resultado: {resultado}")
        else:
            print("Opción no válida")

if __name__ == "__main__":
    calculator = MainCalculator()
    calculator.ejecutar_calculadora()