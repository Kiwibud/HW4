def hottest(cities, n=4) -> list:
    return sorted(cities, key=cities.get, reverse=True)[:n]


def common_words(str1, str2):
    words = set(str1.lower().split()) & set(str2.lower().split())
    return len(words)


def alert(students) -> set:
    return {student for student in students
            if min(students[student]) < 50}


def make_password(string) -> str:
    return '\'' + ''.join(
        letter[0] for letter in string.split()).upper() + '\''


def extra_credit(students, credit=1):
    students.update({student: grade + credit for (student, grade) in
                     students.items()})
    return students


if __name__ == "__main__":
    main()
