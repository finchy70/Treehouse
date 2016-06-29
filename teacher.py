teachers = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
            'Kenneth Love': ['Python Basics', 'Python Collections']}

def most_classes(teachers):
    max_lessons = 0
    max_teacher = ""
    for item in teachers:
        print(item)
        print(len(teachers[item]))
        if len(teachers[item]) > max_lessons:
            max_lessons = len(teachers[item])
            max_teacher = item

    return max_teacher

def num_teachers(teachers):
    return len(teachers)

def stats(teachers):
    list_of_teachers = []

    for item in teachers:
        print("The item is {}.".format(item))
        print("The number of lessons is {}.".format(len(teachers[item])))
        sub_list =list([item])
        sub_list.append(len(teachers[item]))
        print(sub_list)
        list_of_teachers.append(sub_list)
    return list_of_teachers


def courses(teachers):
    list_of_courses = []
    for item in teachers:
        courses_list = teachers[item]
        for f in courses_list:
            if f not in list_of_courses:
                list_of_courses.append(f)

    return list_of_courses




print(most_classes(teachers))
print(num_teachers(teachers))
print(stats(teachers))
print(courses(teachers))