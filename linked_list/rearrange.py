def rearrange(head):
    elem = []
    i =0
    temp = head
    while temp!=None:
        elem.append(temp.data)
        temp = temp.next
    print(temp)
    
    if len(elem):
        return

    temp = head
    while len(elem)>0:
        if i%2==0:
            temp.data = elem[0]
            elem.pop(0)

        else:
            temp.data = elem[-1]
            elem.pop()
        i+=1
        temp = temp.next

    return head