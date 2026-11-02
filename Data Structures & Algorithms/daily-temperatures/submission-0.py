class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
         # need to find next greatest element index (NGEI)
        # NGEI - current index = # of days you have to wait

        result = [0] * len(temperatures)
        stack = [] # monotonic, non decreasing order, pairs [temp, i]

        for i, temp in enumerate(temperatures):
            # while stack is not empty and curr temp > temp at the top of stack
            while stack and temp > stack[-1][0]: # get top pair, from that pair get element [0]
                prevTemp, prevIndex = stack.pop()
                result[prevIndex] = i - prevIndex
            stack.append([temp, i])
        
        return result
