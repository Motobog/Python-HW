# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
# больше суммы двух других, то треугольника с такими сторонами не существует.Отдельно
# сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = 3
b = 2
c = 4

if a >= (b + c) or b >= (a + c) or c >= (a + b):
    res = 'Такого треугольника не существует'
elif a == c == b:
    res = 'Треугольник равносторонний'
elif a == b or a == c or b == c:
    res = 'Треугольник равнобедренный'
else:
    res = 'треугольник разносторонний'
print(res)

# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на
# единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

LOWER_LIMIT = 1
UPPER_LIMIT = 100000
res = 0

while True:
    num_str = input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT} - ')
    
    if num_str.isnumeric():
        num = int(num_str)
        
        if num < LOWER_LIMIT or num > UPPER_LIMIT:
            print('число находится за допустимым диапазоном')
            continue
        else:
            for i in range(2, num + 1):
                if num % i == 0:
                    res +=1
            if res == 1 or num == 1:
                print('Число простое')
            else:
                print('Число составное')
            break

    else:
        print('это либо отрицательное число, либо не число')

# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна
# подсказывать “больше” или “меньше” после каждой попытки.

from random import randint

LOWER_LIMIT = 1
UPPER_LIMIT = 1000
cnt = 10

res = randint(LOWER_LIMIT, UPPER_LIMIT)

while cnt>=0:
    if cnt == 0:
        print('У вас 0 попыток. Не угадали')
        break

    num_str = input(f'У вас {cnt} попыток. Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT} - ')
    
    if num_str.isnumeric():
        num = int(num_str)
        
        if num < LOWER_LIMIT or num > UPPER_LIMIT:
            print('число находится за допустимым диапазоном')
            continue
        else:
            cnt -= 1
            if res == num:
                print('Ура. Угадал')
                break
            elif num < res:
                print('больше')
            else:
                print('меньше')

    else:
        print('это либо отрицательное число, либо не число')

print(f'Загаданное число - {res}')

# Программа загадывает число от 0 до 1000 и сама пытается угадать за 10 попыток.

from random import randint

LOWER_LIMIT = 1
UPPER_LIMIT = 1000
cnt = 10
num = int(UPPER_LIMIT / 2)
num_up = UPPER_LIMIT
num_low = LOWER_LIMIT
res = randint(LOWER_LIMIT, UPPER_LIMIT)

while cnt>=0:
    print(f'Попытка {11-cnt}. Число {num}')
    if cnt == 0:
        print('У вас 0 попыток. Не угадали')
        break
    else:
        if num == res:        
            print(f'Ура. Угадал с {11 - cnt} попытки')
            break
        elif num > res:
            num_up = num
        else:
            num_low = num
    num = int((num_low + num_up)/2)        
    cnt -= 1
print(f'Загаданное число - {res}')