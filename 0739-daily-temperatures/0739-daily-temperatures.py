class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[] #pair:[temperature,index]
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stacktem,stackin=stack.pop()
                res[stackin]=i-stackin
            stack.append([t,i])
        return res
                    

        