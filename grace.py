def main():
    # Q1
    no_cities = {}
    norcal = {'Fresno': 77, 'Napa': 74, 'Palo Alto': 70, 'Sacramento': 75,
              'San Francisco': 64, 'San Jose': 73, 'Oakland': 67,
              'Los Altos': 71, 'Mountain View': 72}
    print(hottest(norcal, 2))  # ['Fresno', 'Sacramento']
    print(hottest(norcal))  # ['Fresno', 'Sacramento', 'Napa', 'San Jose']
    print(hottest(norcal, 8))
    print(hottest(norcal, 20))
    print(norcal)
    print(hottest(no_cities, 6))  # []
    # Q2
    phrase1 = '''Simple is better than     complex and flat 
                 is better than nested'''
    phrase2 = '''Complex is  better than complicated 
                 and  Sparse is better than dense'''
    print(common_words(phrase1, phrase2))  # should print 5

    print(common_words('', ''))  # should print 0
    print(common_words('Hi Class', 'Hello world'))  # should print
    # Q3
    disney_class = {'Mickey': [78, 50, 100], 'Minnie': [88, 65, 99, 70],
                    'Pluto': [70, 49, 87, 66, 38], 'Donald': [40]}
    cs122 = {'Alex': [76, 90], 'Diana': [100, 100, 100],
             'Zoe': [50, 87, 90, 100]}
    empty_class = {}

    print(alert(disney_class))  # {'Donald', 'Pluto'}
    print(disney_class)  # unchanged
    print(alert(cs122))  # empty set
    print(cs122)  # unchanged
    print(alert(empty_class))  # empty set
    print(empty_class)  # unchanged
    # Q4
    print(make_password('Simple is       better than \t complicated'))  # will
    # return 'SIBTC'
    print(make_password('python'))  # will return 'P'
    print(make_password(''))  # will return ''
    # Q5
    empty_class = {}
    cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}
    print(extra_credit(cs122))  # {'Zoe':91, 'Alex': 94, 'Dan':80, 'Anna':101}
    print(cs122)  # {'Zoe':91, 'Alex': 94, 'Dan':80, 'Anna':101}
    print(
        extra_credit(cs122, 2))  # {'Zoe':93, 'Alex': 96, 'Dan':82, 'Anna':103}
    print(cs122)  # {'Zoe':93, 'Alex': 96, 'Dan':82, 'Anna':103}
    print(extra_credit(empty_class, 5))  # {}


def hottest(cities, n=4) -> list:
    return sorted(cities, key=cities.get, reverse=True)[:n]


def common_words(str1, str2):
    words = set(str1.lower().split()) & set(str2.lower().split())
    word_count = {word: 0 for word in words}
    for each_word in words:
        word_count[each_word] = word_count.get(each_word, 0) + 1
    result = len({word for word in word_count if word_count[word] == 1})
    return result


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
