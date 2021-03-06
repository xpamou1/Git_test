#coding: utf-8

import random


# Задание №1
# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть
# произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить
# (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".


def arithmetic(num_1, num_2, do):
    if do == '-':
        print(num_1 - num_2)
    elif do == '+':
        print(num_1 + num_2)
    elif do == '*':
        print(num_1 * num_2)
    elif do == '/':
        try:
            print(num_1 / num_2)
        except ZeroDivisionError:
            print('Наноль делить нельзя!')
    else:
        print('Неизвестная операция!')


num_1 = int(input('Число№1'))
num_2 = int(input('Число№2'))
do = input('Действие')
arithmetic(num_1, num_2, do)


# Задание№2 Високосный год (2)
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

def is_year_leap(year):
    ves = year % 100
    if (year % 4) == 0 and ves != 0:
        year_ves = True
    elif (year % 400) == 0:
        year_ves = True
    else:
        year_ves = False
    return year_ves


print(is_year_leap(int(input('Введите год: '))))


# Задание№3 Квадрат (3)
# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.

def square(side_square):
    cube = []
    cube.append(4 * side_square)
    cube.append(side_square ** 2)
    cube.append(side_square * (2 ** (1 / 2)))
    return cube


print(square(int(input('Введите сторону квадрата: '))))


# Задание№4 Времена года (4)
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому
#  этот месяц принадлежит (зима, весна, лето или осень).

def season(month):
    seasons = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', \
               10: 'Осень', 11: 'Осень', 12: 'Зима'}
    for key, value in seasons.items():
        if key == month:
            print(value)
        elif month > 12:
            print('error')


season(int(input('Введите месяц, для определения времени года: ')))

# Задание№5 Банковский вклад (5)
# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада
# увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.


money = int(input('Ведите количество денег: '))
year = int(input('Ведите на кокое количество лет: '))
days_in_year = 365
day_out = days_in_year * year
day_in = 1
year_pass = 1

while day_in < day_out:
    if day_in > days_in_year * year_pass:
        money = money * 1.1
        year_pass += 1
        wait_com = input('Спустя год вы получили: {}'.format(money))
    else:
        print('Ваша сумма равна {}'.format(money))
        break


def bank(money, year):
    n = 0
    while year != n:
        money = money * 1.1
        n += 1
    print('Ваша сумма составит: {}'.format(money))


bank(money, year)


# Задание№6 Простые числа (6)
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое,
# и False - иначе.


def is_prime(number):
    number_easy = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, \
                   101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, \
                   199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, \
                   317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, \
                   443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, \
                   577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, \
                   701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, \
                   839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, \
                   983, 991, 997]
    for i in number_easy:
        if number == i:
            a = True
            break
        else:
            a = False
    return a


print(is_prime(random.randint(0, 1000)))

# задание№7 Правильная дата (7)
# Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в
# нашем календаре, и False иначе.

from datetime import date


def date_1(day, month, year):
    try:
        (date(int(year), int(month), int(day)))
        return True
    except ValueError:
        return False


currentdate = input('Введите любую дату для проверки в формате: dd.mm.yyyy: ')
day, month, year = currentdate.split('.')
print(date_1(day, month, year))


# Задание№8 XOR-шифрование (8)
# Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая
#  возвращает строку,
# зашифрованную путем применения функции XOR (^) над символами строки с ключом. Написать также функцию XOR_uncipher,
#  которая по зашифрованной строке и ключу восстанавливает исходную строку.


def xor_cipher(text, key):
    cipher_text = ''
    for i in text:
        try:
            cipher_text += chr(ord(i) ^ ord(key))
        except TypeError:
            cipher_text += chr(ord(i) ^ key)
    print(cipher_text)
    return cipher_text


def xor_uncipher(cipher_text, key):
    uncipher_text = ''
    for i in cipher_text :
        try:
            uncipher_text += chr(ord(i) ^ ord(key))
        except TypeError:
            uncipher_text += chr(ord(i) ^ key)
    print(uncipher_text)

cipher_text = xor_cipher('hello world', 10)
xor_uncipher(cipher_text, 10)
