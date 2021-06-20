#Переделываем задачу номер 4(про овощи) на функции.

def vegetableLower(name):
    return name.lower()

def vegetableUpper(name):
    return name.upper()

def vegetableTitle(name):
    return name.title()

def sum(count):
    return count

vegetable1 = input("1 овощ: ")
vegetable2 = input("2 овощ: ")
vegetable3 = input("3 овощ: ")

vegetables1 = int(input("сколько " + vegetable1 + ": "))
vegetables2 = int(input("сколько " + vegetable2 + ": "))
vegetables3 = int(input("сколько " + vegetable3 + ": "))

print('{} {}({}, {})'.format(sum(vegetables1), vegetableLower(vegetable1), vegetableUpper(vegetable1), vegetableLower(vegetable1)))
print('{} {}({}, {})'.format(sum(vegetables2), vegetableLower(vegetable3), vegetableUpper(vegetable2), vegetableLower(vegetable2)))
print('{} {}({}, {})'.format(sum(vegetables3), vegetableLower(vegetable3), vegetableUpper(vegetable3), vegetableLower(vegetable3)))



