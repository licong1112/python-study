def mergesort(array):
    if len(array) < 2:
        return array

    array_length = len(array)
    mid = array_length / 2
    
    left = mergesort(array[:mid])
    right = mergesort(array[mid:array_length])

    left_length = len(left)
    right_length = len(right)

    left_ind = 0
    right_ind = 0

    merged_result = []
    while left_ind < left_length or right_ind < right_length:
        if left_ind < left_length and right_ind < right_length:
            if left[left_ind] < right[right_ind]:
                merged_result.append(left[left_ind])
                left_ind += 1
            else:
                merged_result.append(right[right_ind])
                right_ind += 1
        elif left_ind < left_length:
            merged_result.append(left[left_ind])
            left_ind += 1
        else:
            merged_result.append(right[right_ind])
            right_ind += 1

    return merged_result


if __name__ == '__main__':
    print(mergesort(map(int, raw_input().split())))





