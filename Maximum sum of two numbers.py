import collections
##Given an array A consisting of N integers, returns the maximum sum of two numbers whose digits add up to an equal sum.
##if there are not two numbers whose digits have an equal sum, the function should return -1.
def MaximumSum(A):
    table = collections.defaultdict(list)
    for a in A:
        num = a
        s = 0
        while num:
            s += num % 10
            num //= 10
        table[s].append(a)          
        maxSum = -1
    for val in table.values():
        if len(val) > 1:
            maxSum = max(maxSum, sum(sorted(val)[-2:]))
    return maxSum
print(MaximumSum([51, 71, 17, 42]))
