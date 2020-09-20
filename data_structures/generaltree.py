class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def find_level(self):
        level = 0
        p = self
        while p.parent != None:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.find_level() * 2
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.value)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("Samsung"))
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("OnePlus"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Samsung"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
