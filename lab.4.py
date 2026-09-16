def classify_performance(marks):
    if 90 <= marks <= 100:
        return "Excellent"
    elif 75 <= marks < 90:
        return "Very Good"
    elif 60 <= marks < 75:
        return "Good"
    elif 45 <= marks < 60:
        return "Average"
    elif 0 <= marks < 45:
        return "Poor"
    else:
        return "Invalid marks. Please enter a value between 0 and 100."

# Input from user
marks = float(input("Enter the student's marks: "))

result = classify_performance(marks)
print(f"Performance category: {result}")