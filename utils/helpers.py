def highest_score(students):
    return max(students, key=lambda student: student["score"])

def lowest_score(students):
    return min(students, key=lambda student: student["score"])
