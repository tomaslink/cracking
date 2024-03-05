import pytest

from algorithmic import llists


def test_linked_list():
    llist = llists.LinkedList()
    assert llist.get_node("a") is None

    items1 = ["a", "b"]
    items2 = ["c", "d", "e", "e"]

    llist = llists.LinkedList(items1)
    assert repr(llist) == "a -> b -> None"

    llist.add_last(items2)
    assert llist.tolist() == items1 + items2

    assert repr(llist.head) == "a"


def test_remove_duplicates():
    items = ["a", "b", "b", "c", "d", "e", "e"]
    llist = llists.LinkedList(items)

    assert llist.tolist() == items

    llists.remove_duplicates(llist)
    assert llist.tolist() == list(dict.fromkeys(items))


def test_kth_to_last():
    items = ["a", "b", "c", "d", "e"]
    llist = llists.LinkedList(items)

    ktolast = llists.kth_to_last(llist, k=1, size=len(items))
    assert ktolast.data == "e"

    ktolast = llists.kth_to_last(llist, k=3, size=len(items))
    assert ktolast.data == "c"

    with pytest.raises(ValueError):
        ktolast = llists.kth_to_last(llist, k=3, size=10)

    ktolast = llists.kth_to_last(llist, k=3)
    assert ktolast.data == "c"

    with pytest.raises(ValueError):
        ktolast = llists.kth_to_last(llist, k=10)


def test_kth_to_last_recursive():
    items = ["a", "b", "c", "d", "e"]
    llist = llists.LinkedList(items)

    ktolast, i = llists.kth_to_last_recursive(llist.head, k=1)
    assert i == len(items)
    assert ktolast.data == "e"

    ktolast, i = llists.kth_to_last_recursive(llist.head, k=3)
    assert i == len(items)
    assert ktolast.data == "c"


def test_delete_node():
    items = ["a", "b", "c", "d", "e"]
    llist = llists.LinkedList(items)

    node = llist.get_node("c")

    llists.delete_middle_node(node)
    assert llist.tolist() == ["a", "b", "d", "e"]

    with pytest.raises(ValueError):
        node = llist.get_node("e")
        llists.delete_middle_node(node)


def test_partition():
    items = [3, 5, 8, 5, 10, 2, 1]
    llist = llists.LinkedList(items)

    llist = llists.partition(llist, x=5)
    output = [1, 2, 3, 5, 8, 5, 10]
    assert llist.tolist() == output

    items = [6, 5, 3, 4, 10, 2, 9]
    llist = llists.LinkedList(items)
    llist = llists.partition(llist, x=5)
    output = [2, 4, 3, 6, 5, 10, 9]
    assert llist.tolist() == output
