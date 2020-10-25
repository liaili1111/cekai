# coding=utf-8
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 解题思路，先求出所有的组合，然后去重
count=0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print i, j, k
                count=count+1
print count