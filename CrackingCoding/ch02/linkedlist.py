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

    def delete_node(self, val: int) -> Node:
        if self.head.val == val:
            self.head = self.head.next
        
        cur = self.head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                self.size -= 1
                return self.head
            cur = cur.next
        return self.head

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