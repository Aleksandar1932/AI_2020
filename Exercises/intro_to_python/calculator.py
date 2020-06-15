allowed_operations = ["+", "-", "*", "/", "%", "//", "**"]


def calculate(x, y, operator):
    if operator not in allowed_operations:
        return "INVALID ARGUMENTS"

    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y
    elif operator == "%":
        return x % y
    elif operator == "//":
        return x // y
    elif operator == "**":
        return x ** y


if __name__ == "__main__":
    op1 = float(input())
    operator = input()
    op2 = float(input())
    result = calculate(op1, op2, operator)
    if result == "INVALID ARGUMENTS":
        print(result)
    else:
        print(f"Resultat: {result}")

