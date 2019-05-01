class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]+[0]*rowIndex
        for i in range(rowIndex):
            for j in range(i+1, 0, -1):
                ans[j] = ans[j] + ans[j-1]
                print(i,j,ans)
        return ans
x = Solution()
x.getRow(5)