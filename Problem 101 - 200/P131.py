'''
Seventh problem (131):
    Given a string s, partition s such that every 
substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
'''
def partition(s: str) -> [[str]]:
    def isPalindrome(s: str, low: int, high: int) -> bool:
        while (low < high):
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True
    
    def backtrak(results: [[str]], temp_list: [str], start: int):
        if (start == len(s)):
            results.append(temp_list.copy())
        else:
            for i in range(start, len(s)):
                if isPalindrome(s, start, i):
                    temp_list.append(s[start:i+1])
                    backtrak(results, temp_list, i+1)
                    temp_list.pop()
    
    results_patition = []
    backtrak(results_patition, [], 0)
    return results_patition

input = "cabababcbc"
print(partition(input))