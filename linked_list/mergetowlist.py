from linked_list.linked_list import Node, Linkedlist

def merge(list1,list2):
    current1 = list1.head
    current2 = list2.head
    mergelist = Linkedlist()

    if list1 == None:
        return list2
    if list2 ==None:
        return list1

    while current1 or current2:
        if current1:
            mergelist.appen(current1.data)
            current1 = current1.next
        elif current2:
            mergelist.appen(current2.data)
            current2 = current2.next

    return mergelist