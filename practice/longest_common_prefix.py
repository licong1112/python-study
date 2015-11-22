def isValidIndex(strs, index):
    """
    Returns True if all strings in *strs* have character at position *index*.
    """
    for s in strs:
        if (not s) or (index >= len(s)):
            return False
    return True

def isValidChar(strs, index):
    """
    isValidIndex(strs, index) == True.
    """
    c = strs[0][index]
    for s in strs[1:]:
        if c != s[index]:
            return False
    return True


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    result = ""
    if not strs:
        return result;

    index = 0
    while isValidIndex(strs, index) and isValidChar(strs, index):
        result += strs[0][index]
        index += 1

    return result

    

if __name__ == "__main__":
    print(longestCommonPrefix(raw_input().split()))
