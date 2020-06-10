"""
"Fizz Buzz", если число делится на 3 и 5;
"Fizz", если число делится на 3;
"Buzz", если число делится на 5;
"""


# Your optional code here
# You can import some modules or create additional functions


def checkio(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    return f"{number}"


"""
Вам необходимо поделить всех нанятых матросов на 2 команды, согласно следующим правилам: те, чей возраст меньше 
20 лет или больше 40 - отправляются на первый корабль, все остальные - на второй. Это
"""


def two_teams(sailors):
    # frst_team = []
    # sec_team = []
    # for name, age in sailors.items():
    #     if age < 20 or age > 40:
    #         frst_team.append(name)
    #     else:
    #         sec_team.append(name)
    # return [sorted(frst_team), sorted(sec_team)] # return list(map(sorted, teams_list))
    frst_team = sorted([sailor for sailor, age in sailors.items() if age < 20 or age > 40])
    sec_team = sorted([sailor for sailor in sailors.keys() if sailor not in frst_team])
    return [frst_team, sec_team]


def is_acceptable_password(password: str) -> bool:
    """
    the length should be bigger than 6;
    should contain at least one digit.
    """
    # return len(password) > 6 and any(map(str.isdigit, password))
    # if len(password) > 6 and any(str.isdigit(letter) for letter in password)
    return True if len(password) > 6 and sum(n.isdigit() for n in password) > 0 else False


def is_acceptable_password2(password: str) -> bool:
    """
    the length should be bigger than 6;
    should contain at least one digit, but cannot consist of just digits.
    """
    # your code here
    # and not sum(n.isdigit() for n in password) == len(password):
    if len(password) > 6 \
            and any(map(str.isdigit, password)) \
            and any(map(str.isalpha, password)):
        return True
    return False


def is_acceptable_password3(password: str) -> bool:
    """
    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    having numbers or containing just numbers does not apply to the password longer than 9.
    """
    if len(password) > 6 \
            and any(map(str.isalpha, password)) \
            or sum(n.isdigit() for n in password) >= 9:
        return True
    return False


def is_acceptable_password4(password: str) -> bool:
    """
    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    having numbers or containing just numbers does not apply to the password longer than 9.
    a string should not contain the word "password" in any case.
    """
    if len(password) > 6 \
            and "password" not in password.lower() \
            and any(map(str.isalpha, password)) \
            or sum(n.isdigit() for n in password) >= 9:
        return True
    return False


def is_acceptable_password5(password):
    """
    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    having numbers or containing just numbers does not apply to the password longer than 9.
    a string should not contain the word "password" in any case;
    should contain 3 different letters (or digits) even if it is longer than 10
    """
    if len(password) > 6 \
            and 'password' not in password.lower() \
            and any(map(str.isalpha, password)) \
            and len({c: c.count(c) for c in password}) > 2 \
            or sum(n.isdigit() for n in password) >= 9:
        return True
    return False


if __name__ == '__main__':
    # print('Example:')
    # print(checkio(15))
    #
    # assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    # assert checkio(6) == "Fizz", "6 is divisible by 3"
    # assert checkio(5) == "Buzz", "5 is divisible by 5"
    # assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    # print("Example:")
    # print(two_teams({
    #     'Fernandes': 18,
    #     'Johnson': 22,
    #     'Kale': 41,
    #     'McCortney': 54}))
    #
    # # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert two_teams({
    #     'Smith': 34,
    #     'Wesson': 22,
    #     'Coleman': 45,
    #     'Abrahams': 19}) == [
    #            ['Abrahams', 'Coleman'],
    #            ['Smith', 'Wesson']
    #        ]
    #
    # assert two_teams({
    #     'Fernandes': 18,
    #     'Johnson': 22,
    #     'Kale': 41,
    #     'McCortney': 54}) == [
    #            ['Fernandes', 'Kale', 'McCortney'],
    #            ['Johnson']
    #        ]
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    # print("Example:")
    # print(is_acceptable_password('short'))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert is_acceptable_password('short') == False
    # assert is_acceptable_password('muchlonger') == False
    # assert is_acceptable_password('ashort') == False
    # assert is_acceptable_password('muchlonger5') == True
    # assert is_acceptable_password('sh5') == False
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    # print("Example:")
    # print(is_acceptable_password2('short'))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert is_acceptable_password2('short') == False
    # assert is_acceptable_password2('muchlonger') == False
    # assert is_acceptable_password2('ashort') == False
    # assert is_acceptable_password2('muchlonger5') == True
    # assert is_acceptable_password2('sh5') == False
    # assert is_acceptable_password2('1234567') == False
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    # print("Example:")
    # print(is_acceptable_password3('short'))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert is_acceptable_password3('short') == False
    # assert is_acceptable_password3('short54') == True
    # assert is_acceptable_password3('muchlonger') == True
    # assert is_acceptable_password3('ashort') == False
    # assert is_acceptable_password3('muchlonger5') == True
    # assert is_acceptable_password3('sh5') == False
    # assert is_acceptable_password3('1234567') == False
    # assert is_acceptable_password3('12345678910') == True
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    # print("Example:")
    # print(is_acceptable_password4('short'))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert is_acceptable_password4('short') == False
    # assert is_acceptable_password4('short54') == True
    # assert is_acceptable_password4('muchlonger') == True
    # assert is_acceptable_password4('ashort') == False
    # assert is_acceptable_password4('muchlonger5') == True
    # assert is_acceptable_password4('sh5') == False
    # assert is_acceptable_password4('1234567') == False
    # assert is_acceptable_password4('12345678910') == True
    # assert is_acceptable_password4('password12345') == False
    # assert is_acceptable_password4('PASSWORD12345') == False
    # assert is_acceptable_password4('pass1234word') == True
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    print("Example:")
    print(is_acceptable_password5('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password5('short') == False
    assert is_acceptable_password5('short54') == True
    assert is_acceptable_password5('muchlonger') == True
    assert is_acceptable_password5('ashort') == False
    assert is_acceptable_password5('muchlonger5') == True
    assert is_acceptable_password5('sh5') == False
    assert is_acceptable_password5('1234567') == False
    assert is_acceptable_password5('12345678910') == True
    assert is_acceptable_password5('password12345') == False
    assert is_acceptable_password5('PASSWORD12345') == False
    assert is_acceptable_password5('pass1234word') == True
    assert is_acceptable_password5('aaaaaa1') == False
    assert is_acceptable_password5('aaaaaabbbbb') == False
    assert is_acceptable_password5('aaaaaabb1') == True
    assert is_acceptable_password5('abc1') == False
    assert is_acceptable_password5('abbcc12') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
