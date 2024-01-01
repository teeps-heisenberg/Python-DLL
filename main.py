from doubly_linked_list import DoublyLinkedList

my_doubly_linked_list = DoublyLinkedList(6)
my_doubly_linked_list.print_list()
my_doubly_linked_list.append(24)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(37)
my_doubly_linked_list.append(14)
my_doubly_linked_list.print_list()

#Pop
print('Pop Operation Performed:')
my_doubly_linked_list.pop()
my_doubly_linked_list.print_list()

#Prepend
print('Prepend Operation:')
my_doubly_linked_list.prepend(5)
my_doubly_linked_list.print_list()

#Pop First
print('Pop First Operation:')
my_doubly_linked_list.pop_first()
my_doubly_linked_list.print_list()

#Get by Index
print('Get By Index Operation:')
print(my_doubly_linked_list.get(3).value)


#Set Value by Index
print('Set Value By Index Operation:')
my_doubly_linked_list.set_value(2,13)
my_doubly_linked_list.print_list()

#Insert Value by Index
print('Insert Value By Index Operation:')
my_doubly_linked_list.insert(index=1,value=78)
my_doubly_linked_list.print_list()

#Remove Value by Index
print('Remove Value By Index Operation:')
my_doubly_linked_list.remove(2)
my_doubly_linked_list.print_list()