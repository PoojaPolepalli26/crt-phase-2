class node:
   def __init__(self,data):
       self.data=data
       self.left=None
       self.right=None
def printPostorder(root):
    if root == None:
        return 
    # 1 
    printPostorder(root.left)
    # 2 
    printPostorder(root.right)
    # 3
    print(root.data, end = ", ")
    
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

printPostorder(obj1)
