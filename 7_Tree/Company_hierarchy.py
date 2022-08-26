class TreeNode:
    def __init__(self, data, designation):
        self.data = data
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, property_name):

        if property_name == 'both':
            value = self.data + " (" + self.designation + ")"
        elif property_name == 'name':
            value = self.data
        else:
            value = self.designation

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)

    def insertChildNode(self, child):
        child.parent = self
        self.children.append(child)


def built_product_tree():

    Sales = TreeNode("Mitch", "VP Sales")
    Finance = TreeNode("Raj", "VP Finance")
    HR = TreeNode("Kiri", "HR")
    HR.insertChildNode(TreeNode("Teresa", "Front Desk Associate"))

    CTO = TreeNode("Kestas", "CTO")
    CTO.insertChildNode(TreeNode("SAM", "IT Support"))

    CEO = TreeNode("Steve", "CEO")
    CEO.insertChildNode(Sales)
    CEO.insertChildNode(Finance)
    CEO.insertChildNode(HR)
    CEO.insertChildNode(CTO)

    return CEO


if __name__ == '__main__':
    root_node = built_product_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")
