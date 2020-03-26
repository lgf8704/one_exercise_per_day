"""Fibonacci"""
import time

nums = [1, 1]


# Method 1: 遍历
def fib_traverse(n):

    if n == 1 or n == 2:
        return 1
    nums = [1, 1]
    for i in range(2, n):
        nums.append(nums[i - 1] + nums[i - 2])
    return nums[-1]


# Method 2: 递归
def fib_recurve(n):

    if n == 1 or n == 2:
        return 1
    else:
        return fib_recurve(n - 1) + fib_recurve(n - 2)


# Method 3: 有记忆的递归
def fib_recurve_memory(n):
    if n <= len(nums):
        pass
    else:
        nums.append(fib_recurve_memory(n - 1) + fib_recurve_memory(n - 2))

    return nums[n - 1]


def test_time(i, n):
    if i == 1:
        print("采用遍历的方法")
        start = time.perf_counter()
        fib_traverse(n)
        end = time.perf_counter()
        print(f"总共耗时{end - start} 秒")
    elif i == 2:
        print("采用递归的方法")
        start = time.perf_counter()
        fib_recurve(n)
        end = time.perf_counter()
        print(f"总共耗时{end - start} 秒")
    elif i == 3:
        print("采用记忆递归的方法")
        start = time.perf_counter()
        fib_recurve_memory(n)
        end = time.perf_counter()
        print(f"总共耗时{end - start} 秒")


if __name__ == "__main__":
    start = time.perf_counter()
    while True:
        n = int(input("请输入您要查的是Fibnacci数列的第几项： "))

        print("三种方法执行效率测试")
        for i in range(1, 4):
            test_time(i, n)