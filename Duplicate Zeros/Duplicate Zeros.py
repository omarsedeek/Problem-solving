from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr_length = len(arr)
        arr2 = arr.copy()
        counter = 0
        for i in range(len(arr2)):
            if arr2[i] == 0:
                arr.insert(i+counter,0)
                arr.pop()
                counter +=1
        arr = arr[:arr_length]
        return print(arr)
