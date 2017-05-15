#! /usr/bin/env python3
# Two sum


class Solution(object):
    def two_sum(self, numlist, target):
        for i in range(len(numlist)):
            for j in range(i, len(numlist)):
                if numlist[i] + numlist[j] == target:
                    return i, j

    def two_sum_on(self, numlist, target):
        if len(numlist) <= 1:
            return False
        buff_dict = {}
        for i in range(len(numlist)):
            if numlist[i] in buff_dict:
                return [buff_dict[numlist[i]], i]
            else:
                buff_dict[target - numlist[i]] = i


s = Solution()
a = s.two_sum([2, 7, 11, 15], 13)
b = s.two_sum_on([2, 7, 11, 15], 13)
print(a)
print(b)
