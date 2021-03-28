import collections

class Solution:
    # assume the primes is a sorted list
    def nthSuperUglyNumber(self, n: int, primes: [int]) -> int:
        # primes.sort()

        p_len = len(primes)
        ugly_queue = collections.deque([1])
        ugly_idx = 1
        q_dict = {}
        for i in range(p_len):
            q_dict[i] = collections.deque()
        
        while ugly_idx < n:
            # since primes is sorted, we only need to check
            # first prime in the list
            if not q_dict[0]:
                prime_to_time = ugly_queue.popleft()
                for i in range(p_len):
                    q_dict[i].append(prime_to_time * primes[i])
            
            next_ugly = float('inf')
            for i in range(p_len):
                if q_dict[i][0] < next_ugly:
                    next_ugly = q_dict[i][0]

            # remove the next ugly number from the queues
            for i in range(p_len):
                if q_dict[i][0] == next_ugly:
                    q_dict[i].popleft()

            # update ugly number and index
            ugly_queue.append(next_ugly)
            ugly_idx += 1

        return ugly_queue[-1]
            
sol = Solution()
primes = [2, 7, 13, 19]
primes = [3,5,7,11,19,23,29,41,43,47]
print(sol.nthSuperUglyNumber(15, primes))
