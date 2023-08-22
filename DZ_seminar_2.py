# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
#
#5 -> 10110
#2

enter = int(input('Введите количество монет '))
heads = 0
tails = 0
for i in range(enter):
    face = int(input('Если монетка лежит вверх орлом, введите \"1\" если решкой, введите \"0\": '))
    if face == 1:
        heads += 1
    else:
        tails += 1
if heads > tails:
    print(f'Переверните {tails} монет с решки на орла')
elif heads == tails:
    print(f'Количество орлов и решек одинаково, переверните любые {heads} монет')
else:
    print((f'Переверните {heads} монет с орла на решку'))
    
    
    
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

S = int(input('Введите число полученное от суммы задуманных чисел: '))
P = int(input('Введите число полученное от произведения задуманных чисел: '))
for X in range(0, 1001):
    for Y in range(0, 1001):
        if (int(X) + int(Y) == S) and (int(X) * int(Y) == P):
            print(X, Y)


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

N = int(input('Введите число N: '))
stop = 0
step = 2
for i in range(N):
    if stop != 1:
        step = step ** i
        if step <= N:
            print(step, end = ' ')
            step = 2
        else:
            stop = 1
    else:
        i = N
