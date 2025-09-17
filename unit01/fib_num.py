"""生成斐波那契数列并计算时间 """

import time
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

start = time.time()
# 计算前10个数
for i in range(40):
    print(fibonacci_recursive(i), end=" ")
# 输出: 0 1 1 2 3 5 8 13 21 34

print("\nTime taken:", time.time() - start)