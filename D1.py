n = int(input('Ведите трехзначное число:'))
a = n % 10
n = n // 10
b = n % 10
n = n // 10
print('Сумма цифр трехзачного числа, равна:', n + a + b)