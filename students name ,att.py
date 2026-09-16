name = input("Enter the student's name: ")
roll_number = input("Enter the roll number: ")
marks = float(input("Enter the marks: "))
attendance = float(input("Enter the attendance percentage: "))

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