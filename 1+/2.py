# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val == [0]:
            return liToNum(l2)
        elif l2.val == [0]:
            return liToNum(l1)
        else:
            return numToLi(liToNum(l1) + liToNum(l2))

        
def liToNum(l):
    currentNode = l
    depth = 0
    num = 0
    contin = True
    while contin == True:
        num += (currentNode.val * (10**depth))
        depth += 1
        if currentNode.next == None:
            contin = False
        currentNode = currentNode.next
    return num
        
def numToLi(num):
    num = str(num)[::-1] #flips the number and turns it into a string
    FirstNode = ListNode(int(num[0]))
    LastNode = FirstNode
    for digit in num[1:]:
        LastNode.next = ListNode(int(digit))
        LastNode = LastNode.next
    return FirstNode
    