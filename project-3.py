
# Collection Manipulator - Student Data Organizer

students = {}
student_list = []
subjects_offered = set()

print("Welcome to the Student Data Organizer!")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")

        if student_id in students:
            print("Student ID already exists!")
            continue

        name = input("Enter Name: ").strip().title()
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ").strip().upper()
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        subject_input = input("Enter Subjects (comma-separated): ")

        subject_list = [
            subject.strip().title()
            for subject in subject_input.split(",")
            if subject.strip()
        ]

        # Tuple stores unchangeable student information
        immutable_info = (student_id, dob)

        # Dictionary stores student details
        students[student_id] = {
            "immutable_info": immutable_info,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subject_list
        }

        # List stores multiple student records
        student_list.append(student_id)

        # Set stores unique subjects without duplicates
        subjects_offered.update(subject_list)

        print("\nStudent added successfully!")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\n--- All Students ---")

            for sid in student_list:
                if sid in students:
                    s = students[sid]
                    print("\nStudent ID:", s["immutable_info"][0])
                    print("Name:", s["name"])
                    print("Age:", s["age"])
                    print("Grade:", s["grade"])
                    print("Date of Birth:", s["immutable_info"][1])
                    print("Subjects:", ", ".join(s["subjects"]))

    elif choice == "3":
        student_id = input("Enter Student ID to update: ")

        if student_id in students:
            s = students[student_id]

            print("Leave blank to keep the existing value.")

            name = input("Enter new Name: ").strip()
            age = input("Enter new Age: ").strip()
            grade = input("Enter new Grade: ").strip()
            subject_input = input(
                "Enter new Subjects (comma-separated): "
            ).strip()

            if name:
                s["name"] = name.title()

            if age:
                s["age"] = int(age)

            if grade:
                s["grade"] = grade.upper()

            if subject_input:
                s["subjects"] = [
                    sub.strip().title()
                    for sub in subject_input.split(",")
                    if sub.strip()
                ]
                subjects_offered.update(s["subjects"])

            print("Student updated successfully!")
        else:
            print("Student ID not found.")

    elif choice == "4":
        student_id = input("Enter Student ID to delete: ")

        if student_id in students:
            del students[student_id]
            student_list.remove(student_id)
            print("Student deleted successfully!")
        else:
            print("Student ID not found.")

    elif choice == "5":
        if subjects_offered:
            print("\n--- Subjects Offered ---")
            for subject in sorted(subjects_offered):
                print("-", subject)
        else:
            print("No subjects available.")

    elif choice == "6":
        print("Thank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
