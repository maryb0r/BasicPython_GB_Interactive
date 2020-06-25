#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться
после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

def main():

    original_list = [16, 10, 5, 4, 0]

    while True:
        new_value = input('Введите новый элемент рейтинга, чтобы прекратить введите NO: ')

        if new_value.upper() == 'NO':
            break

        original_list.append(int(new_value))
        original_list.sort(reverse=True)

    print('Результат: {}'.format(', '.join(str(x) for x in original_list)))


if __name__ == '__main__':
        main()
