def sum_of_multiples(limit, multiples):
    nums = set()
    for m in multiples:
        if m == 0:
            continue
        for i in range(m,limit,m):
            nums.add(i)
    return sum(nums)
