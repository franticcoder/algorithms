# Leetcode : 200. Number of Islands
#
# Author: Chungmin Kim
# Date: May 4, 2019
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> int:
        row = len(grid)
        if row == 0:
            return 0;
        col = len(grid[0])

        cnt = 0

        headGrid = [-1] * (row * col)
        val = 0

        # The basic idea is that while iterating the 2-d lists, check 4 directions(up,right,down,left)
        # and find the smallest head value(cnt) and update the valid elements in 4 directions.
        for r in range(0, row):
            for c in range(0, col):

                minNum = -1
                fourDir = [False] * 4

                if grid[r][c] == "0":
                    cnt += 1
                    continue

                # find the minimum cnt around the current element
                # minNum == -1 -> not found yet
                # val == -1 -> the element is not yet set with the head value
                if r - 1 >= 0 and grid[r-1][c] == "1":                  # up
                    val = headGrid[self.getIndexOfHeadGrid(r-1, c, col)]
                    if minNum == -1 or ( val != -1 and minNum > val):
                        minNum = val
                    fourDir[0] = True
                if c + 1 <= col -1 and grid[r][c+1] == "1":            #right
                    val = headGrid[self.getIndexOfHeadGrid(r , c+1, col)]
                    if minNum == -1 or ( val != -1 and minNum > val):
                        minNum = val
                    fourDir[1] = True
                if r + 1 <= row - 1 and grid[r+1][c] == "1":            #down
                    val = headGrid[self.getIndexOfHeadGrid(r+1 , c, col)]
                    if minNum == -1 or ( val != -1 and minNum > val):
                        minNum = val
                    fourDir[2] = True
                if c - 1 >= 0 and grid[r][c-1] == "1":                  #left
                    val = headGrid[self.getIndexOfHeadGrid(r , c-1, col)]
                    if minNum == -1 or ( val != -1 and minNum > val):
                        minNum = val
                    fourDir[3] = True

                # update the headGrid with the found minNum above.
                cellVal = 0
                if minNum >= 0:
                    if fourDir[0] :
                        cellVal = headGrid[self.getIndexOfHeadGrid(r-1, c, col)]
                        if cellVal != -1 and cellVal != minNum:
                            headGrid[headGrid[self.getIndexOfHeadGrid(r - 1, c, col)]] = minNum

                    if fourDir[1]:
                        cellVal = headGrid[self.getIndexOfHeadGrid(r , c+1, col)]
                        if cellVal != -1 and cellVal != minNum:
                            headGrid[headGrid[self.getIndexOfHeadGrid(r , c+1, col)]] = minNum

                    if fourDir[2]:
                        cellVal = headGrid[self.getIndexOfHeadGrid(r+1 , c, col)]
                        if cellVal != -1 and cellVal != minNum:
                            headGrid[headGrid[self.getIndexOfHeadGrid(r + 1, c, col)]] = minNum

                    if fourDir[3]:
                        cellVal = headGrid[self.getIndexOfHeadGrid(r , c-1, col)]
                        if cellVal != -1 and cellVal != minNum:
                            headGrid[headGrid[self.getIndexOfHeadGrid(r , c-1, col)]] = minNum


                    headGrid[self.getIndexOfHeadGrid(r, c, col)] = minNum
                else:
                    headGrid[self.getIndexOfHeadGrid(r , c, col)] = cnt


                cnt += 1

        # update the change
        cnt = 0
        for i in range(0, row * col):
            if headGrid[i] != -1 and headGrid[i] != cnt:
                headGrid[i] = headGrid[headGrid[i]]
            cnt += 1

        # using set, count the number of values in the list(headGrid)
        # the number of values(except -1) is the number of islands
        mset = set()
        for i in range(0, row * col):
           mset.add( headGrid[i] )
        mset.discard(-1)

        return len(mset)


    def getIndexOfHeadGrid(self, row, col, size):
        return (size * row) + col



grid = [["1","0","1","1","1"],
        ["1","0","1","0","1"],
        ["1","1","1","0","1"]]

grid0 = [["1"]]

sol = Solution()
print(sol.numIslands( grid ))
