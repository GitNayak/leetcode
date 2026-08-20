class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        
        # First element goes to arr1
        arr1 = [nums[0]]

        # Second element goes to arr2
        arr2 = [nums[1]]

        # Process remaining elements
        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1 + arr2