class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        distinct_values = []
        freq=[]

        for num in nums:
            if num not in distinct_values:
                distinct_values.append(num)
                freq.append(1)
            else:
                idx = distinct_values.index(num)
                freq[idx] += 1
        count = 0
        n = len(distinct_values)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range (j + 1, n):
                    count +=freq[i] * freq[j]
                    
        return count
        