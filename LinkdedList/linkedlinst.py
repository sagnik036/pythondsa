"""linkded list"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def takeInput():
    inputList=[int(i) for i in input().split(' ')]
    head = None

    for i in inputList:
        if i == -1:
            break
        newData = Node(i)
        if head is None:
            head = newData
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newData
    return head

def printLL(head):
    while head is not None:
        print(head.data,"->",end=" ")
        head = head.next
    print("None")
    return

L = takeInput()
P = printLL(L)
    
        