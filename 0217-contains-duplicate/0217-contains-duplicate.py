class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashTable = set()
        for n in nums:
            if n in hashTable:
                return True
            hashTable.add(n)
        return False