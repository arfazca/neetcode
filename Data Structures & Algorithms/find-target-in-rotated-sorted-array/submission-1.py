class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for target value in a rotated sorted array using binary search.
        This simplified version compares with the rightmost element to determine
        which portion of the array to search.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            nums (List[int]): Rotated sorted array
            target (int): Value to find
            
        Returns:
            int: Index of target if found, -1 otherwise
            
        Example:
            >>> solution = Solution()
            >>> solution.search([4,5,6,7,0,1,2], 0)
            4
        """
        L, R = 0, len(nums) - 1
        
        while L <= R:
            M = L + ((R - L) // 2)
            if nums[M] == target:
                return M
                
            # If right portion is sorted
            if nums[M] <= nums[R]:
                # Check if target is in right sorted portion
                if nums[M] <= target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1
            # If left portion is sorted
            else:
                # Check if target is in left sorted portion
                if nums[L] <= target <= nums[M]:
                    R = M - 1
                else:
                    L = M + 1
        
        return -1