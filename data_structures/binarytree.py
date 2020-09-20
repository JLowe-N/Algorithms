class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values):
        queue = [self]
        while len(queue) > 0 and len(values) > 0:
            current = queue.pop(0)
            if current.left is None and len(values) > 0:
                current.left = BinaryTree(values.pop(0))
                queue.append(current.left)
            if current.right is None and len(values) > 0:
                current.right = BinaryTree(values.pop(0))
                queue.append(current.right)
        return self

    def print_tree(self, level = 0):
        spaces = ' ' * level * 4
        prefix = spaces + '|__' if level > 0 else ''
        print(prefix + str(self.value))
        if self.left:
            self.left.print_tree(level + 1)
        if self.right:
            self.right.print_tree(level + 1)
        

if __name__ == '__main__':
    tree = BinaryTree(1).insert([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

