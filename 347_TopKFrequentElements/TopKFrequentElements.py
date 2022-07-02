import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqDict = collections.defaultdict(int)
        resDict = collections.defaultdict(list)

        for n in nums:
            freqDict[n] += 1
        for n,f in freqDict.items():
            resDict[f].append(n)

        return [y for x in sorted(resDict.keys(),reverse=True) for y in resDict[x]][:k]


# Iterate nums to get frequency of each number. Create mapping of frequency to numbers. Return K most frequent numbers from mapping.
