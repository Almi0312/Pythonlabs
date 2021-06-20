#Переделываем задачу номер 3(калькулятор) на функции.
import math
import random

def plus(number1, number2):
    return number1 + number2

def minus(number1, number2):
    return number1 - number2

def div(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        print("на 0 делить нельзя")

def multi(number1, number2):
    return number1 * number2

def pow(number1, number2):
    return math.pow(number1, number2)

def module(number1):
    return abs(number1)

def rand(number1, number2):
    return random.uniform(number1, number2)

def whole_div(number1, number2):
    if number2 != 0:
        return number1 // number2
    else:
        print("на 0 делить нельзя")

def mod(number1,number2):
    return (number1 % number2)

def factorial(number1):
    return math.factorial(number1)

def arccos(number1):
    return number1*math.pi/180

do = input("ввести арифметический оператор: ")
while do != "exit":
    if do == "+":
        print(plus(number1 = float(input("ввести 1 значение: ")),number2 = float(input("ввести 2 значение: "))))

    elif do == "-":
        print(minus(number1=float(input("ввести 1 значение: ")), number2=float(input("ввести 2 значение: "))))

    elif do == "/":
        print(div(number1=float(input("ввести 1 значение: ")), number2=float(input("ввести 2 значение: "))))

    elif do == "*":
        print(multi(number1=float(input("ввести 1 значение: ")), number2=float(input("ввести 2 значение: "))))

    elif do == "^":
        print(pow(number1=float(input("ввести 1 значение: ")), number2=float(input("ввести 2 значение: "))))

    elif do == "module":
        print(module(number1=float(input("ввести значение: "))))

    elif do == "0":
        print(rand(number1=float(input("ввести верхнее значение: ")), number2=float(input("ввести нижнее значение: "))))

    elif do == "//":
        print(whole_div(number1=float(input("ввести 1 значение: ")), number2=float(input("ввести 2 значение: "))))

    elif do == "%":
        print(mod(number1=float(input("ввести 1 значение: ")), number2=float(input("ввести 2 значение: "))))

    elif do == "f":
        print(factorial(number1=int(input("ввести  значение: "))))

    elif do == "acos":
        print(math.acos(arccos(number1=float(input("ввести  значение: ")))))

    do = input("Введите оператор: ")
