if __name__ == "__main__":
    nums = [3, 3, 7, 7, 10, 11, 11]
    p = 0
    q = len(nums) - 1
    m = 0
    while p < q:
        m = p + int((q - p) / 2)
        if nums[m] == nums[m-1]:
            if (m - p) % 2 == 0:
                q = m - 2
            else:
                p = m + 1
        elif nums[m] == nums[m+1]:
            if (q - m) % 2 == 0:
                p = m + 2
            else:
                q = m - 1
        else:
            print(nums[m])

    print(nums[p])
