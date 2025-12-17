class OperadorInvalidoError(Exception):
    def __init__(self, operador):
        self.operador = operador
        super().__init__(f"Operador '{operador}' no es válido. Use +, -, *, /")

def operacion_un_string(cadena):
    try:
        # Separa los componentes
        partes = cadena.split()
        # Valida que haya exactamente 3 partes
        if len(partes) != 3:
            raise ValueError("¡Formato incorrecto! Use: numero operador numero")
        num_1_str, operador, num_2_str = partes

        num_1 = float(num_1_str)
        num_2 = float(num_2_str)
        
        if operador not in ['+', '-', '*', '/']:
            raise OperadorInvalidoError(operador)
        
        if operador == "+":
            resultado = num_1 + num_2
        elif operador == "-":
            resultado = num_1 - num_2
        elif operador == "*":
            resultado = num_1 * num_2
        elif operador == "/":
            if num_2 == 0:
                raise ZeroDivisionError("¡No se puede dividir entre cero!")
            resultado = num_1 / num_2
        return f"Resultado: {resultado}"
    
    except ValueError as e:
        return "Error: Los valores ingresados no son números válidos"
    
    except ZeroDivisionError as e:
        return f"Error matemático: {e}"
    
    except OperadorInvalidoError as e:
        return str(e)


print("=" * 25)
print("CALCULADORA")
print("=" * 25)
print("Formato: numero operador numero")
print("Ejemplo: 10 / 2")
print("=" * 20)

cadena_ing = input("Ingrese su operación: ")
resultado = operacion_un_string(cadena_ing)
print(resultado)