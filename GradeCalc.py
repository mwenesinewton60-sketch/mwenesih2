def calculate_grade(score):
    if score >=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return"FAIL"

name = input("Enter Student Name:")
score = float(input("Enter Student Score(0-100):"))

grade= calculate_grade(score)
print("Student:",name)
print("Score:",score)
print("Grade:",grade)