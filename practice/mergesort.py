def mergesort(array):
    if len(array) < 2:
        return array

    array_length = len(array)
    mid = array_length / 2
    
    left = mergesort(array[0:mid])
    right = mergesort(array[mid:len(array)])

    merged_result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                merged_result.append(left.pop(0))
            else:
                merged_result.append(right.pop(0))
        elif len(left) > 0:
            merged_result.append(left.pop(0))
        else:
            merged_result.append(right.pop(0))

    return merged_result


if __name__ == '__main__':
    print(mergesort(map(int, raw_input().split())))





