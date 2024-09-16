def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль!"

# Пример использования:
num1 = float(input("Введите первое число: "))
operator = input("Выберите операцию (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "Неправильная операция. Пожалуйста, выберите +, -, *, или /."

print(f"Результат: {result}")
