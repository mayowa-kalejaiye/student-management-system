from students import students
from utils.helpers import highest_score, lowest_score


def main():
    print("Student Scores")
    print("-" * 20)

    for student in students:
        print(f"{student['name']}: {student['score']}")

    highest = highest_score(students)
    lowest = lowest_score(students)

    print("\nSummary")
    print(f"Highest Score: {highest['name']} ({highest['score']})")
    print(f"Lowest Score: {lowest['name']} ({lowest['score']})")


if __name__ == "__main__":
    main()
