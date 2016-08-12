# 基于这样两个事实, 可以保证一定有合法解
# 1. sum(gas) >= sum(cost)
# 2. 从i出发, 按照顺时针走, 能保证到达第一个station
# 解释: 第一个条件很简单, 如果所有的汽油不能小于消耗, 肯定不能走完路程; 第二个条件是, 现在假设从第i个station出发, 可以走到第1个station, 那个之后的2, 3, ..., i - 2, i - 1能不能到达呢? 其实是能的. 我们反过来考虑, 如果能到达station i - 2, 那么能不能到达i - 1呢? 这是肯定的, 因为如果i - 2是一个消耗型的station, 那么i - 2station本身的gas不足以提供足够的cost, 那么为了保证条件一, 到达i时还有剩下的gas, 在i - 2处, 一定是有没有用完的gas, 加上gas[i - 2] > cost[i - 2], 才能保证条件1. 如果能自给自足, 那么也能到达i - 1. 因此, 按照这个思路, 逆推就可以了, 一定可以到达2.
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_gas < total_cost:
            return -1
        ans = 0
        count = 0
        for i in range(len(gas)):
            if count + gas[i] < cost[i]:
                ans = i + 1
                count = 0
            else:
                count = count + gas[i] - cost[i]
        if ans == len(gas):
            return -1
        else:
            return ans
