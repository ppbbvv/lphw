# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

#students = [
#    {'first_name': 'Вася'},
#    {'first_name': 'Петя'},
#    {'first_name': 'Маша'},
#    {'first_name': 'Маша'},
#    {'first_name': 'Петя'},
#]
# ???
#names = [student['first_name'] for student in students]
#unique_names = set(names)
#for name in unique_names:
#    print (f"{name}: {names.count(name)}")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
#names = [student['first_name'] for student in students]
#unique_names = set(names)
#d = {}
#for name in unique_names:
#    d[name] = names.count(name)
#max_count = max(d, key=d.get)
#print(f"(The most common name is {max(d, key=d.get)}")


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???
#for count,grade in enumerate(school_students, start = 1):
#    #count = count+1 ### fuck it
#    names = [name['first_name'] for name in grade]
#    unique_names = set(names)
#    d = {}
#    for name in unique_names:
#        d[name] = names.count(name)
#    print(f"(The most common name in {count} grade is {max(d, key=d.get)}")

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

#school = [
#    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
#    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
#    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
#]
#is_male = {
#    'Олег': True,
#    'Маша': False,
#    'Оля': False,
#    'Миша': True,
#    'Даша': False,
#}
# ???
#for grade in school:
#    people = grade['students']
#    class_name = grade['class']
#    names = [name['first_name'] for name in people]
#    male = 0
#    female = 0
#    for hooman in names:
#        if is_male[hooman] == True:
#            male = male + 1
#        elif is_male[hooman] == False:
#            female = female + 1
#    print(f"{class_name} grade contains {male} males and {female} females")            
    


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '4d', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
# я добавил ещё один dict выше, чтобы проверить не сломается ли на любом количестве данных
d = {}
l = []
males = {}
females = {}
for grade in school:
    people = grade['students']
    class_name = grade['class']
    names = [name['first_name'] for name in people]
    male = 0
    female = 0
    for hooman in names:
        if is_male[hooman] == True:
            male = male + 1
        elif is_male[hooman] == False:
            female = female + 1
        males.update({class_name: male})
        females.update({class_name: female})
print(f"The most number of males in class {max(males, key=males.get)} it is {max(males.values())} ")
print(f"The most number of females in class {max(females, key=females.get)} it is {max(females.values())} ")
#тут можно было перезаписывать переменные типа max_count, но я передумал так делать, это показалось мне плохой идеей

#males {2a:0, 3c:2}
#females {2a:2, 3c: 0}