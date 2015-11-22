def reverse(x):
    """
    :type x: int
    :rtype: int

    This is not an ideal solution. I intentionally wrote it like this in order 
    to get familiar with Python built-in functions.
    """
    is_negative = x < 0
    x = abs(x)

    x_str = str(x)
    x_reverse_str = x_str[: : -1]

    if is_negative:
        result = int(x_reverse_str) * (-1)
        return 0 if result < -(2 ** 31) else result

    result = int(x_reverse_str)
    return 0 if result > (2 ** 31 - 1) else result
    

if __name__ == "__main__":
    print(reverse(int(raw_input())))
