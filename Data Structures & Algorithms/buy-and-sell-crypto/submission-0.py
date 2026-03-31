class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 1
        i = 0
        m = 0
        length = len(prices)

        while True:
            if(j == length):
                break
            
            if(prices[i] <= prices[j]):
                sub = prices[i] - prices[j]
                m = min(m, sub)
                j = j+1
            elif(prices[i]> prices[j]):
                i = j
                j = j+1

        return abs(m)
            
            

            
