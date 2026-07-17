from students import students
from utils.helpers import (
    highest_score,
    lowest_score,
    average_score,
)


def display_students():
    print("=" * 35)
    print("      STUDENT REPORT")
    print("=" * 35)

    for student in students:
        print(f"{student['name']:<12} {student['score']}")

    highest = highest_score(students)
    lowest = lowest_score(students)
    average = average_score(students)

    print("\nStatistics")
    print("-" * 35)
    print(f"Highest Score : {highest['name']} ({highest['score']})")
    print(f"Lowest Score  : {lowest['name']} ({lowest['score']})")
    print(f"Average Score : {average:.2f}")


if __name__ == "__main__":
    display_students()