# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 == [0]:
            return liToNum(l2)
        elif l2 == [0]:
            return liToNum(l1)
        else:
            return liToNum(l1) + liToNum(l2)

        
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
    num = str(num)
    FirstNode = ListNode(num[0])
    LastNode = FirstNode
    for digit in range(len(num)):
        if digit == 0:
            continue
        else:         
            LastNode.next = ListNode(digit)
            LastNode = LastNode.next
    return FirstNode

three = ListNode(3)
four = ListNode(4,three)
two = ListNode(2,four)

print(liToNum(two))


