from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1
        
        new_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        
        result = []
        for i in new_d:
            result.append(i)
        
        return sorted(result[:k])


        