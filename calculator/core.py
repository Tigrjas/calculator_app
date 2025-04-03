
def calculator(a: int, b:int, operator:str):
    """Performs basic arithmetic operations"""
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
        case _: # Default case (if no match is found)
            raise ValueError("Invalid operator")
