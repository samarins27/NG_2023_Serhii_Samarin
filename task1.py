num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operator = input("Введите оператор (+, -, *, /, **, //): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "**":
    result = num1 ** num2
elif operator == "//":
    result = num1 // num2
else:
    print("Ошибка: неправильный оператор!")
    exit()

print("Результат:", result)
