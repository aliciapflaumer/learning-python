# Slow but works:

# def climbingStairs(n):
#     if n <= 1:
#         return 1
#     return climbingStairs(n -1) + climbingStairs(n - 2)
#
# print(climbingStairs(38))

#  Better:

def climbingStairs(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

print(climbingStairs(4))

#  0/n Solution with memoization:
# def climbingStairs(n):
#     memo = {}
#     return climbingStairs_helper(n, memo)
#
# def climbingStairs_helper(n, memo):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0
#     if n in memo:
#         return memo[n]
#     memo[n] = climbingStairs_helper(n - 1, memo) + climbingStairs_helper(n - 2, memo)
#     return memo[n]
#
# print(climbingStairs(34))
