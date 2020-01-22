
def binary_to_string(binary):
    return "".join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))


print(binary_to_string('0100100001100101011011000110110001101111') == 'Hello')
print(binary_to_string('00110001001100000011000100110001') == '1011')


def binary_to_string(bin_str):
    string = ''
    for i in range(0, len(bin_str), 8):
        string += chr(int(bin_str[i:i + 8], 2))
    return string


print(binary_to_string('0100100001100101011011000110110001101111') == 'Hello')
print(binary_to_string('00110001001100000011000100110001') == '1011')
