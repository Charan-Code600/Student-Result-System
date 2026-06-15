


import pandas as pd
import os

FILE = "students.csv"

if os.path.exists(FILE):
    df = pd.read_csv(FILE)
else:
    df = pd.DataFrame(columns=["Name", "Roll", "Math", "Science", "English", "Hindi", "Computer", "Average", "Grade"])

while True:
    print("""
====================
Student Result System
====================

Add Student        enter ---> 1
Show All Results   enter ---> 2
Search Student     enter ---> 3
Class Topper       enter ---> 4
Class Summary      enter ---> 5
Delete Student     enter ---> 6
Exit               enter ---> 7
""")

    option = input("Choose: ")

    if option == "1":
        try:
            name = input("Student Name : ")
            roll = input("Roll Number : ")
            math = float(input("Math Marks : "))
            science = float(input("Science Marks : "))
            english = float(input("English Marks : "))
            hindi = float(input("Hindi Marks : "))
            computer = float(input("Computer Marks : "))
            average = (math + science + english + hindi + computer) / 5

            if average >= 90:
                grade = "A"
            elif average >= 75:
                grade = "B"
            elif average >= 60:
                grade = "C"
            elif average >= 40:
                grade = "D"
            else:
                grade = "F"

            new_row = pd.DataFrame([{
                "Name": name,
                "Roll": roll,
                "Math": math,
                "Science": science,
                "English": english,
                "Hindi": hindi,
                "Computer": computer,
                "Average": round(average, 2),
                "Grade": grade
            }])

            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(FILE, index=False)
            print(f"✅ {name} added successfully!")
        except ValueError:
            print("❌ Invalid marks! Please enter numbers only!")

    elif option == "2":
        if df.empty:
            print("❌ No students found!")
        else:
            print(df.to_string(index=False))

    elif option == "3":
        search = input("Enter Name or Roll : ")
        result = df[(df["Name"] == search) | (df["Roll"].astype(str) == str(search))]
        if result.empty:
            print("❌ Student not found!")
        else:
            print(result.to_string(index=False))

    elif option == "4":
        if df.empty:
            print("❌ No students found!")
        else:
            topper = df.loc[df["Average"].idxmax()]
            print("\n🏆 Class Topper:")
            print(topper.to_string())

    elif option == "5":
        if df.empty:
            print("❌ No students found!")
        else:
            print(f"\n📊 Class Summary:")
            print(f"Total Students : {len(df)}")
            print(f"Class Average  : {round(df['Average'].mean(), 2)}")
            print(f"Highest Score  : {df['Average'].max()}")
            print(f"Lowest Score   : {df['Average'].min()}")
            print(f"Pass Count     : {len(df[df['Grade'] != 'F'])}")
            print(f"Fail Count     : {len(df[df['Grade'] == 'F'])}")

    elif option == "6":
        delete = input("Enter Name to delete : ")
        if delete in df["Name"].values:
            df = df[df["Name"] != delete]
            df.to_csv(FILE, index=False)
            print(f"✅ {delete} deleted!")
        else:
            print("❌ Student not found!")

    elif option == "7":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option!")
