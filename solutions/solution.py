class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True  # Duplicate found
            seen.add(num)
        return False  # No duplicates
        
