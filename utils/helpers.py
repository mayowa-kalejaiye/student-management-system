"""
Helper functions for computing statistics on student score data.
"""
import statistics

def highest_score(students):
    """
    Return the Student with the highest score.

    Args:
        students (list[Student]): list of Student objects.

    Returns:
        Student | None: the student with the highest score,
        or None if the list is empty.
    """
    # Corrective maintenance: prevent crash when the student list is empty.
    # Previously, max() on an empty sequence raised:
    #   ValueError: max() iterable argument is empty
    if not students:
        return None
    return max(students, key=lambda student: student.score)


def lowest_score(students):
    """
    Return the Student with the lowest score.

    Args:
        students (list[Student]): list of Student objects.
    Returns:
        Student | None: the student with the lowest score,
        or None if the list is empty.
    """
    # Corrective maintenance: same empty-list guard as highest_score(),
    # since min() has the identical failure mode on an empty sequence.
    if not students:
        return None
    return min(students, key=lambda student: student.score)

def median_score(students):
    """
    Return the median score of the students.

    Args:
        students (list[Student]): list of Student objects.
    Returns:
        float | None: the median score, or None if the list is empty.
    """
    # median() function from statistics module also raises ValueError on empty list.
    if not students:
        return None

    return statistics.median([student.score for student in students])
