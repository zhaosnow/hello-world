class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ans = list()
        ans.append(1)
        index = [0] * len(primes)
        for i in range(n - 1):
            mini = min([ans[index[i]] * primes[i] for i in range(len(primes))])
            ans.append(mini)
            for i in range(len(primes)):
                while primes[i] * ans[index[i]] == mini:
                    index[i] += 1
        return ans[-1]
