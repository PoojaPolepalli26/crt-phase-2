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
def insertatspecificposition(head, position, ele):
    if position == 0:
        return insertathead(head, ele)
 
    temp = node(ele)
    index = 0 
    currentnode = head 
 
    while index != position - 1:
        currentnode = currentnode.next 
        index += 1 
 
     
    temp.next =currentnode.next   
    currentnode.next = temp 
    return head
nums=[71,72,73,74,75,76,77,78,79,80]
head = None 
for ele in nums:
    head = listtail(head, ele)
print("Final linked list is:")
linkedlist(head)
 
head =insertatspecificposition(head, 3, 68)
linkedlist(head)
        
'''obj1=node(71)
obj2=node(72)
obj3=node(73)
obj4=node(74)
obj5=node(75)
obj6=node(76)
obj7=node(77)
obj8=node(78)
obj9=node(79)
obj10=node(80)
obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj5.next=obj6
obj6.next=obj7
obj7.next=obj8
obj8.next=obj9
obj9.next=obj10'''

    


