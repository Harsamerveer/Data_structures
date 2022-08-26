class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_oder_traversal(self):

        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_oder_traversal()

        if self.right:
            elements += self.right.pre_oder_traversal()

        return elements

    def calculate_sum(self, elements):

        sum = 0

        for i in range(0, len(elements)):
            sum += elements[i]

        return sum

    def find_min(self):

        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):

        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete_value(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_value(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_value(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_value(max_val)

        return self


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list Left-Root-Right:", numbers_tree.in_order_traversal())
    print("Post order traversal gives this sorted list Left-Right-Root:", numbers_tree.post_order_traversal())
    print("Pre order traversal gives this sorted list Root-Left-Right:", numbers_tree.pre_oder_traversal())
    print("Sum:", numbers_tree.calculate_sum(numbers_tree.in_order_traversal()))
    print("Find min: ", numbers_tree.find_min())
    print("Find max: ", numbers_tree.find_max())

    numbers_tree.delete_value(20)
    print("After deleting 20 ", numbers_tree.in_order_traversal())

    numbers_tree.delete_value(9)
    print("After deleting 9 ", numbers_tree.in_order_traversal())

    numbers_tree.delete_value(17)
    print("After deleting 17 ", numbers_tree.in_order_traversal())