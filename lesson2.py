# Напишите программу,которая получает целое число и возвращает его шестнадцатиричное строковое представление.
# Функцию hex используйте для проверки своего результата

num=int(input('Введите число: '))
print(f'Шестнадцатиричное представление числа {num}:')
print(format(num,'x'))
print(f'Проверка: {hex(num)}')


# Напишите программу которая принимает две строки вида "a/b" - дробь с числитилем и знаменателем.Программа 
# должна возвращать сумму и *произведение дробей.Для проверки кода использовать модуль fractions.

import math
import fractions
str1=input('Введите первую дробь в формате "a/b": ')
str2=input('Введите вторую дробь в формате "a/b": ')


list1 = str1.split('/')
numerator1=int(list1[0])
denomerator1=int(list1[1])

list2=str2.split('/')
numerator2=int(list1[0])
denomerator2=int(list2[1])

sum_fractions_denomerator =  denomerator1 * denomerator2
sum_fractions_numerator=(numerator1*denomerator2) + (numerator2*denomerator1)

div=int(math.gcd(sum_fractions_numerator,sum_fractions_denomerator))

final_numerator=int(sum_fractions_numerator/div)
final_denomerator=int(sum_fractions_denomerator/div)

print(f'Сумма дробей {str1} и {str2} = {final_numerator}/{final_denomerator}')

mult_fractions_numerator=numerator1*numerator2
mult_div=int(math.gcd(mult_fractions_numerator,sum_fractions_denomerator))
mult_final_numerator=int(mult_fractions_numerator/mult_div)
mult_final_denomerator=int(sum_fractions_denomerator/mult_div)

print(f'Произведение дробей {str1} и {str2} = {mult_final_numerator}/{mult_final_denomerator}')

fraction1=(fractions.Fraction(numerator1,denomerator1))
fraction2=(fractions.Fraction(numerator2,denomerator2))
sum_fraction=fraction1+fraction2
mult_fraction=fraction1*fraction2
print(f'Проверка: {fraction1}+{fraction2}={sum_fraction }')
print(f'Проверка: {fraction1}*{fraction2}={mult_fraction }')