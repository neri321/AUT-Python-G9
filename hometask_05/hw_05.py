"""Домашнє завдання №4: Робота з виключеннями (exceptions)

1. Створити функцію, що приймає число з консолі (використати функцію input());
    Функція повинна обробити значення таким чином: використовуючи вбудовану функцію int(),
    спробувати конвертувати рядок в число (input() завжди повертає рядок).
    Якщо конвертувати не виходить, то вивести в консоль "Entered not valid data"."""


def check_input():
    data = input('Enter data here:')
    try:
        print(int(data))
    except ValueError:
        print("Entered not valid data")


check_input()

"""2. Створити функцію, що приймає 2 рядки;
    Якщо хоча б один рядок не виходить конвертувати в число, тоді робимо конкатенацію (з'єднуємо рядки),
    якщо ж обидва значення можна конвертувати в числа, то отримуємо їх суму.
    Результат друкуємо в консоль."""


def funk_2():
    a = input('Enter the first value: ')
    b = input('Enter the second value: ')
    try:
        x = int(a)
        y = int(b)
        result = x + y
    except ValueError:
        result = a + b
        print(result)


funk_2()

"""3. Створити функцію, що приймає значення з консолі. Якщо значення не можна привести до числа,
    тоді просимо користувача ввести інше значення, доки він не введе число. Згадуємо про цикл while.
   Коли користувач вводить число, дякуємо йому!"""


def check_digit():
    while True:
        a = input('Enter value here: ')
        try:
            int(a)
        except ValueError:
            print('Enter another value: ')
        else:
            print(f"Thank you, you enter number {a}")
            return a


check_digit()


"""4. Створити ВЛАСНЕ виключення. Наприклад OnlyEvenError. Створити функцію check_digit(), яка приймає число.
    Якщо число не парне, то породжувати це своє виключення;
    Якщо парне, то повертати його (return)"""


class OnlyEvenError(Exception):
    pass


def check_digit(num):
    if num % 2 != 0:
        raise OnlyEvenError
    else:
        return num


print(check_digit(3))

"""5. Створити функцію, що буде приймати число як аргумент і викликАти в тілі функцію check_digit,
    в яку передавати це число.
   Якщо виникає помилка, то перехопити її, та збільшити вхідне число на 1;
   Якщо помилки не вникає, то помножити число на 2.
    Результат виводити в консоль.
    Також функція повинна надрукувати в консоль фразу "Я все одно завжди щось друкую".
   !!! Використовувати try-except-else-finally"""


def func_3(num):
    try:
        check_digit(num)
    except OnlyEvenError:
        return num + 1
    else:
        return num * 2
    finally:
        print('Я все одно завжди щось друкую')


print(func_3(4))
