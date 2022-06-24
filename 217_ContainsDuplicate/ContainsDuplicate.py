#!/usr/bin/env python3

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ret = False if len(nums) == len(set(nums)) else True
        return ret

# All elements are unique if length of nums and length of the set(nums) are equal 
