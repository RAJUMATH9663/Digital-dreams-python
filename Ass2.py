def check_attendance(login_time):
    if login_time < 9.30:
        return "Present"
    elif login_time <= 10.00:
        return "Late"
    else:
        return "Absent"

# Example
print(check_attendance(9.10))
print(check_attendance(9.45))
print(check_attendance(10.30))