#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
#  Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#  Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.


S = int(input('Введите сумму чисел X и Y: '))
P = int(input('Теперь ведите произведение чисел: '))
diskr = S**2 - 4*(-1)*(-1)*P
if diskr == 0:
    print(f'Два одинаковых числа: {(-1)*S/(2*(-1))}')
elif diskr > 0:
    print(f'Загаданы числа {((-1)*S + diskr**0.5)/(2*(-1))} и {((-1)*S - diskr**0.5)/(2*(-1))}')
else: print ('Неверно')