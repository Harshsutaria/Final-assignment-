from Course import Course
from Student import Student
from DILevel import Level_3_Students
import os


class School(Course,Level_3_Students ,Student):
    def __init__(self):
        self.file1_data = []
        self.file2_data = []
        self.file3_data = []

    ''' Section 1: PASS Level
        Read from a file specified in command line, 
        create a list of Student
        objects and a list of Course objects. '''

    def read_level_1_file(self, file):
        self.score_data = self.read(file)
        self.generate_table(self.score_data)
        avg_of_top_result = self.calculate_average(self.score_data)
        print(avg_of_top_result)

    # To calculate average score of the student with the top score
    def calculate_average(self, score_data):
        formatted_array = self.reformat_data(self.score_data)
        # print(formatted_array)

        data_to_calculate_avg = [[j for j in i if type(j) != str] for i in formatted_array]

        avg = [sum(i) // len(i) if (len(i) != 0) else " " for i in data_to_calculate_avg]

        record = {}
        for i in range(len(formatted_array)):
            if (type(avg[i] == int)):
                record[formatted_array[i][0]] = avg[i]
            else:
                record[formatted_array[i][0]] = 0

        p = sorted(record.items(), key=lambda x: x[1])
        output = "{} students, {} courses the top student is {}, average is {}".format(len(p),
                                                                                       len(formatted_array[0]) - 1,
                                                                                       p[-1][0], p[-1][1])

        return output

    # To generate a table for Pass Level
    def generate_table(self, score_data):
        d = self.score_data[0][0]
        d = d.split()
        d[0] = " "
        d = [[i for i in d]]
        table = self.reformat_data(self.score_data)
        table = d + table
        # print(table)

        for i in table[:1]:
            print("{:<8} | {:<10} | {:<10} | {:<10} | {:<10}".format(i[0], i[1], i[2], i[3], i[4]))
        print("{:<8} | {:<10} | {:<10} | {:<10} | {:<10}".format('________', '__________', '__________', '__________',
                                                                 '__________'))

        for i in table[1:]:
            print("{:<8} | {:<10} | {:<10} | {:<10} | {:<10}".format(i[0], i[1], i[2], i[3], i[4]))

        print("{:<8} | {:<10} | {:<10} | {:<10} | {:<10}".format('________', '__________', '__________', '__________',
                                                                 '__________'))

    # To reforamt the data in the rows
    def reformat_data(self, score_data):
        formatted_array = []
        # print(score_data)
        for i in score_data[1:]:
            x = []
            for j in i:
                x.append(j.split()[0])
                for k in j.split()[1:]:
                    if k.isnumeric() and (0 <= int(k) <= 100):
                        x.append(int(k))
                    elif (int(k) == 888):
                        x.append("--")
                    else:
                        x.append(" ")
                formatted_array.append(x)
        # print(formatted_array)
        return formatted_array

    # Level-2 Implementation
    # To read scores from scores.txt and course.txt

    ''' Section 2: CREDIT Level
        At this level,  program can support two types of courses. One is Compulsory Course.
        Compulsory courses may have different credit points. Another type is Elective Course. 
        All elective courses have the same credit point.'''

    def read_level_2_files(self, file1, file2):
        self.file1_data = self.reformat_data(self.read(file1))
        self.file2_data = (self.read(file2))
        self.create_course_object()

    # To create courses object
    def create_course_object(self):
        self.formatted_course_object = []

        for i in self.file2_data:
            c = ",".join(i)
            self.formatted_course_object.append(c)
        # print(self.formatted_course_object)
        marks_of_course = self.calculate_average_of_courses(self.file1_data)
        for i in range(len(self.formatted_course_object)):
            self.formatted_course_object[i] += " " + str(len(marks_of_course[i]))
            self.formatted_course_object[i] += " " + str(sum(marks_of_course[i]) // len(marks_of_course[i]))
        # print(self.formatted_course_object)
        for i in range(len(self.formatted_course_object)):
            self.formatted_course_object[i] = self.formatted_course_object[i].split()
        # print(self.formatted_course_object)

        self.list_course_object = self.create_list_course_object()
        self.list_course_object[0].get_course_summary(self.list_course_object)

    # To create list of course objects
    def create_list_course_object(self):
        total_course = []
        for i in range(len(self.formatted_course_object)):
            id = self.formatted_course_object[i][0]
            name = self.formatted_course_object[i][1]
            type = self.formatted_course_object[i][2]
            credit = self.formatted_course_object[i][3]
            enroll = self.formatted_course_object[i][4]
            average = self.formatted_course_object[i][5]
            d = Course(id, name, type, credit, enroll, average)
            total_course.append(d)
        return total_course

    # Calculate marks for each course
    def calculate_average_of_courses(self, score_file):
        course_marks = []
        for i in range(1, len(score_file[0])):
            x = [j[i] for j in score_file if j[i] != " "]
            course_marks.append(x)
        # print(course_marks)
        return course_marks

    # Level-3 Implementation
    # Read data from scores.txt, courses.txt, student.txt
    ''' Section 3: DI Level --- 
        At this level,  program can support two types of Students, full time students (FT) and part time
        students (PT). A full time student is required to enrol in at least 3 compulsory courses. A part time
        student is required to enrol in at least 2 compulsory courses.'''

    def read_level_3_files(self, file1, file2, file3):
        self.file1_data = self.reformat_data(self.read(file1))
        self.file2_data = (self.read(file2))
        self.file3_data = (self.read(file3))

        self.create_student_object()

    # Create student object
    def create_student_object(self):
        c = []
        for i in range(len(self.file3_data)):
            c = ",".join(self.file3_data[i])
            c = c.split(" ")
            self.file3_data[i] = c

        self.list_students_object = self.create_list_student_object()

        self.list_students_object[0].get_student_report_table(self.list_students_object)

    # Create list of student objects
    def create_list_student_object(self):
        final = self.create_student_data()
        total_student = []
        for i in range(len(final)):
            id = final[i][0]
            name = final[i][1]
            student_type = final[i][2]
            enrolled = final[i][3]
            main_enrolled = final[i][4]
            gpa = final[i][5]
            d = Level_3_Students(id, name, student_type, enrolled, main_enrolled, gpa)
            total_student.append(d)
        return total_student

    # Fetch details of the student like sid, name, marks
    def create_student_data(self):
        self.res = []
        for i in self.file1_data:
            d = i[1:]
            self.res.append(d)
        print(self.res)
        res = self.calculate_gpa(self.res)

        number_of_courses = res[0]
        gpa_of_student = res[1]
        number_of_compulsory_course = res[2]
        for i in range(len(self.file1_data)):
            self.file3_data[i].append(number_of_courses[i])
            self.file3_data[i].append(number_of_compulsory_course[i])
            self.file3_data[i].append(gpa_of_student[i])
        print(self.file3_data)
        return self.file3_data

    # This method willl return list of GPA , Total courses Enrolled  , compulsory course enrolled by students
    def calculate_gpa(self, c):
        gpa = []
        main_enrolled_list = [[j for j in i[:-1] if type(j) != str] for i in c]
        main_enrolled = [len(i) for i in main_enrolled_list]
        c = [[j for j in i if type(j) != str] for i in c]
        # print(c)
        enrolled = [len(i) for i in c]
        # print(enrolled)
        for i in c:
            x = 0
            for j in i:
                x += self.get_gpa(j)

            final = round(x / len(i), 2)
            gpa.append(final)
        print(gpa)
        return [enrolled, gpa, main_enrolled]

    # Level 4 implementation starts from here
    '''Section 4: HD Level 
        At this level, your program can handle some variations in the files.'''

    def read_level_4_files(self, file1, file2, file3):
        self.file1_data = self.read(file1)
        self.file2_data = self.read(file2)
        self.file3_data = self.read(file3)

        a = self.format_array(self.file1_data)
        self.b = self.format_array(self.file2_data)
        c = self.format_array(self.file3_data)
        list = self.sort_file(a, c)
        self.a = list[0]
        self.c = list[1]
        res = self.credit_point()
        self.individual_credit = res[0]
        self.individual_GPA = res[1]
        self.compulsion_enrolled = res[2]
        self.crpt = res[3]
        # print(self.individual_credit)
        # print(self.individual_GPA)
        # print(self.compulsion_enrolled)
        # print(self.c)
        self.level4_object = self.create_final_report_object()
        self.level4_object[0].get_student_report_table(self.level4_object)

    # creating  final report object
    def create_final_report_object(self):
        self.c = self.create_final_report_list()
        list_of_di_object = []
        for i in range(len(self.c)):
            id = self.c[i][0]
            name = self.c[i][1]
            student_type = self.c[i][2]
            credits = self.c[i][6]
            compulsion_enrolled = self.c[i][4]
            gpa = self.c[i][5]
            d = Student(id, name, student_type, credits, compulsion_enrolled, gpa)
            list_of_di_object.append(d)
        return list_of_di_object

    # Creating  list in - order to create final list of object
    def create_final_report_list(self):
        for i in range(len(self.c)):
            self.c[i].append(self.individual_credit[i])
            self.c[i].append(self.compulsion_enrolled[i])
            self.c[i].append(self.individual_GPA[i])
            self.c[i].append(self.crpt[i])
        self.c.sort(reverse=True, key=lambda x: x[6])

        return self.c

    # This  method will return list consisting of student  credit, gpa, compulsory course
    def credit_point(self):
        course_credit = [int(j[3]) for j in self.b]
        res = self.formatting_final_report_data(self.a)
        marks_of_student = res[0]
        compulsion_enrolled = res[1]
        individual_credit = []
        gpa = []
        Crpt = []
        for i in marks_of_student:

            credit = 0
            d = 0
            crpt = 0

            for j in range(len(i)):
                if type(i[j]) != str:
                    d += i[j] * course_credit[j]
                    credit += course_credit[j]
                    if (i[j] > 0):
                        crpt += course_credit[j]

            Crpt.append(crpt)
            d = round((d / credit), 2)
            individual_credit.append(credit)
            gpa.append(d)
        return [individual_credit, gpa, compulsion_enrolled, Crpt]

    # This method will validate the score of student
    def formatting_final_report_data(self, a):

        final_score = []

        for i in a[1:]:
            d = []
            for j in i[1:]:
                if j == "TBA":
                    d.append("-")
                elif j.isalpha():
                    d.append(" ")
                elif str(int(float(j))).isnumeric():
                    c = self.get_gpa(int(float(j)))
                    d.append(c)
            final_score.append(d)

        course_enrolled = [[j for j in i[:-1] if type(j) != str] for i in final_score]
        compulsion_enrolled = [len(i) for i in course_enrolled]
        return [final_score, compulsion_enrolled]

    # This method will get the gpa according to marks of the stdent
    def get_gpa(self, a):
        if a >= 80:
            return 4
        elif 70 <= a <= 79:
            return 3
        elif 60 <= a <= 69:
            return 2
        elif 50 <= a <= 59:
            return 1
        else:
            return 0

    # Format array
    @staticmethod
    def format_array(file):
        c = []
        for i in range(len(file)):
            c = ",".join(file[i])
            c = c.split(" ")
            file[i] = c
        return file

    # sort file
    @staticmethod
    def sort_file(a, c):
        a.sort()
        c.sort()
        return [a, c]

    # To read data from file and generate a nested list of the rows
    @staticmethod
    def read(file):

        list_of_rows_from_file = []
        if os.stat(file).st_size == 0:
            # print("File Contents is empty")
            exit("File Contents is empty")
        with open(file, "r") as content:
            for line in content:
                rows = []
                i = line.strip()
                rows.append(i)
                # print(i , rows)
                list_of_rows_from_file.append(rows)
        return list_of_rows_from_file
