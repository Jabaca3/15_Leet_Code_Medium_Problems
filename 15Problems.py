'''
Created on Dec 6, 2018

@author: josephbaca

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# Problem 1
def rangeSumBST(self, root, L, R):

        return self.accumulate(root, 0, L, R)
            
def accumulate(self, root, sum, L, R):
    
    if root is not None:
        sum = self.accumulate(root.left, sum, L, R)
        
        if root.val >= L and root.val <= R:
            sum += root.val
            
        sum = self.accumulate(root.right, sum, L, R)
    
    return sum

# Problem 2
def maxIncreaseKeepingSkyline(self, grid):
            
        rowMax = [0] * len(grid)
        colMax = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rowMax[i] = max(rowMax[i], grid[i][j])
                colMax[j] = max(colMax[j], grid[i][j])

        incramenting = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                incramenting += min(rowMax[i], colMax[j]) - grid[i][j]

        return incramenting
    
# Problem 3
# Unsolved

# Problem 4
def constructMaximumBinaryTree(self, nums):
    if not nums:
        return 

    val = max(nums)
    node = TreeNode(val)

    index = nums.index(val)
    
    node.left = self.constructMaximumBinaryTree(nums[:index])
    node.right = self.constructMaximumBinaryTree(nums[index+1:])
    
    return node


# Problem 5
def insertIntoBST(self, root, val):
    
    if root is None: 
        return TreeNode(val);
    
    if root.val < val: 
        root.right = self.insertIntoBST(root.right, val);
        
    else: root.left = self.insertIntoBST(root.left, val);
        
    return(root)

# Problem 6
# Unsolved

# Problem 7
def minAddToMakeValid(self, S):
        stack = []
        for char in S:
            if char == "(":
                stack.append(char)
            else:
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(char)
        return len(stack)
    
# Problem 8
def pruneTree(self, root):
        
        if root == None: 
            return root;
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if(root.val == 0 and (root.left == None and root.right == None)): 
            return None;
        return root
    
# Problem 9
def findDuplicates(self, nums):
        
        output = []
        mySet = set()
        
        for num in nums:
            if num not in mySet:
                mySet.add(num)
            else:
                output.append(num)
                
        return output
    
# Problem 10    
def findPoisonedDuration(self, timeSeries, duration):
        
        result = 0
        
        for i in range(len(timeSeries) - 1):
            result += min(duration, timeSeries[i+1] - timeSeries[i])
            
        return result + duration if timeSeries else 0
    
# Problem 11
# Unsolved

# Problem 12
def frequencySort(self, s):

        CharMap = {}
        SortedByFrequency = ""
        for i in s:
            if i in CharMap.keys():
                CharMap[i] += 1
            else:
                CharMap[i] = 1
        for key, value in [(k,CharMap[k]) for k in sorted(CharMap, key = CharMap.get, reverse=True)]:
            for i in range (0, value):
                SortedByFrequency += key
        return SortedByFrequency


# Problem 13
def singleNonDuplicate(self, nums):

        mySet = set()
        
        for num in nums:
            if num in mySet:
                mySet.remove(num)
            else:
                mySet.add(num)
                
        for num in mySet:
            return num
        
# Problem 14
def findDuplicate(self, nums):
        mySet = set()
        
        for num in nums:
            if num in mySet:
                return num
            else:
                mySet.add(num)

# Problem 15
def minDistance(self, word1, word2):
    
        w1, w2 = len(word1)+1, len(word2)+1
        dp = [[0 for _ in range(w2)] for _ in range(w1)]
        
        for i in range(w1):
            dp[i][0] = i
        for j in range(w2):
            dp[0][j] = j
            
        for i in range(1, w1):
            for j in range(1, w2):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(word1[i-1]!=word2[j-1]))
                
        return dp[-1][-1]


    
    
    
        