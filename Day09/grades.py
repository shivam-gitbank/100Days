student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def grades(x):
    if (x) >= 91 and x <= 100:
        return "Outstanding"
    elif x >= 81 and x <= 90:
        return "Exceeds Expectations"
    elif x >= 71 and x <= 80:
        return "Acceptible"
    else:
        return "Fail !"

student_grades = {}

for i in student_scores:
    student_grades[i] = grades(student_scores[i]) # trying to access the value by assining the value index to grades dictionary

print(f"{student_grades}\n")