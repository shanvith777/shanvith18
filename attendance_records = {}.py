attendance_records = {}

while True:
    name = input("Enter student name (or type 'done' to finish): ")

    if name.lower() == "done":
        break

    status = input(f"Is {name} present? (yes/no): ").lower()

    while status not in ("yes", "no"):
        print("Please enter yes or no.")
        status = input(f"Is {name} present? (yes/no): ").lower()

    attendance_records[name] = "Present" if status == "yes" else "Absent"

print("\nAttendance Records:")
for name, status in attendance_records.items():
    print(f"{name}: {status}")