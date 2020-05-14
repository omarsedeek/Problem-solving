class Solution:
    '''takes an array of zeros and ones and returt highest number of consecutive ones in the array '''

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        all_counts = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                all_counts.append(count)
                count = 0
        return max(all_counts)
