def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        start = i + 1
        end = len(nums) - 1
        while start < end:
            sum = nums[start] + nums[end]
            if nums[i] == -sum:
                result.append([nums[i], nums[start], nums[end]])
                start += 1
                end -= 1
                while start < len(nums) and nums[start] == nums[start-1]:
                    start += 1
                while end > 0 and nums[end] == nums[end+1]:
                    end -= 1
            elif nums[i] > -sum:
                end -= 1
            else:
                start += 1
    return result


if __name__ == "__main__":
    nums = []
    for n in raw_input().split():
        nums.append(int(n))
    print(threeSum(nums))

