# ---------------------------------------------------------------------
# Name: Homework 4
# Purpose: Dictionary applications
# Author: Kiwibud
# ---------------------------------------------------------------------

import string


def hottest(cities, num=4):
    return sorted(cities, key=cities.get, reverse=True)[0:num]


def common_words(str1, str2):
    # import string
    str1_set = set(str1.lower().strip(string.punctuation).split())
    str2_set = set(str2.lower().strip(string.punctuation).split())
    return len(str1_set & str2_set)


def alert(grades):
    return {name for name in grades if min(grades[name]) < 50}



def make_password(sentence):
    return ''.join(word[0] for word
                   in sentence.upper().strip(string.punctuation).split())


def extra_credit(grades, extra_points=1):
    for each_student in grades:
        grades[each_student] += extra_points;
    return grades


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
