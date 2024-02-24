'''
Марк, здравствуйте!

Спасибо, у вас отличная работа, задания выполнены полностью верно :)

Только в задаче со знаками зодиака более корректно было бы использовать if/elif/elif/..., чем просто множественные if ,
т.к. это все единая логическая конструкция, тем более мы не предполагаем вариант,
что у человека может быть одновременно 2 знака зодиака (нам достаточно одного срабатывания проверки).
И если интересно, то чуть забегая вперед и используя словари для задачи со знаками зодиака,
ее можно оптимизировать вот так:
'''

signs = {"март": (21, "Рыбы", "Овен"), "апрель": (21, "Овен", "Телец"), "май": (22, "Телец", "Близнецы"),
         "июнь": (22, "Близнецы", "Рак"), "июль": (23, "Рак", "Лев"), "август": (24, "Лев", "Дева"),
         "сентябрь": (24, "Дева", "Весы"), "октябрь": (24, "Весы", "Скорпион"),
         "ноябрь": (23, "Скорпион", "Стрелец"), "декабрь": (23, "Стрелец", "Козерог"),
         "январь": (21, "Козерог", "Водолей"), "февраль": (20, "Водолей", "Рыбы")}

if (day >= signs[month][0]):
    print(signs[month][2])
else:
    print(signs[month][1])