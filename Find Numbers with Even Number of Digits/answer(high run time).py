from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        nums_nums = []
        for i in nums:
            counter = 0
            for n in range(5):
                if i >= 1:
                     i = i/10
                     counter +=1
                else:
                     if counter % 2 == 0:
                         nums_nums.append(counter)
                     break

        return len(nums_nums)
