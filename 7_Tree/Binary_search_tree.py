# At most 2 child nodes
class BinarySearchNode:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchNode(data)

    # In-order of traversal
    def in_order_traversal(self):
        elements = []

        # Visit Left Tree
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit Base Node
        elements.append(self.data)

        # Visit Right Tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, value):
        if value == self.data:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False


def build_tree(elements):
    root = BinarySearchNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 99, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(8))
