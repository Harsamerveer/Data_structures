class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def insertChildNode(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        formatting = '|__' if self.parent else ""
        print(spaces + formatting + self.data)
        if len(self.children):
            for child in self.children:
                child.print_tree()


def built_product_tree():
    root = TreeNode("Products")

    Laptops = TreeNode("Laptops")
    Laptops.insertChildNode(TreeNode("Mac"))
    Laptops.insertChildNode(TreeNode("Surface"))
    Laptops.insertChildNode(TreeNode("Think-pad"))

    Fruits = TreeNode("Fruits")
    Fruits.insertChildNode(TreeNode("Apple"))
    Fruits.insertChildNode(TreeNode("Orange"))
    Fruits.insertChildNode(TreeNode("Mango"))

    root.insertChildNode(Laptops)

    root.insertChildNode(Fruits)

    root.print_tree()


if __name__ == '__main__':
    built_product_tree()

