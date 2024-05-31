class node:
   def __init__(self,data,left=None,right=None):
       self.data=data
       self.left=None
       self.right=None
#class Solution(object):
   def maxLevelSum(self, root):
       if root == None:
          return 0
       Q = [root]
       resultLevel = 0 
       resultSum = -100000000
       currLevel = 1
       while len(Q) > 0:
          n = len(Q)
          currSum = 0
          for i in range(n):
                 # step-1 (Deleting)
               currNode = Q.pop(0)
 
                 # step-2 (Appending to subResult)
               currSum += currNode.val
 
                 # step-3 (Enquing the left child)
               if currNode.left != None:
                    Q.append(currNode.left)
 
                 # step-4 (Enquing the right child)
               if currNode.right != None:
                    Q.append(currNode.right)
 
          if currSum > resultSum:
              resultSum = currSum 
              resultLevel = currLevel 
          currLevel += 1
       print(resultLevel) 
obj1=node(100)
obj2=node(21)
obj3=node(-15)
obj4=node(87)
obj5=node(12)
obj6=node(52)

obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
maxLevelSum(obj1) 
