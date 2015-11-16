def reverse(x):
    """
    :type x: int
    :rtype: int

    This is not an ideal solution. I intentially wrote it like this in order 
    to get familiar with Python built-in functions.
    """
    is_negative = False
    if x < 0:
        is_negative = True
        x = -x

    x_str = str(x)
    x_reverse_str = [''] * len(x_str)

    for i in range(len(x_str)):
        x_reverse_str[i-1] = x_str[-i]

    result_str = ''.join(x_reverse_str)
    if is_negative:
        result = int(result_str) * (-1)
        return 0 if result < -(2 ** 31) else result

    result = int(result_str)
    return 0 if result > (2 ** 31 - 1) else result
    

if __name__ == "__main__":
    print(reverse(int(raw_input())))
