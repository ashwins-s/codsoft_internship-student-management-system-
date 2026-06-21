import csv

FILE_NAME = "students.csv"


class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks


def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, name, marks])

    print("Student Added Successfully!\n")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n--- Student Records ---")
            found = False

            for row in reader:
                found = True
                print(f"Roll No: {row[0]}, Name: {row[1]}, Marks: {row[2]}")

            if not found:
                print("No Records Found!")

    except FileNotFoundError:
        print("No Records Found!")

    print()


def search_student():
    roll_no = input("Enter Roll No to Search: ")

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == roll_no:
                    print("\nStudent Found!")
                    print(f"Roll No: {row[0]}")
                    print(f"Name: {row[1]}")
                    print(f"Marks: {row[2]}\n")
                    return

            print("Student Not Found!\n")

    except FileNotFoundError:
        print("No Records Found!\n")


def update_student():
    roll_no = input("Enter Roll No to Update: ")

    rows = []
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == roll_no:
                    found = True

                    name = input("Enter New Name: ")
                    marks = input("Enter New Marks: ")

                    rows.append([roll_no, name, marks])

                else:
                    rows.append(row)

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        if found:
            print("Student Updated Successfully!\n")
        else:
            print("Student Not Found!\n")

    except FileNotFoundError:
        print("No Records Found!\n")


def delete_student():
    roll_no = input("Enter Roll No to Delete: ")

    rows = []
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == roll_no:
                    found = True
                else:
                    rows.append(row)

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        if found:
            print("Student Deleted Successfully!\n")
        else:
            print("Student Not Found!\n")

    except FileNotFoundError:
        print("No Records Found!\n")


def sort_students():
    try:
        with open(FILE_NAME, "r") as file:
            reader = list(csv.reader(file))

        reader.sort(key=lambda x: int(x[2]), reverse=True)

        print("\n--- Students Sorted by Marks ---")
        for row in reader:
            print(f"Roll No: {row[0]}, Name: {row[1]}, Marks: {row[2]}")

        print()

    except FileNotFoundError:
        print("No Records Found!\n")


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Sort by Marks")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        sort_students()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!\n")