from datetime import datetime
import os


class Student:
    def __init__(self, sid, name, student_type, credit, compulsory_courses_enrolled, gpa):
        self.id = sid
        self.name = name
        self.student_type = student_type
        self.credit = credit
        self.compulsory_courses_enrolled = compulsory_courses_enrolled
        self.gpa = gpa

    # method to generate a table
    def get_student_report_table(self, student_object):
        print("{:<8}  {:<15}  {:<10}  {:<3} {:<5} {:<10}".format("SID", "Name", "Mode", "CrPt", " ", "GPA"))
        print("{:<8}{:<15}{:<10}{:<10}{:<3}{:<15}".format('________', '_______________', '__________', '__________',
                                                          '___', '__________'))

        for i in student_object:
            if i.student_type == "FT" and i.compulsory_courses_enrolled >= 3 and i.credit >= 50:
                x = ""
            elif i.student_type == "PT" and i.compulsory_courses_enrolled >= 2 and i.credit >= 30:
                x = ""
            else:
                x = "!"
            print("{:<8}  {:<15}  {:<10}  {:<3}{:<7}{:<10}".format(i.id, i.name, i.student_type, i.credit, x, i.gpa))

        self.save_student_report_table(student_object)

    # method to sake a method in a file including with the date
    @staticmethod
    def save_student_report_table(student_object):
        with open("student_report.txt", "r") as f:
            with open("newFile.txt", "w") as f2:

                now = datetime.now()
                current_time = now.strftime("%d/%m/%Y %H:%M")
                f2.write("\n")
                f2.write(current_time)
                f2.write("\n")
                f2.write("{:<8}  {:<15}  {:<10}  {:<10} {:<3} {:<10}".format("SID", "Name", "Mode", "CrPt", " ", "GPA"))
                f2.write("\n")
                f2.write("{:<8}{:<15}{:<10}{:<10}{:<3}{:<15}".format('________', '_______________', '__________', '__________',
                                                                     '___', '__________'))
                f2.write("\n")
                for i in student_object:
                    if i.student_type == "FT" and i.compulsory_courses_enrolled >= 3 and i.credit >= 50:
                        x = ""
                    elif i.student_type == "PT" and i.compulsory_courses_enrolled >= 2 and i.credit >= 30:
                        x = ""
                    else:
                        x = "!"
                    f2.writelines("{:<8}  {:<15}  {:<10}  {:<3}{:<7}{:<10}".format(i.id, i.name, i.student_type, i.credit, x, i.gpa))

                    f2.writelines("\n")
                f2.write(f.read())
        os.remove("student_report.txt")
        os.rename("newFile.txt", "student_report.txt")
        print("student_report.txt generated!")
