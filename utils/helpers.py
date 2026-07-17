def highest_score(students):
    return max(students, key=lambda student: student["score"])

def lowest_score(students):
    return min(students, key=lambda student: student["score"])

def average_score(students):
    total = sum(student["score"] for student in students)
    return total / len(students)

