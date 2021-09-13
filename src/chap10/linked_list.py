from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class ListNode(Generic[T]):
    def __init__(self, key: T) -> None:
        self.key = key
        self.prev: Optional[ListNode] = None
        self.next: Optional[ListNode] = None


class LinkedList(Generic[T]):
    def __init__(self, key=None) -> None:
        self.head: Optional[ListNode] = None
        self.size = 0
        self.key = key

    def search(self, key: T) -> Optional[ListNode]:
        x = self.head
        while x != None and x.key != key:
            x = x.next
        return x

    def insert(self, x: ListNode) -> None:
        self.size += 1
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def delete(self, x: ListNode) -> None:
        self.size -= 1
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev
    def is_empty(self)->bool:
        return self.size == 0
