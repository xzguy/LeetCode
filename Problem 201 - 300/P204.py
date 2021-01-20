import sys
sys.path.append('c:\\Users\\ShenChen\\Desktop\\Python_projects\\LeetCode')
import function_exec_time_compare as fetc

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        if n == 3:
            return 1
        prime = [2]
        for i in range(3, n, 2):
            is_prime = True
            for j in range(len(prime)):
                if prime[j]**2 > i:
                    break
                if i % prime[j] == 0:
                    is_prime = False
                    break
            if is_prime:
                prime.append(i)
        return len(prime)

    '''
    Another way: instead of searching for primes,
    remove all non-primes
    '''
    def countPrimes_1(self, n: int) -> int:
        if n <= 2:
            return 0
        # prime_list[X] is true if number X is a prime number 
        prime_list = [True] * n
        prime_list[0] = prime_list[1] = False
        for i in range(2, n):
            if prime_list[i]:
                for j in range(i**2, n, i):
                    prime_list[j] = False
        return sum(prime_list)

sol = Solution()
print(sol.countPrimes_1(100))

# remove non-prime is about 10 times faster than first one
fetc.compare_function_exec_time(100000, None, 1, \
    [sol.countPrimes, sol.countPrimes_1], \
    ["calculate prime method", "remove non-prime method"])