class Node:

    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def add_to_end(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            self.size += 1
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)
        self.size += 1

    def add_to_head(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        self.size += 1

    def delete_by_value(self, val: int) -> None:
        if self.head.val == val:
            self.head = self.head.next
        
        cur = self.head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                self.size -= 1
            cur = cur.next

    def delete_by_index(self, index: int) -> None:
        if index >= self.size:
            return -1
        cur = self.head
        i = 0
        while i < index - 1:
            cur = cur.next
            i += 1
        if cur.next:
            cur.next = cur.next.next
        self.size -= 1
    

    def remove_dups(self) -> None:
        """ 2.1 remove duplicates from an unsorted linked list """
        vals = set()
        cur = self.head
        while cur.next:
            vals.add(cur.val)
            print("Node: ", cur.val)
            if cur.next.val in vals:
                cur.next = cur.next.next
                self.size -= 1
            if cur.next:
                cur = cur.next

    def print_nodes(self) -> None:
        cur = self.head
        while cur:
            print(cur.val, end='-> ')
            cur = cur.next
        print('None')

    def find_kth_from_tail(self, k: int) -> None:
        index = self.size - k
        if index < 0:
            return None
        self.delete_by_index(index)
        self.size -= 1

    def partition(self, val: int):
        tmp = LinkedList()
        cur = self.head
        while cur:
            if cur.val < val:
                tmp.add_to_head(cur.val)
            else:
                tmp.add_to_end(cur.val)
            cur = cur.next
        self.head = tmp.head

    def sum_lists(self, other: 'LinkedList') -> int:
        cur_str = self._str_total()
        other_str = other._str_total()
        return int(cur_str) + int(other_str)

    
    def _str_total(self) -> str:
        cur = self.head
        res = ''
        while cur:
            res += str(cur.val)
            cur = cur.next
        return res

if __name__ == '__main__':
    llist = LinkedList()
    llist.add_to_end(1)
    llist.add_to_end(5)
    llist.add_to_head(3)
    llist.add_to_head(2)
    llist.add_to_end(7)
    llist.add_to_end(3)
    llist.add_to_head(2)
    llist.print_nodes()

    llist.remove_dups()
    llist.print_nodes()

    llist.delete_by_index(2)
    llist.print_nodes()

    llist.delete_by_value(5)
    llist.print_nodes()

    llist.add_to_head(10)
    llist.add_to_head(5)
    llist.add_to_head(1)
    llist.print_nodes()
    llist.partition(5)
    llist.print_nodes()
    print(llist._str_total())

    llist2 = LinkedList()
    llist2.add_to_end(1)
    llist2.add_to_end(5)
    print(llist.sum_lists(llist2))