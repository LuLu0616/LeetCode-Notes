def find_min_in_rotated_array(nums):
    p = 0
    q = len(nums)-1
    m = int((p + q) / 2)
    while nums[m] < nums[m+1]:
        if nums[p] > nums[m]:
            q = m
            m = int((p + q) / 2)
        elif nums[q] < nums[m]:
            p = m
            m = int((p + q) / 2)
        else:
            return nums[p]
    return nums[m+1]


if __name__ == "__main__":
    nums = [5, 1, 2, 3, 4]
    print(find_min_in_rotated_array(nums))
