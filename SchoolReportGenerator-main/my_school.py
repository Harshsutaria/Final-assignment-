import sys
from School import School

# Create instance of the School Class
school = School()

def checker(file1):
    flag = False
    a = School.read(file1)
    b = School.format_array(a)
    for i in a:
        if('TBA' in i):
            flag  = True
    return flag
            

def main():
    if len(sys.argv) == 1:
        print("[Usage:] Python my_school.py <scores file>")

    elif len(sys.argv) == 2:

        file1 = sys.argv[1]
        school.read_level_1_file(file1)

    elif len(sys.argv) == 3:

        file1 = sys.argv[1]
        file2 = sys.argv[2]
        school.read_level_2_files(file1, file2)

    else:

        file1 = sys.argv[1]
        file2 = sys.argv[2]
        file3 = sys.argv[3]
        c = checker(file1)
        if(c):
            school.read_level_4_files(file1, file2, file3)
        else:
            school.read_level_3_files(file1, file2 , file3)

if __name__ == "__main__":
    main()
