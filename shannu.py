total_classes = int(input("Enter the total number of classes conducted: "))
classes_attended = int(input("Enter the number of classes attended: "))

if total_classes > 0:
    attendance_percentage = (classes_attended / total_classes) * 100
    print(f"Attendance percentage: {attendance_percentage:.2f}%")
else:
    print("Total classes must be greater than zero.")

