while True:
    name = input("\nenter student name or 'stop' to finish: ")
    if name == 'stop':
        break
    total =int (input("enter total classes"))
    attended = int(input("enter classes attended"))
    if total <= 0 or attended < 0 or attended > total:
        print("Invalid input. Please enter valid numbers.")
        continue    
    percentage = (attended / total) * 100
    print ("students:",name)
    print("attendence:",round(percentage,2),"%")