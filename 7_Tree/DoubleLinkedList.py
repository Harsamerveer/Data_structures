
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):

        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.node = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def print_forward(self):

        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        lik = ''
        while itr:
            lik += str(itr.data) + '--->'
            itr = itr.next
        print(lik)


    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += str(itr.data)+ '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr


    def insert_values(self, data_list):
        if self.head is None:
            return
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        if self.head is None:
            return
        itr = self.head
        while itr.next:
            itr = itr.next
            count += 1
        return count

    def remove_element(self, index):
        if index < 0 or index >= self.get_length():
            return Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            return Exception("Invalid Index")

        if self.head is None:
            return None

        #beg
        if index == 0 :
            self.insert_at_begining(data)
            return
        #middle
        #end
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):


    # Search for first occurence of data_after value in linked list
    # Now insert data_to_insert after data_after node

        if self.head is None:
            return None

        count = 0
        itr = self.head
        while itr:

            if data_after == itr.data:
                print(itr.data)
                node = Node(data_to_insert, itr.next)
                itr.next = node

            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return None

        count = 0
        itr = self.head
        print(itr.data)
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1



if __name__ == '__main__':
    LL = LinkedList()
    LL.insert_at_begining(2)
    LL.insert_at_begining(31)
    LL.insert_at_end(23)
    LL.insert_after_value(23,100)
    LL.insert_values([532,57656,1221,67,73])
    LL.remove_by_value(1221)
    LL.print_forward()
    LL.print_backward()
