class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        fuel = start = 0
        
        for i, (g, c) in enumerate(zip(gas, cost)):
            fuel += g - c
            if fuel < 0:
                start = i + 1
                fuel = 0
                
        return start