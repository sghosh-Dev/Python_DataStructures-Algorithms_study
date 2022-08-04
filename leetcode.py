from multiprocessing import dummy


def twoSum(self, nums, target):
        prevmap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff],i]
            prevmap[n] = i
        return

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class solution:
    def addtwonumbers(self, l1:ListNode, l2: ListNode) -> ListNode:

        dummmy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            #get the digits from them as one of them could be null and then wont add
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
        
        #new digit

            val = v1 + v2 + carry
            #if double digit number
            carry = val //10 #gets only the tenths digit to add to the next column
            val = val % 10
            #update pointers
            cur.next = ListNode(val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
