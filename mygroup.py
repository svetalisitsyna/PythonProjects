groupmates = [
    {
        "name": "Радмила",
        "surname": "Кунафина",
        "exams": ["Иностранный язык", "Философия", "РБ"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Анна",
        "surname": "Храпова",
        "exams": ["СОС", "Нечеткая логика", "Философия"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Валерий",
        "surname": "Шелюхин",
        "exams": ["Философия", "РБ", "ИБД"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Альбина",
        "surname": "Мяличева",
        "exams": ["Программирование", "ИБД", "Иностранный язык"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Алмаз",
        "surname": "Мадиев",
        "exams": ["Нечеткая логика", "СОС", "Программирование"],
        "marks": [3, 4, 3]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

def filter_students_by_average_mark(students, threshold):
    filtered_students = []
    for student in students:
        average_mark = sum(student["marks"]) / len(student["marks"])
        if average_mark > threshold:
            filtered_students.append(student)
    return filtered_students

if __name__ == "__main__":
    try:
        threshold = float(input("Введите средний балл для фильтрации: "))
        filtered_students = filter_students_by_average_mark(groupmates, threshold)
        print("Студенты со средним баллом выше", threshold, ":")
        print_students(filtered_students)
    except ValueError:
        print("Пожалуйста, введите корректное число.")        