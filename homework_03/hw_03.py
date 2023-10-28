"""Домашнє завдання №3: Робота з рядками (strings)
Preconditions:
Є рядок "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення."""

doc = 'Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення.'

# 1. Вивести в консоль довжину рядка (кількість символів)
print(len(doc))

# 2. Вивести в консоль довжину рядка (кількість слів)
print(len(doc.split(' ')))

# the first try
# doc = doc.replace('а', '#')
# doc = doc.replace('о', '#')
# doc = doc.replace('и', '#')
# doc = doc.replace('і', '#')
# doc = doc.replace('у', '#')
# doc = doc.replace('є', '#')
# doc = doc.replace('е', '#')
# doc = doc.replace('я', '#')
# doc = doc.replace('ю', '#')
# doc = doc.replace('ї', '#')


# print(doc.split())
# print(' '.join(doc.split()))

# the second try
# def remove_vowels(sentences: str):
#     vowels_letter = 'аАоОиИіІуУєЄеЕяЯюЮїЇ'
#     result = ""
#     for letter in sentences:
#         if letter not in vowels_letter:
#             result += letter
#         else:
#             result += '#'
#     return result.split()
#
#
# print(remove_vowels(doc))
# print(' '.join(remove_vowels(doc)))

# finally
"""3. Розбити рядок на список окремих слів та замінити в кожному слові усі голосні літери
    іншим символом, наприклад '#'."""


def replace_vowels(text: str):
    vowels_letter = 'аАоОиИіІуУєЄеЕяЯюЮїЇ'
    for letter in text:
        if letter in vowels_letter:
            text = text.replace(letter, '#')
    return text.split()


print(replace_vowels(doc))
# 4. Відновити рядок зі списку, зі вже заміненими словами.
print(' '.join(replace_vowels(doc)))
