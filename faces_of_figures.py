import math
figure = input()
if figure == 'square':
    a = float(input())
    face = a * a
    print(face)

elif figure == "rectangle":
    a = float(input())
    b = float(input())
    face = a * b
    print(face)

elif figure == "circle":
    r = float(input())
    face = math.pi *(r ** 2)
    print(face)
elif figure == "triangle":
    a = float(input())
    b = float(input())
    face = a * b / 2
    print(face)

