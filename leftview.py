class node:
   def __init__(self,data):
       self.data=data
       self.left=None
       self.right=None
def printLeftView(root):
     if root == None:
        return 
     Q = [root]
     result = []
     while len(Q) > 0:
         n = len(Q)
         for i in range(n):   
            # step-1 (Deleting)
             currNode = Q.pop(0)
 
            # step-2 (Appending to result)
             if i == 0:
                 
                 result.append(currNode.data)
 
            # step-3 (Enquing the left child)
             if currNode.left != None:
                 
                 Q.append(currNode.left)
 
            # step-4 (Enquing the right child)
             if currNode.right != None:
                 Q.append(currNode.right)
 
     print("Left view is:", result)
obj1=node(100)
obj2=node(21)
obj3=node(-15)
obj4=node(87)
obj5=node(12)
obj6=node(52)
obj7=node(8)
obj8=node(27)
obj9=node(28)
obj10=node(7)


obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
obj3.right=obj7
obj4.right=obj8
obj5.right=obj9
obj7.left=obj10

printLeftView(obj1) 
 
