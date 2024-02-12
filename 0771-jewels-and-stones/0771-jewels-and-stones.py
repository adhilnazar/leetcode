class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # dic = {}
        
        count = 0
        
        for i in jewels:
            for j in stones:
                if i == j:
                    count += 1
                else:
                    pass
        return count
        