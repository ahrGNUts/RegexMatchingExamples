import re

# begin function definitions


def phoneNumMatch():

    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # create regex object with re.compile (and pass raw string with r'[regex]' so everything doesnt need to be escaped
    mo = phoneNumRegex.search('My number is 415-555-4242.') # pass the string to search to look for the pattern
    print('Phone number found: ' + mo.group())
    print('\n')


def phoneNumGrouping():
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')# group 0 is entire pattern, 1 is fist parenths, 2 is second parenths
    mo = phoneNumRegex.search('My number is 415-555-4242.')
    print('Full expression:')
    print(mo.group())


    for i in range(3):
        print('Group ' + str(i) + ':')
        print(mo.group(i))

    # display groups
    print('\n')
    print('Groups:')
    print(mo.groups())

    # splitting up, printing the groups
    areaCode, mainNumber = mo.groups()

    print('\n')
    print('Area code:')
    print(areaCode)
    print('Main number:')
    print(mainNumber)

    # escaping, searching for, printing parentheses
    phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
    mo = phoneNumRegex.search('My number is (415) 555-4242.')

    print('\n')
    print('Area code:')
    print(mo.group(1))
    print('Main number:')
    print(mo.group(2))


def pipeGrouping():
    # pipe will return the first found instance of the search term if both are present
    heroRegex = re.compile(r'Batman|Tina Fey')
    mo1 = heroRegex.search('Batman and Tina Fey.')
    mo2 = heroRegex.search('Tina Fey and Batman.')

    print('\n')
    print('Searching \'Batman and Tina Fey\'')
    print(mo1.group())
    print('Searching \'Tina Fey and Batman\'')
    print(mo2.group())

    # top of p 154: batregex



# begin function calls, etc.
phoneNumMatch()
phoneNumGrouping()
pipeGrouping()
