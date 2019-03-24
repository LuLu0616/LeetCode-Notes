def my_sqrt(x):
    if x == 1:
        return 1
    p = 0
    q = x
    while p <= q:
        m = (p + q) // 2
        if m * m <= x < (m + 1) * (m + 1):
            return m
        elif x < m * m:
            q = m
        else:
            p = m

            
if __name__ == "__main__":
    x = 8
    print(my_sqrt(x))
