def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Выберите: 1 - C в F, 2 - F в C: ")
if choice == "1":
    c = float(input("Введите температуру в Цельсиях: "))
    print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
elif choice == "2":
    f = float(input("Введите температуру в Фаренгейтах: "))
    print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
else:
    print("Неверный выбор!")