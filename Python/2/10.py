#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
#  Выведите минимальное количество монет, которые нужно перевернуть.

coins = list(input(
    'Введите стороны лежащих монет (решкой - 1, гербом - 0): ').replace(' ', ''))
if coins.count('0') > coins.count('1'):
    print(f"Необходимо перевернуть {coins.count('1')} монет(-ы/- у)")
else:
    print(f"Необходимо перевернуть {coins.count('0')} монет(-ы/-у)")
    