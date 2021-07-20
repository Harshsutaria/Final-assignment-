class Course:
    def __init__(self, sid, name, course_type, credit, students_enrolled, avg):
        self.id = sid
        self.name = name
        self.__course_type = course_type
        self.credit = credit
        self.enroll = students_enrolled
        self.avg = avg

    def get_course_summary(self, list_course_object):

        print("{:<8} {:<3}  {:<15}  {:<10}  {:<10}  {:<10}".format("CID", "   ", "Name", "Pt.", "Enl.", "Avg."))
        print("{:<8}{:<3}{:<15}{:<10}{:<10}{:<13}".format('________', '___', '_______________', '__________',
                                                          '__________', '_____________'))

        for i in list_course_object:
            if i.__course_type[0] == "C":
                x = "*"
            else:
                x = "-"
            print("{:<8} {:<3}  {:<15}  {:<10}  {:<10}  {:<10}".format(i.id, x, i.name, i.credit, i.enroll, i.avg))

        print("{:<8}{:<3}{:<15}{:<10}{:<10}{:<13}".format('________', '___', '_______________', '__________'
                                                          , '__________', '_____________'))

        self.save_course_summary(list_course_object)

    def save_course_summary(self, list_course_object):

        file1 = open("courses_report.txt", "w")

        file1.writelines("{:<8} {:<3}  {:<15}  {:<10}  {:<10}  {:<10}".format("CID", "   ", "Name", "Pt.",
                                                                              "Enl.", "Avg."))
        file1.writelines("\n")
        file1.writelines("{:<8}{:<3}{:<15}{:<10}{:<10}{:<13}".format('________', '___', '_______________', '__________'
                                                                     , '__________', '_____________'))
        file1.writelines("\n")
        for i in list_course_object:
            if i.__course_type[0] == "C":
                x = "*"
            else:
                x = "-"
            file1.writelines \
                ("{:<8} {:<3}  {:<15}  {:<10}  {:<10}  {:<10}".format(i.id, x, i.name, i.credit, i.enroll, i.avg))
            file1.writelines("\n")
        file1.writelines("{:<8}{:<3}{:<15}{:<10}{:<10}{:<13}".format('________', '___', '_______________', '__________'
                                                                     , '__________', '_____________'))
        res = self.calculate_average_course_marks(list_course_object)
        file1.writelines("\n")
        file1.writelines(res)
        # file1.writelines(list_course_object)
        file1.close()
        print("courses_report.txt generated!")

    def calculate_average_course_marks(self, list_course_object):
        c = []
        list_course_object.sort(key=lambda x: x.avg)
        c = "The worse performing course is {} with an average {}".format(list_course_object[0].id,
                                                                          list_course_object[0].avg)
        print(c)
        return c
