def area(height, left, right):
    return min(height[left], height[right]) * (right - left)

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    start = 0
    end = len(height) - 1
    result = area(height, start, end)

    while start < end:
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
        result = max(result, area(height, start, end))

    return result
    


if __name__ == "__main__":
   print(maxArea(map(int, raw_input().split())))
