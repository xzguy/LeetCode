class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        m_2 = 1
        while 2*m_2 <= m:
            m_2 *= 2
        n_2 = 1
        while 2*n_2 <= n:
            n_2 *= 2
        # m_2 <= m < 2*m_2, n_2 <= n < 2*n_2
        if m_2 != n_2:
            return 0
        return m_2 + self.rangeBitwiseAnd(m-m_2, n-m_2)

sol = Solution()
print(sol.rangeBitwiseAnd(1,2))
