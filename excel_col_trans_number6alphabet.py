def num2alpha(int_col):
    int_col = int(int_col) - 1
    if int_col < 0:
        raise ValueError('The augument must be a Positive integer.')
    lint_digit = [int_col % 26]
    int_col //= 26
    if int_col != 0:
        int_col -= 1
        for i in range(3): #Remove this limit, if you treat larger numbers, just "while 1:".
            lint_digit.insert(0,int_col % 26)
            int_col //= 26
            if int_col == 0:
                break
        else:
            raise ValueError('The augument was too big for Excel.')
    return ''.join([chr(i + 65) for i in lint_digit])
            
print([num2alpha(i) for i in range(1,100)])

def alpha2num(str_col):
    lint_col = [ord(i) - 65 for i in reversed(str_col.strip())]
    lint_col = [i for i in lint_col if 0 <= i and i <= 25]
    if lint_col == []:
        raise ValueError('The augument has no [A-Z].')
    lint_col = [lint_col[i]*26**i for i in range(len(lint_col))]
    if len(lint_col) == 1:
        return lint_col[0] + 1
    else:
        return sum(lint_col) + 27
    
print([alpha2num(i) for i in [num2alpha(i) for i in range(1,100)]])
