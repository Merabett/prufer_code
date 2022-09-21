class Tree:
    def __init__(self, ele=None):
        self.__element = ele
        self.__parent = None
        self.__children = None
        self.__right_sibling = None

    def __str__(self):
        string = '<' + str(self.__element)
        aux = self.leftmost_child()
        while aux is not None:
            string += aux.__str__()
            aux = aux.right_sibling()
        string += '>'
        return string

    def is_empty(self):
        return self.__element is None

    def parent(self):
        return self.__parent

    def element(self):   # New
        return self.__element

    def is_root(self):
        return self.__parent is None

    def leftmost_child(self):
        return self.__children

    def right_sibling(self):
        return self.__right_sibling

    def is_leaf(self):   # New
        return self.__children is None

    def append_child(self, child):
        child.__parent = self
        if self.__children is None:
            self.__children = child
        else:
            tmp = self.__children
            while tmp.right_sibling() is not None:
                tmp = tmp.right_sibling()
            tmp.__right_sibling = child

    def preorder(self, order):
        order.append(self.__element)
        aux = self.__children
        while aux is not None:
            aux.preorder(order)
            aux = aux.right_sibling()
        return order


    def postorder(self, order):
        aux = self.__children
        while aux is not None:
            aux.postorder(order)
            aux = aux.right_sibling()
        order.append(self.__element)
        return order

    def inorder(self, order):
        if self.is_leaf():
            order.append(self.__element)
        else:
            self.leftmost_child().inorder(order)
            order.append(self.__element)
            aux = self.__children.right_sibling()
            while aux is not None:
                aux.inorder(order)
                aux = aux.right_sibling()
        return order
