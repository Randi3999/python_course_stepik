"""
На числовой прямой даны два отрезка: [a1; b1] и [a2; b2]. Напишите программу, которая находит их пересечение.
Формат входных данных
На вход программе подаются четыре целых числа a1, b1, a2, b2, каждое на отдельной строке. Гарантируется, что a1 < b1 и a2 < b2.

Формат выходных данных
Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое множество» (без кавычек).
"""
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

# точка
if a1 == b2 and a2 != b1: print(a1)
elif a1 != b2 and a2 == b1: print(a2)

# отрезок
elif a1 == a2 and b1 == b2: print(a1, b1)
elif a1 == a2 and b1 < b2: print(a1, b1)
elif a1 == a2 and b1 > b2: print(a2, b2)
elif b1 == b2 and a1 > a2: print(a1, b1)
elif b1 == b2 and a1 < a2: print(a2, b2)
elif a1 < a2 and a1 < b2 and b1 < a2 and b1 < b2: print("пустое множество")
elif a2 < a1 and a2 < b1 and b2 < a1 and b2 < b1: print("пустое множество")
elif a1 < a2 and b1 < b2: print(a2, b1)
elif a2 < a1 and b2 < b1: print(a1, b2)
elif a1 < a2 and b1 > b2: print(a2, b2)
elif a2 < a1 and b2 > b1: print(a1, b1)
