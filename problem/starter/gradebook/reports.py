"""gradebook.reports — build a printable report from grade records."""
from .stats import (average_per_student, subjects_offered, top_scorer, passing_students)

def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report"""
    print("total records:",len(records))
    s=subjects_offered(records)
    print("\nsubject offered:")
    for i in s:
        print(i)
    a=average_per_student(records)
    print("\nAverages:")
    for i in a:
        print(i,":",a[i])
    print("\nTop scorer:",top_scorer(records))
    p=passing_students(records)
    print("\npassing students:")
    for i in p:
        print(i)
