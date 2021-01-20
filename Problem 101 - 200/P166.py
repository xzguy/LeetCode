class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        split1 = version1.split(".")
        split2 = version2.split(".")

        i = 0
        while i < min(len(split1), len(split2)):
            if int(split1[i]) > int(split2[i]):
                return 1
            if int(split1[i]) < int(split2[i]):
                return -1
            i += 1
        
        if i < len(split1):
            for j in range(len(split2), len(split1)):
                if int(split1[j]) > 0:
                    return 1
        else:
            for j in range(len(split1), len(split2)):
                if int(split2[j]) > 0:
                    return -1
        return 0

version1 = "1.01"
version2 = "1.001"

version1 = "1.0"
version2 = "1.0.0"

version1 = "0.1"
version2 = "1.1"

version1 = "1.0.1"
version2 = "1"

version1 = "7.5.2.4"
version2 = "7.5.3"

sol = Solution()
print(sol.compareVersion(version1, version2))
