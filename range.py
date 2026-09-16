name = input("Enter the student's name: ")
roll_number = input("Enter the roll number: ")

marks = float(input("Enter marks (0-100): "))
while marks < 0 or marks > 100:
    print("Invalid marks. Enter a value from 0 to 100.")
    marks = float(input("Enter marks (0-100): "))

attendance = float(input("Enter attendance percentage (0-100): "))
while attendance < 0 or attendance > 100:
    print("Invalid attendance. Enter a value from 0 to 100.")
    attendance = float(input("Enter attendance percentage (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

if attendance >= 75:
    attendance_status = "Satisfactory"
else:
    attendance_status = "Shortage of attendance"

if attendance >= 75 and marks >= 40:
    eligibility = "Eligible for examination"
else:
    eligibility = "Not eligible for examination"

print("\n--- Student Details ---")
print("Name:", name)
print("Roll number:", roll_number)
print("Grade:", grade)
print("Attendance status:", attendance_status)
print("Examination eligibility:", eligibility)