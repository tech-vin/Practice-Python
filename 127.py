int_value = 30

if int_value.bit_length() <= 63:
    print((-2 * 63).bit_length())
    print((2 * 63).bit_length())