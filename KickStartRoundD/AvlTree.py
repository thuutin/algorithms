class Node:
    def __init__(self, parent):
        self.val = None
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 0

    def is_balanced(self):
        return abs(self.left.height() - self.right.height()) <= 1

    def insert(self, val):
        if val < self.val:
            self.height += 1
            if self.left is None:
                self.left = Node(self)
                self.left.val = val
                self.fix_it()
            else:
                self.left.insert(val)
        else:
            self.height += 1
            if self.right is None:
                self.right = Node(self)
                self.right.val = val
                self.fix_it()
            else:
                self.right.insert(val)

    def fix_it(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        heavy = left_height - right_height
        p = self.parent
        if abs(heavy) > 1:
            if heavy == 2:
                if self.left.get_heavy() == -1:
                    self.left.left_rotate()
                    self.right_rotate()
                else:
                    self.right_rotate()

            if heavy == -2:
                if self.right.get_heavy() == 1:
                    self.right.right_rotate()
                    self.left_rotate()
                else:
                    self.left_rotate()

        if p is not None:
            p.fix_it()

    def get_heavy(self):
        if self.left is None and self.right is None:
            return 0
        if self.left is None:
            return -1
        if self.right is None:
            return 1
        return self.left.height - self.right.height

    def left_rotate(self):
        if self.right is None:
            raise Exception()

        if self.parent is not None:
            if self.parent.left == self:
                self.parent.left = self.right
            if self.parent.right == self:
                self.parent.right = self.right
        r = self.right

        self.right.parent = self.parent
        if self.right.left is not None:
            self.right.left.parent = self
        self.right = self.right.left
        r.left = self
        self.parent = r

        self.update_height()
        r.update_height()
        pass

    def update_height(self):
        if self.left is None and self.right is None:
            self.height = 0
        elif self.left is None or self.right is None:
            self.height = 1
        else:
            self.height = 1 + max(self.left.height, self.right.height)

    def right_rotate(self):
        if self.left is None:
            raise Exception()
        if self.parent is not None:
            if self.parent.right == self:
                self.parent.right = self.left
            if self.parent.left == self:
                self.parent.left = self.left

        l = self.left

        self.left.parent = self.parent
        if self.left.right is not None:
            self.left.right.parent = self
        self.left = self.left.right
        l.right = self
        self.parent = l

        self.update_height()
        l.update_height()
        pass

    def pr(self):
        p = [self]
        while len(p) > 0:
            all = p[:]
            p = []
            for a in all:
                if a.left is not None:
                    p.append(a.left)
                if a.right is not None:
                    p.append(a.right)
                print a.val,
            print




    def __str__(self):
        return str(self.val)

    def find_root(self):
        c = self
        while c.parent is not None:
            c = c.parent
        return c


class AvlTree:
    def __init__(self, rootval):
        self.root = Node(None)
        self.root.val = rootval

    def is_balanced(self):
        return self.root.is_balanced()

    def insert(self, val):
        self.root.insert(val)
        self.root = self.root.find_root()

    def delete(self):
        raise NotImplementedError()

    def pr(self):
        self.root.pr()

t = AvlTree(0)
t.insert(10)
t.insert(15)
t.insert(20)
t.insert(67)
t.insert(19)
t.insert(1)
t.insert(-1)
t.insert(14)
t.insert(-2)

print t.root
t.pr()
