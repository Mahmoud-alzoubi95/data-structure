class Node:
  def __init__(self,data):
    self.data=data
    self.next=None 

class Linkedlist:
  def __init__(self):
    self.head=None 

  def appen(self,data):
    new_node = Node(data)
    if self.head:
      new_node.next = self.head
    self.head = new_node

  def deletenode(self,value):
    current = self.head
    if self.head.data == value:
      self.head = self.head.next

    else:
      while current.next.data != value:
        current = current.next
      current.next = current.next.next

  def reversing(self):
    rev_data = []
    current = self.head
    while current:
      rev_data.append(current.data)
      temp = current.next
      self.deletenode(current.data)
      current = temp

    for i in rev_data:
      self.appen(i)


  def rearrange(self,head):
      elem = []
      i =0
      temp = self.head

      while temp!=None:
          elem.append(temp.data)
          temp = temp.next
      print(temp)
      
      if len(elem):
          return

      temp = self.head
      while len(elem)>0:
          if i%2==0:
              temp.data = elem[0]
              elem.pop(0)

          else:
              temp.data = elem[-1]
              elem.pop()
          i+=1
          temp = temp.next


  def __str__(self):
    current= self.head
    list=""
    while current:
      list +="{%s} -> "%current.data
      current=current.next
    list+="Null"
    return list

if __name__=="__main__":
  L = Linkedlist()
  L.appen("alzoubi")
  L.appen("Hasan")
  L.appen("mahmoud")
  # print(L)
  # L.reversing()
  # print(L)
  # L.deletenode("Hasan")
  # print(L)

  M = Linkedlist()
  M.appen("6")
  M.appen("5")
  M.appen("4")
  M.appen("3")
  M.appen("2")
  M.appen("1")
  M.rearrange(M)
  print(M)
 
