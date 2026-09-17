while True:
    name = input("enter student name or 'stop' to finish: ")
    if name == "stop":
        break
    total = int(input("enter total number of classes: "))
    attended = int(input("enter number of classes attended: "))

    percentage = (attended/total)*100

    print("attendence:",round(percentage,2),"%")
    print("attendence processing completed ,")