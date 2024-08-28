# Student Grade Management Systm
student_grades={
    # empty dictionary
}
def add_student(name, grade):
    student_grades[name]=grade
    print(f"Added {name} with a {grade} ")

def update_student(name, grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"{name} with a marks updated {grade}")
    
    else:
        print(f"{name} is not found!")

def delete_student(name,grade):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been deleted successfully")
    else:
        print(f"{name} is not found!")
    
def display_all_student():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name}:{grade}")
    else:
        print("No student found / added")

def main():
    while True:
        print("\nStudent Management System")
        print("1.Add Student")
        print("2.Update Student")
        print("3.Delete Student")
        print("4.Display All Student")
        print("5.Exit")

        choice=int(input("Enter your choice="))
        if choice==1:
            name=input("Enter student name=")
            grade=int(input("Enter student grade="))
            add_student(name, grade)
        
        elif choice==2:
            name=input("Enter Student name=")
            grade=int(input("Enter Student Grade="))
            update_student(name,grade)
        
        elif choice==3:
            name=input("Enter Student name=")
            delete_student(name,grade)
        
        elif choice==4:
            display_all_student()
        
        elif choice==5:
            print("Closing the Program")
            break
    
        else:
            print("Invalid Choice")
         
main()