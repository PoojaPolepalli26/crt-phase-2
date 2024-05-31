class node:
    def __init__ (self,data):
        self.data=data
        self.next=None
def linkedlist(head):
    new_data=head
    while new_data!=None:
        print(new_data.data,end="--> ")
        new_data=new_data.next
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
def insertathead(head,ele):
    temp=node(ele)
    temp.next=head
    return temp
def insertposition)head,position,ele):
    if position==0:
        return(list

nums=[71,72,73,74,75,76,77,78,79,80]
head=None
for ele in nums:
    head=insertathead(head,ele)
    linkedlist(head)

linkedlist(head)
