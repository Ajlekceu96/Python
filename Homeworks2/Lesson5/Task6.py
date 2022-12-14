"""

6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести его на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

"""

lst = [
    "Информатика: 100 50 20",
    "Физика: 30 40 10",
    "Физкультура: 10 30 10",
]
with open("task6.txt", "w", encoding="utf-8") as my_f:
    for i in lst:
        my_f.write(i + "\n")

subj = {}
with open("task6.txt", "r", encoding="utf-8") as my_f:
    for line in my_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f"Общее количество часов по предмету - \n {subj}")
