from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(list, Generic[T]):
    def __init__(self, size: int) -> None:
        super().__init__([None] * (size + 1))
        self.size = size
        self.head = 0
        self.tail = 0

    def enqueue(self, x: T) -> None:
        if self.is_full() == True:
            raise ValueError("Queue is full")
        self[self.tail] = x
        if self.tail == self.size:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self) -> T:
        if self.is_empty() == True:
            raise ValueError("Queue is empty")
        x = self[self.head]
        if self.head == self.size:
            self.head = 0
        else:
            self.head += 1
        return x

    def is_empty(self) -> bool:
        return self.tail == self.head

    def is_full(self) -> bool:
        if self.head == 0 and self.tail == self.size:
            return True
        elif self.tail + 1 == self.head:
            return True
        return False
