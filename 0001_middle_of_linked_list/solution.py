from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val 
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = ListNode(data)
        if self.head == None:
            self.head = new_node 
            return 
        last_node = self.head 
        while last_node.next:
            last_node = last_node.next 
        last_node.next = new_node
        
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print("None")



class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        temp_head = head
        while temp_head.next != None:
            length += 1
            temp_head = temp_head.next
        middle_index = int(length/2)
        middle = head 
        for i in range(middle_index):
            middle = middle.next 
        
        return middle


if __name__ == "__main__":
    solution = Solution()

    test_1 = LinkedList() 
    for i in [1,2,3,4,5]:
        test_1.add_node(i)
    assert solution.middleNode(test_1.head).val == 3
    test_1.print_list()

    test_2 = LinkedList()
    for i in [1,2,3,4,5,6]:
        test_2.add_node(i)
    assert solution.middleNode(test_2.head).val == 4 
    test_2.print_list()
