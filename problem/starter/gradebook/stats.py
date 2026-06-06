"""gradebook.stats — aggregate statistics over grade records."""

def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    avg={}
    a=0
    for i in records:
        sum=0
        for j in records:
            if i['name']==j['name']:
                sum=sum+j['score']
        a=sum/3
        avg[i['name']]=a
    return avg


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    n=set()
    for i in records:
        if i['subject'] not in n:
            n.add(i['subject'])
    return n

def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    t=()
    m=0
    a=average_per_student(records)
    for i in a:
        if a[i]>m:
            m=a[i]
            t=(i,m)
    return t

def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    ar=average_per_student(records)
    l=[]
    for i in ar:
        if ar[i]>=threshold:
            l.append(i)
    return l
