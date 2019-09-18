# ---------------------------------------------------------------------
# Name: Homework 4
# Purpose: Dictionary applications
# Author: Kiwibud
# ---------------------------------------------------------------------
"""
Dictionary applications

Find n hottest cities from the given dictionary of cities
Compute number of unique words in common of two strings
Filter the students that have at least one grade below 50
Extract and capitalize first letter of each word in the given string
Add extra credits to each student in the given dictionary
"""


def hottest(cities, n=4):
    """
    Find n hottest cities from the given dictionary of cities
    :param cities: (dictionary) cities' name and their temperature
    :param n: (number) requested number of cities defaults to 4
    :return: (list) list of n cities
    """
    return sorted(cities, key=cities.get, reverse=True)[:n]


def common_words(str1, str2):
    """
    Compute number of unique words in common of two strings
    :param str1: (String) string 1
    :param str2: (String) string 2
    :return: (number) number of common unique words of two strings
    """
    return len(set(str1.lower().split()) & set(str2.lower().split()))


def alert(students):
    """
    Filter the students that have at least one grade below 50
    :param students: (dictionary) students and their grades
    :return: (set) set of students' names
    """
    return {name for name in students if min(students[name]) < 50}


def make_password(sentence):
    """
    Extract and capitalize first letter of each word in the given string
    :param sentence: (String) the given sentence
    :return: (String) the expected output string
    """
    return '\'' + ''.join(word[0] for word
                          in sentence.split()).upper() + '\''


def extra_credit(students, extra_points=1):
    """
    Add extra credits to each student in the given dictionary
    :param students: (dictionary) students and their grades
    :param extra_points: (number) extra credit defaults to 1 if omitted
    :return: (dictionary) modified dictionary of students and new grades
    """
    for each_student in students:
        students[each_student] += extra_points
    return students


def main():
    print('Testing hottest function')
    no_cities = {}
    norcal = {'Fresno': 77, 'Napa': 74, 'Palo Alto': 70, 'Sacramento': 75,
              'San Francisco': 64, 'San Jose': 73, 'Oakland': 67,
              'Los Altos': 71, 'Mountain View': 72}
    print(hottest(norcal, 2))
    print(hottest(norcal))
    print(hottest(norcal, 8))
    print(hottest(norcal, 20))
    print(norcal)
    print(hottest(no_cities, 6))
    print('Testing the common_words function:')
    phrase1 = '''Simple is better than     complex and flat 
                 is better than nested'''
    phrase2 = '''Complex is  better than complicated 
                 and  Sparse is better than dense'''
    print(common_words(phrase1, phrase2))
    print(common_words('We are Kiwibud', 'Kiwibud are us'))
    print(common_words('', ''))
    print(common_words('Hi Class', 'Hello world'))
    print('Testing alert function')
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
    print('Testing make_password function')
    print(make_password('Simple is       better than \t complicated'))
    print(make_password('python'))
    print(make_password(''))
    print('Testing extra_credit function')
    empty_class = {}
    cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    print(extra_credit(cs122))
    # {'Zoe':91, 'Alex': 94, 'Dan':80, 'Anna':101}
    print(cs122)  # {'Zoe':91, 'Alex': 94, 'Dan':80, 'Anna':101}
    print(extra_credit(cs122, 2))
    # {'Zoe':93, 'Alex': 96, 'Dan':82, 'Anna':103}
    print(cs122)  # {'Zoe':93, 'Alex': 96, 'Dan':82, 'Anna':103}
    print(extra_credit(empty_class, 5))  # {}


if __name__ == '__main__':
    main()
