"""
https://www.codewars.com/kata/5a5f9f80f5dc3f942b002309
Can a value be both True and False?
Define omnibool so that it returns True for the following:
omnibool == True and omnibool == False

https://www.codewars.com/kata/59f44c7bd4b36946fd000052
"""


class Omnibool:
    def __eq__(self, other):
        return True


omnibool = Omnibool()


def hist(string):
    err = ["u", "w", "x", "z"]
    c, err_msg = 0, ""
    for i in err:
        c = string.count(i)
        if 0 < c < 10:
            err_msg += i + "  " + str(c) + "     " + "*" * c + "\r"
        elif c >= 10:
            err_msg += i + "  " + str(c) + "    " + "*" * c + "\r"

    return err_msg[:-1]
