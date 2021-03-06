class Node:
    """
    DESCRIPTION: To represent the Node entity.
    """

    def __init__(self, data):
        """
        Objective: To initialise the object of class Node.
        Input Parameters:
                    self: Implicit object of class Node.
                    data: Value to be assigned to the data of object.
                    next: It holds the address of the next object.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    DESCRIPTION: To represent the LinkedList.
    """

    def __init__(self):
        """
        Objective: To initialize the object of class LinkedList.
        Input Parameters:
                    self: Implicit object of class LinkedList.
        """
        self.head = None

    def __str__(self):
        """
        Objective: To print all the elements of the linked list
        Input Parameter:
            self: Implicit object of class LinkedList.
        """
        elements = ''
        total = 0
        if self.head is None:
            return "\t\tEmpty List!"
        current = self.head
        while True:
            elements += f'|{current.data}|next|-->'
            total += 1
            current = current.next
            if current is None:
                return f'\t\tTotal node(s): {total} \n\t\tNode(s) in Linked List are:\n\n\t\t{elements}None'

    def add_node(self, data):
        """
        Objective: To add new node at the beginning of the linked list.
        Input Parameters:
                    self: Implicit object of class LinkedList
                    data: Value to be assigned to the object of class Node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def append_node(self, data):
        """
        Objective: To append node at the end of the linked list.
        Input Parameter(s):
                    self: Implicit object of class LinkedList.
                    data: Value to be assigned to the object of class Node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = new_node
                return
            current_node = current_node.next

    def remove_node(self):
        """
        Objective: To remove node from the beginning of the Linked List.
        Input Parameter:
                self: Implicit object of the class LinkedList.
        """
        if self.head is None:
            return '\t\tEmpty List!'
        current = self.head
        self.head = current.next
        return f'\t\tYou have removed: {current.data}'

    def delete_specific_node(self, data):
        if self.head is None:
            return '\t\tEmpty List! '
        if self.head.data == data:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
            return f'\t\tYou have deleted: {data}'
        current_node = self.head
        while True:
            prev_node = current_node
            current_node = current_node.next
            if current_node is None:
                return f'\t\tNode with value: {data} not found!'
            if current_node.data == data:
                current_node = current_node.next
                prev_node.next = current_node
                return f'\t\tYou have deleted: {data}'


def main():
    linkedlist = LinkedList()
    while True:
        print("\n\t", "==" * 20, "Linked List", "==" * 20)
        print("""\t\t1. Add new node at the beginning of linked list.
                2. Remove the first node of linked list.
                3. Remove a specific node from the linked list.
                4. Display all node(s) of the linked list.
                5. Exit """)
        print("\t", "==" * 20, "Linked List", "==" * 20)
        user_choice = input("\t\tEnter your choice: ")
        if user_choice == '1':
            data = int(input("\t\tEnter any integer number: "))
            linkedlist.add_node(data)
        elif user_choice == '2':
            print(linkedlist.remove_node())
        elif user_choice == '3':
            data = int(input("\t\tEnter the element to be deleted: "))
            print(linkedlist.delete_specific_node(data))
        elif user_choice == '4':
            print(linkedlist)
        elif user_choice == '5':
            return
        else:
            print("\t\tWrong Choice! Try again....")


if __name__ == '__main__':
    main()
