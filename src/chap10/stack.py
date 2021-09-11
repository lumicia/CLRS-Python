from typing import Generic, TypeVar


T = TypeVar("T")


class Stack(list, Generic[T]):
    def __init__(self, size: int) -> None:
        super().__init__([None] * size)
        self.top = -1
        self.size = size

    def push(self, x: T) -> None:
        if self.is_full():
            raise ValueError("Stack is full")
        else:
            self.top += 1
            self[self.top] = x

    def pop(self) -> T:
        if self.is_empty():
            raise ValueError("Stack is empty")
        else:
            self.top -= 1
            return self[self.top + 1]

    def is_empty(self) -> bool:
        return self.top == -1

    def is_full(self) -> bool:
        return self.top == self.size - 1
