def num2alpha(int_num):
    int_num = int(int_num) - 1
    if int_num < 0:
        raise ValueError('The augument must be a Positive integer.')
    lst_digit = [int_num % 26]
    int_num //= 26
    if int_num != 0:
        int_num -= 1
        while 1:
            lst_digit.insert(0,int_num % 26)
            int_num //= 26
            if int_num == 0:
                break
    return ''.join([chr(i + 65) for i in lst_digit])

print([num2alpha(i) for i in range(1,100)])