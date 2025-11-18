value = int(input("Введите число: "))

if value == 0:
    print("нулевое число")
    exit()

parity = "четное" if value % 2 == 0 else "нечетное"

if value > 0:
    print(f"Положительное {parity} число")
else:
    print(f"Отрицательное {parity} число")