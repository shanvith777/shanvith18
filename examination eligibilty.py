total_classes = int(input("Enter the total number of classes conducted: "))
classes_attended = int(input("Enter the number of classes attended: "))
marks = float(input("Enter the student's marks: "))

if total_classes > 0:
    attendance_percentage = (classes_attended / total_classes) * 100

    if attendance_percentage >= 75 and marks >= 40:
        print("The student is eligible for the examination.")
    else:
        print("The student is not eligible for the examination.")
else:
    print("Total classes must be greater than zero.")