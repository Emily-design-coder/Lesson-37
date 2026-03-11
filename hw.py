working_days = int(input("Enter the total amount of working days: "))
absent_days = int(input("Enter the total amount of absent days: "))

present_days = working_days + absent_days
attendance = (working_days / present_days) * 100

print("Attendance:", attendance, "%")

if attendance >= 75:
    print("You can sit the exam.")
else:
    print("You cannot sit the exam.")