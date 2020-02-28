operations = ["+", "-", "*", "/", "%", "//", "**"]  # Allowed arithmetical operations


def calculate(x, y, operation):
    if operation not in operations:
        return "Greska"

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
    x = float(input())
    operator = input()
    y = float(input())
    print("Result: {}".format(calculate(x, y, operator)))
