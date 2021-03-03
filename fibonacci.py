#coding:utf-8

# 递归
def fib_recu(n):
    if n <= 1:
        return n
    else:
        return fib_recu(n-1) + fib_recu(n-2)

# for i in range(10):
#     print(f"{fib_recu(i)}", end=" ")

# 循环
def fib_loop(n):
    fibs = [0, 1]
    if n <= 1:
        return n
    else:
        for i in range(n-2):
            fibs.append(fibs[-2]+fibs[-1])
    return fibs

#print(f"fibonacci number: {fib_loop(10)}")


# 迭代器对象
class Fibs:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib
# fibs = Fibs(100000)
# lst = [ fibs.__next__() for i in range(10)]
# print(lst)

# 生成器对象
def fib_iter():
    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr

import itertools
fibs = list(itertools.islice(fib_iter(), 100))
for i in range(2, 30):
    print(f"{fibs[i+1]}/{fibs[i]}={fibs[i+1]/fibs[i]}")



# 矩阵
import numpy as np
def fib_matrix(n):
    F = np.mat([[1,1], [1,0]])
    F_m = pow(F, n)
    return F_m[0, 0]

# print("fibonacci numbers:")
# for i in range(10):
#     print(fib_matrix(i), end=" ")



