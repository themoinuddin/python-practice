# static_members.py
# Author: Moin Uddin

class Student:
    school = "Zenith Learning Hub"  # static variable
    count = 0                        # counts total students

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @staticmethod
    def show_school():
        print(f"School: {Student.school}")

s1 = Student("Moin")
s2 = Student("Ali")
s3 = Student("Sara")

Student.show_school()
print(f"Total Students: {Student.count}")