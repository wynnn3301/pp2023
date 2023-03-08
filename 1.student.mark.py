def input_stu(stu_list):   
    num_stu = int(input('Nhap so hoc sinh: '))
    for i in range(num_stu):
        small_list_stu = []
        id_stu = input('Nhap id hs: ')
        stu_name = input('Nhap ten hs: ')
        stu_dob = input('Nhap dob hs: ')
        small_list_stu.append(id_stu)
        small_list_stu.append(stu_name)
        small_list_stu.append(stu_dob)
        stu_list.append(small_list_stu)


def input_course (course):   
    num_course = int(input('So khoa hoc: '))
    for i in range(num_course): 
        small_list_course = []
        id_course = input('ID cua khoa hoc: ')
        course_name = input('Ten khoa hoc: ')
        small_list_course.append(id_course)
        small_list_course.append(course_name)
        course.append(small_list_course)
    

def pick_cs_and_enter_mark (course, stu_list):
    for i in range(len(course)):  
        pick_cs = input('nhap khoa hoc muon chon: ')
        for small_list_course in course:                
                if pick_cs == small_list_course[0]:
                    mark = []
                    for i in range(len(stu_list)):
                        point = int(input('Nhap diem cua hs vao ' + small_list_course[1] + ':'))
                        mark.append(point)
                    small_list_course.append(mark)


def print_stu (stu_list): 
    print ('danh sach hoc sinh: ')
    for small_list_stu in stu_list:
        for i in range(len(small_list_stu)):    
            print (small_list_stu[i] + ' ')


def print_cs(course): 
    print('danh sach khoa hoc: ')
    for small_list_course in course:
        for i in small_list_course:
            try: 
               print(i + ' ')
            except TypeError:
                pass

def print_point(course):
    enter_cs_id = input('Nhap id khoa hoc can xem diem: ')
    for small_list_course in course:
        if small_list_course[0] == enter_cs_id:
            print('diem trong khoa hoc ' + small_list_course[1] + ' cua hoc sinh la: ', small_list_course[2])
        


# Main code
stu_list = []
course = []
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
        input_stu(stu_list)
    elif choice == 2:
        input_course(course)
    elif choice == 3:
        pick_cs_and_enter_mark(course,stu_list)
    elif choice == 4:
        print_stu(stu_list)
    elif choice == 5:
        print_cs(course)
    elif choice == 6:
        print_point(course)
    elif choice == 7:
        break
    else:
        print('Nhap lai lua chon: ')