'''class node:
    def __init__ (self,data):
        self.data=data
        self.next=None
def linkedlist(head):
    currentnode=head
    while currentnode!=None:
        print(currentnode.data,end="--> ")
        currentnode=currentnode.next
    print()
def listtail(head,ele):
    temp=node(ele)
    if head==None:
        return temp
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=temp
    return head
def deletetailnode(head):
    if head==None or head.next==None:
        return None
    previous=None
    currentnode=head
    while currentnode.next !=None:
        previous=currentnode
        currentnode=currentnode.next
    previous.next=None
    return head

nums=[71,72,73,74,75,76,77,78,79,80]

head = None 
for ele in nums:
    head = listtail(head,ele)
    linkedlist(head)
print("Final linked list is:")
linkedlist(head)
deletetailnode(head)
linkedlist(head)'''



#delete a head


class node:
    def __init__ (self,data):
        self.data=data
        self.next=None
def linkedlist(head):
    currentnode=head
    while currentnode!=None:
        print(currentnode.data,end="--> ")
        currentnode=currentnode.next
    print()
def listtail(head,ele):
    temp=node(ele)
    if head==None:
        return temp
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=temp
    return head
def deleteheadnode(head):
    if head==None:
        return head
    secondnode=head.next
    head.next=None
    return secondnode

nums=[71,72,73,74,75,76,77,78,79,80]

head = None 
for ele in nums:
    head = listtail(head,ele)
    linkedlist(head)
print("Final linked list is:")
linkedlist(head)
head = deleteheadnode(head)
linkedlist(head)
