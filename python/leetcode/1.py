#coding = utf-8
import time
import random


class Solution(object):

    # def __init__(self):
    #     pass

    # O(n*n)
    def method1(self, nums, target):
        start = time.time()*1000
        try:
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if nums[i]+nums[j] == target:
                        return [i, j]
            return [0, 0]
        finally:
            end = time.time()*1000
            print(f'cost time:{end-start}')

    def method2(self, nums: list, target: int) -> list:
        start = time.time()*1000
        try:
            dict_ = {}
            for i in range(len(nums)):
                ftarget = target - nums[i]
                if ftarget in dict_:
                    return [i, dict_[ftarget]]
                dict_[nums[i]] = i
        finally:
            end = time.time()*1000
            print(f'cost time:{end-start}')


solution = Solution()
nums = []
# for i in range(100):
#     nums.append(random.randint(1, 100))
nums=[95, 46, 34, 36, 51, 35, 93, 44, 81, 91, 82, 53, 14, 62, 76, 43, 28, 83, 35, 62, 9, 32, 29, 22, 60, 12, 68, 76, 51, 29, 79, 53, 85, 49, 99, 18, 20, 42, 85, 31, 2, 57, 4, 66, 94, 38, 43, 44, 13, 17, 63, 6, 69, 79, 34, 4, 78, 9, 18, 44, 64, 32, 64, 54, 90, 85, 52, 32, 19, 38, 21, 28, 13, 35, 76, 88, 75, 17, 62, 10, 58, 30, 2, 55, 80, 92, 44, 96, 22, 48, 74, 63, 12, 63, 30, 92, 8, 77, 99, 61]
print(nums)
result = solution.method1(nums=nums, target=10)
print(result)
