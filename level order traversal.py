class node:
   def __init__(self,data):
       self.data=data
       self.left=None
       self.right=None
def printlevelordertraversal(root):
    if root==None:
        return
    q=[root]
    result=[]
    while len(q)>0:
        n=len(q)
        subresult=[]
        for i in range(n):
            currNode=q.pop(0)
            subresult.append(currNode.data)
            if currNode.left !=None:
                q.append(currNode.left)
            if currNode.right !=None:
                q.append(currNode.right)
        result.append(subresult)
    print(result)
    
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

printlevelordertraversal(obj1)
