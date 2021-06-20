#Сделать из функций калькулятора отдельный класс.
import math
import random

class Calculator:
    def plus(self, number1, number2):
        return number1 + number2

    def minus(self, number1, number2):
        return number1 - number2

    def div(self, number1, number2):
        if number2 != 0:
            return number1 / number2
        else:
            print("на 0 делить нельзя")

    def multi(self, number1, number2):
        return number1 * number2

    def pow(self, number1, number2):
        return math.pow(number1, number2)

    def module(self, number1):
        return abs(number1)

    def rand(self, number1, number2):
        return random.uniform(number1, number2)

    def whole_div(self, number1, number2):
        if number2 != 0:
            return number1 // number2
        else:
            print("на 0 делить нельзя")

    def mod(self, number1, number2):
        return number1 % number2

    def factorial(self, number1):
        return math.factorial(number1)

    def arccos(self, number1):
        return number1*math.pi/180

calc = Calculator()
do = input("ввести арифметический оператор: ")
while do != "exit":
    if do == "+":
        print(calc.plus(number1 = float(input("ввести 1 значение: ")),number2 = float(input("ввести 2 значение: "))))

    elif do == "-":
        print(calc.minus(number1=float(input("ввести 1 значение: ")), number2=float(input("ввести 2 значение: "))))

    elif do == "/":
        print(calc.div(number1=float(input("ввести 1 значение: ")), number2=float(input("ввести 2 значение: "))))

    elif do == "*":
        print(calc.multi(number1=float(input("ввести 1 значение: ")), number2=float(input("ввести 2 значение: "))))

    elif do == "^":
        print(calc.pow(number1=float(input("ввести 1 значение: ")), number2=float(input("ввести 2 значение: "))))

    elif do == "module":
        print(calc.module(number1=float(input("ввести значение: "))))

    elif do == "0":
        print(calc.rand(number1=float(input("ввести верхнее значение: ")), number2=float(input("ввести нижнее значение: "))))

    elif do == "//":
        print(calc.whole_div(number1=float(input("ввести 1 значение: ")), number2=float(input("ввести 2 значение: "))))

    elif do == "%":
        print(calc.mod(number1=float(input("ввести 1 значение: ")), number2=float(input("ввести 2 значение: "))))

    elif do == "f":
        print(calc.factorial(number1=int(input("ввести  значение: "))))

    elif do == "acos":
        print(math.acos(calc.arccos(number1=float(input("ввести  значение: ")))))

    do = input("Введите оператор или введите exit, что бы закончить: ")