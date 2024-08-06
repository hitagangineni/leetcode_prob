class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    #TC: O(N) Scan through all the arrays + O(1) for lookup in the hashset
    #SC: O(N) hashset occupies O(N) space as there could be potentially N elements in the hashset 

    #PATTERN:

    #Check for duplicates / any number occuring more than once use a set. 
