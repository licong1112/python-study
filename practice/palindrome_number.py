def isPalindrome(x):
    """
    :type x: int
    :rtype: bool

    Given an integer, return if it is a palindrome number.
    """
    if x < 0:
        return False

    num_digits = len(str(x))
    div = 10 ** (num_digits - 1)

    while div >= 10:
        left_digit = x / div
        right_digit = x % 10

        if left_digit != right_digit:
            return False

        x = (x % div) / 10
        div /= 100

    return True


if __name__ == '__main__':
    print(isPalindrome(int(raw_input())))



