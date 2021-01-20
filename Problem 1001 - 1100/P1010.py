import collections

class Solution:
    def numPairsDivisibleBy60(self, time: [int]) -> int:
        pairs = 0
        for i in range(len(time)-1):
            for j in range(i+1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    pairs += 1
        return pairs

    def numPairsDivisibleBy60_1(self, time: [int]) -> int:
        divisible60 = collections.defaultdict(int)
        for t in time:
            divisible60[t%60] += 1
        pairs = 0
        # residule == 0
        pairs += divisible60[0] * (divisible60[0]-1) // 2
        # residule from 1 to 29, and from 31 to 59
        for i in range(1, 30):
            pairs += divisible60[i] * divisible60[60-i]
        # residule == 30
        pairs += divisible60[30] * (divisible60[30]-1) // 2
        return pairs