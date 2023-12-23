"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузкE.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

from pprint import pprint
from more_itertools import flatten

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]


taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]


#1
#for dep in departments:
#    print(dep["title"])


#2
#depslist = [dep_list["employers"] for dep_list in departments]
#emplist = list(flatten(depslist))
#namelist = [name["first_name"] for name in emplist]
#print(f"{set(namelist)}")


#3

#for dep in departments:
#    oo = dep["title"]
#    for emplist in dep["employers"]:
#        print(f"{emplist['first_name']} in {oo}")

#4
#for dep in departments:
#    for emplist in dep['employers']:
#        if emplist['salary_rub'] > 100000:
#            print(emplist['first_name'])


#5
#for dep in departments:
#    for emplist in dep['employers']:
#        if emplist['salary_rub'] < 80000:
#            print(emplist['position'])


#6
#for dep in departments:
#    oo = dep['title']
#    ll = []
#    for emplist in dep['employers']:
#        ll.append(emplist['salary_rub'])
#    print(f"{oo} - {sum(ll)}")

#7
#for dep in departments:
#    oo = dep['title']
#    ll = []
#    for emplist in dep['employers']:
#        ll.append(emplist['salary_rub'])
#    print(f"{oo} - {min(ll)}")
 
#8
#for dep in departments:
#    oo = dep['title']
#    ll = []
#    for emplist in dep['employers']:
#        ll.append(emplist['salary_rub'])
#    print(f"{oo} - min:{min(ll)} max:{max(ll)} avg:{sum(ll)/len(ll)}")
# 
# 9
#depslist = [dep_list['employers'] for dep_list in departments]
#emplist = list(flatten(depslist))
#sallist = [sal['salary_rub'] for sal in emplist]
#print(f"Company AVG: {sum(sallist)/len(sallist)})")

#10
#ll = []
#for dep in departments:
#    for emplist in dep['employers']:
#        if emplist['salary_rub'] > 90000:
#            ll.append(emplist['position'])
#print(f"{set(ll)}")

#11
#for dep in departments:
#    oo = dep['title']
#    nn = ['Michelle', 'Christina', 'Caitlin', 'Nicole']
#    ll = []
#    for emplist in dep['employers']:
#        if emplist['first_name'] in nn:
#            ll.append(emplist['salary_rub'])
#    print(f"{oo} avg:{sum(ll)/len(ll)}")
# 
# 
# 12
#ll = []
#ao = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
#for dep in departments:
#    for emplist in dep['employers']:
#        if emplist['last_name'][-1] in ao:
#            ll.append(emplist['first_name'])
#print(set(ll))            


#13
#for dep in departments:
#    oo = dep['title']
#    ll = []
#    for tax in taxes:
#        if tax['department'] == None:
#            ll.append(tax['value_percents'])
#        if str(tax['department']).lower() == str(oo).lower():
#            ll.append(tax['value_percents'])             
#    print(f"{oo} - avg tax {sum(ll)/len(ll)} ") #не знаю как правильно считать средний налог, нет тз - результат хз


#14
#for dep in departments:
#    oo = dep['title']
#    for emplist in dep['employers']:
#        lle = []
#        for tax in taxes:
#            if tax['department'] == None:
#                lle.append(tax['value_percents'])
#            if str(tax['department']).lower() == str(oo).lower():
#                lle.append(tax['value_percents'])
#        tax_rate = 100 - sum(lle)    
#        print(f"{emplist['first_name']} {emplist['last_name']} | tax rate {tax_rate} | Salary net: {emplist['salary_rub']/100*tax_rate} | Salary gross: {emplist['salary_rub']} ")

#15
#dt = {}
#for dep in departments:
#    oo = dep['title']
#    ll = []
#    for tax in taxes:
#        if tax['department'] == None:
#            ll.append(tax['value_percents'])
#        if str(tax['department']).lower() == str(oo).lower():
#            ll.append(tax['value_percents'])             
#    deptaxtrate = sum(ll)
#    dt[oo] = deptaxtrate
#    sorted_taxrate = {key: val for key, val in sorted(dt.items(), key = lambda ele: ele[1])}
#print(sorted_taxrate)
# 
# 16
#for dep in departments:
#    oo = dep['title']
#    for emplist in dep['employers']:
#        lle = []
#        for tax in taxes:
#            if tax['department'] == None:
#                lle.append(tax['value_percents'])
#            if str(tax['department']).lower() == str(oo).lower():
#                lle.append(tax['value_percents'])
#        annual_tax_amount = emplist['salary_rub']/100*sum(lle)*12
#        if annual_tax_amount > 100000:
#            print(f"{emplist['first_name']} {emplist['last_name']} {annual_tax_amount}")          
#
# 
# 
# 
# 
#  17
fld = []
for dep in departments:
    oo = dep['title']
    for emplist in dep['employers']:
        lle = []
        employee = {}
        for tax in taxes:
            if tax['department'] == None:
                lle.append(tax['value_percents'])
            if str(tax['department']).lower() == str(oo).lower():
                lle.append(tax['value_percents'])
        annual_tax_amount = emplist['salary_rub']/100*sum(lle)*12
        employee['annual_tax'] = annual_tax_amount
        employee['First_name'] = emplist['first_name']
        employee['Last_name'] = emplist['last_name']
        employee['Department'] = oo
        fld.append(employee)
pprint(fld)



