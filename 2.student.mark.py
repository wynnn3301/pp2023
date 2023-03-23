class Student:
    def __init__(self, id_stu, stu_name, stu_dob):
        self.id_stu = id_stu
        self.stu_name = stu_name
        self.stu_dob = stu_dob


class Course:
    def __init__(self, id_course, course_name):
        self.id_course = id_course
        self.course_name = course_name
        self.marks = {}

    def enter_marks(self, stu_list):
        for stu in stu_list:
            point = int(input(f'Nhap diem cua hoc sinh {stu.stu_name} vao {self.course_name}: '))
            self.marks[stu.id_stu] = point


class School:
    def __init__(self):
        self.stu_list = []
        self.course_list = []

    def input_students(self):
        num_stu = int(input('Nhap so hoc sinh: '))
        for i in range(num_stu):
            id_stu = input('Nhap id hs: ')
            stu_name = input('Nhap ten hs: ')
            stu_dob = input('Nhap dob hs: ')
            self.stu_list.append(Student(id_stu, stu_name, stu_dob))

    def input_courses(self):
        num_course = int(input('So khoa hoc: '))
        for i in range(num_course):
            id_course = input('ID cua khoa hoc: ')
            course_name = input('Ten khoa hoc: ')
            self.course_list.append(Course(id_course, course_name))

    def pick_course_and_enter_marks(self):
        pick_cs = input('nhap khoa hoc muon chon: ')
        for course in self.course_list:
            if pick_cs == course.id_course:
                course.enter_marks(self.stu_list)

    def print_students(self):
        print('Danh sach hoc sinh:')
        for stu in self.stu_list:
            print(f'{stu.id_stu} {stu.stu_name}')

    def print_courses(self):
        print('Danh sach khoa hoc:')
        for course in self.course_list:
            print(f'{course.id_course} {course.course_name}')

    def print_marks(self):
        enter_cs_id = input('Nhap id khoa hoc can xem diem: ')
        for course in self.course_list:
            if course.id_course == enter_cs_id:
                print(f'Diem trong khoa hoc {course.course_name} cua hoc sinh la: {course.marks}')


# Main code
school = School()
while True:
    print('''1. Nhap danh sach hoc sinh
2. Nhap danh sach khoa hoc
3. Chon khoa hoc va nhap diem
4. In danh sach hoc sinh
5. In danh sach khoa hoc
6. In diem cua hoc sinh
7. Thoat''')
    choice = int(input('Nhap lua chon: '))
    if choice == 1:
        school.input_students()
    elif choice == 2:
        school.input_courses()
    elif choice == 3:
        school.pick_course_and_enter_marks()
    elif choice == 4:
        school.print_students()
    elif choice == 5:
        school.print_courses()
    elif choice == 6:
        school.print_marks()
    elif choice == 7:
        break
    else:
        print('Nhap lai lua chon: ')

        
