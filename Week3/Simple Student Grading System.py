class Students:
    def __init__(self,name):
        self.name=name
        self.grades={}
    def add_grades(self,subject,grade):
        self.grades[subject]=grade
        print(f"Added {grade} for {subject} to {self.name}\n")
    def show_info(self):
        print(f"Grades for {self.name}:")
        if not self.grades:
            print("No grades recorded.")
        else:
            for subject,grade in self.grades.items():
                print(f"-{subject}, {grade}")
students={}
while True:
    print("\n Student Grade Manager")
    print("1 Add new student")
    print("2 Record grade")
    print("3 Show student grades")
    print("4 Exit")
    case =input("Choose an option 1 to 4: ")
    if case =='1':
        name = input("Enter student name: ")
        if name in students:
            print("Students has already exists.")
        else:
            students[name]=Students(name)
            print(f"Student {name} added.")
    elif case=='2':
        name = input("Enter student name: ")
        if name in students:
            subject=input("Enter subject name: ")
            try:
                grade= float(input("Enter grade: "))
                students[name].add_grades(subject,grade)
            except ValueError:
                print("Please enter a valid number for grade.")
        else:
            print("Student not found. Please add the student first.")
    elif case=='3':
        name = input("Enter student name to view grades: ")
        if name in students:
            students[name].show_info()
        else:
             print("Student not found.")
    elif case=='4':
        print("Bye!!")
        break
    else:
        print("Invalid choice. Please choose option 1 to 4.")
    