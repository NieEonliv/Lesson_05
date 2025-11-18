minSum = int(input("Минимальная сумма инвестиций: "))
mike = int(input("$ у Майкла: "))
ivan = int(input("$ у Ивана: "))

if ivan + mike < minSum:
    print(0)
    exit()

if ivan >= minSum & mike >= minSum:
    print(2)
    exit()

if ivan >= minSum:
    print("Ivan")
elif mike >= minSum:
    print("Mike")
else:
    print(1)

