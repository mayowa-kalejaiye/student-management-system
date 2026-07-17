from students import students
from utils.helpers import highest_score, lowest_score, median_score


def main():
    print("Student Scores")
    print("-" * 20)

    # Corrective maintenance: guard added here too, same in helpers.py.
    # Without this, an empty list would still loop over nothing pointlessly
    # and then crash on highest['name'] / lowest['name'] since both would
    # now return None from the fixed helper functions above.
    if not students:
        print("No student records available.")
        return

    for student in students:
        print(f"{student.name}: {student.score}")

    highest = highest_score(students)
    lowest = lowest_score(students)
    median = median_score(students)


    print("\nSummary")
    print(f"Highest Score: {highest.name:<15} ({highest.score:>5})")
    print(f"Lowest Score: {lowest.name:<15} ({lowest.score:>5})")
    print(f"Median Score: {median}")
if __name__ == "__main__":
    main()
