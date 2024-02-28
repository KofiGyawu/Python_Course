# Task
# Update the function given in the IDE to output the following to the IDE by printing from inside the function.
# A^2 + 2*A*B + B^2
# A + B
# Sample 1:
# Input
# 3 5
# 2 7
# 4 1
# Output :
# 64
# 8
# 81
# 9
# 25
# 5

def compute_value(a, b):
    value_result = a ** 2 + 2 * a * b + b ** 2
    value_result2 = a + b

    print(value_result)
    print(value_result2)


t = 3
for _ in range(t):
    A, B = map(int, input().split())
    compute_value(A, B)
