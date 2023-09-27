class Calculadora:
    """Una calculadora simple que realiza operaciones de suma, resta, multiplicación y división."""

    def __init__(self):
        """Constructor de la clase Calculadora. No se requiere inicialización adicional."""
        pass

    def suma(self, a, b):
        """Realiza una suma entre dos números.

        Args:
            a (float): El primer número.
            b (float): El segundo número.

        Returns:
            float: El resultado de la suma.
        """
        return a + b

    def resta(self, a, b):
        """Realiza una resta entre dos números.

        Args:
            a (float): El primer número.
            b (float): El segundo número.

        Returns:
            float: El resultado de la resta.
        """
        return a - b

    def multiplicacion(self, a, b):
        """Realiza una multiplicación entre dos números.

        Args:
            a (float): El primer número.
            b (float): El segundo número.

        Returns:
            float: El resultado de la multiplicación.
        """
        return a * b

    def division(self, a, b):
        """Realiza una división entre dos números.

        Args:
            a (float): El numerador.
            b (float): El denominador.

        Returns:
            float o str: El resultado de la división o un mensaje de error si se intenta dividir por cero.
        """
        try:
            if b != 0:
                return a / b
            else:
                return "No se puede dividir por cero"
        except ZeroDivisionError:
            return "Error: división por cero"


