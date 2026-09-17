choice = "yes"
while choice =="yes":
    name = input("\nenter student name: ")
    total = int(input("enter total number of classes: "))
    attended = int(input("enter number of classes attended: "))

    percentage = (attended/total)*100

    print("students:",name)
    print("attendence percentage:",percentage,"%")