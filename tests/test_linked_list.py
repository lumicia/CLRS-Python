from src.chap10.linked_list import LinkedList, ListNode


def test_empty_linked_list():
    l1 = LinkedList()
    assert l1.is_empty() == True


def test_linked_list_insert():
    l = LinkedList()
    n1 = ListNode(10)
    n2 = ListNode(5)
    n3 = ListNode(8)
    l.insert(n1)
    l.insert(n2)
    l.insert(n3)
    a = []
    x = l.head
    while x:
        a.append(x)
        x = x.next
    assert a == [n3, n2, n1]


def test_linked_list_search():
    l = LinkedList()
    n1 = ListNode(10)
    n2 = ListNode(5)
    n3 = ListNode(8)
    l.insert(n1)
    l.insert(n2)
    l.insert(n3)
    assert l.search(5) == n2


def test_linked_list_delete():
    l = LinkedList()
    n1 = ListNode(10)
    n2 = ListNode(5)
    n3 = ListNode(8)
    l.insert(n1)
    l.insert(n2)
    l.insert(n3)
    l.delete(n2)
    a = []
    x = l.head
    while x:
        a.append(x)
        x = x.next
    assert a == [n3, n1]
