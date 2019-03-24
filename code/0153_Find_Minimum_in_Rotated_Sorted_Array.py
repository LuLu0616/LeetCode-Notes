if __name__ == "__main__":
    nums = [5, 1, 2, 3, 4]
    p = 0
    q = len(nums) - 1
    m = 0
    while p < q:
        m = p + int((q - p) / 2)
        if nums[m] > nums[q]:
            p = m + 1
        elif nums[m] < nums[q]:
            q = m
        else:
            q = q - 1
    print(nums[p])
