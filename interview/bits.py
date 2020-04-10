lst = [False] * 2
xs = [()]
print(len(xs))
print(lst)

if xs:
    lst[0] = True
if xs[0]:
    lst[0] = True

# [True, False]


def countBits(n):
    #return bin(n).count('1') + bin(n).count('0') - 1
    return n.bit_length()


print(countBits(50))


def modulus(n):
    if isinstance(n, int):
        return n % 2
    else:
        return -1


print(modulus(15))
