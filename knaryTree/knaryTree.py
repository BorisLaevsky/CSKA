class Child:
    def __init__(self, value, number_of_children, parent = None, list_of_children = []):
        self.__value = value
        self.__parent = parent
        self.__number_of_children = number_of_children
        self.__list_of_children = list_of_children

    def __str__(self):
        return str(self.__value)

    def parent(self):
        return self.__parent

    def list_of_children(self):
        return self.__list_of_children

    def get_kth_child(self, number_of_child):
        try:
            return self.__list_of_children[number_of_child - 1]
        except IndexError:
            return "Child does not exist"

    def insert(self, value_to_insert, number_of_children):
        if len(self.__list_of_children) < self.__number_of_children:
            self.__list_of_children.append(Child(value_to_insert, number_of_children, None, []))
            self.__list_of_children[-1].__parent = self
        else:
            for child in self.__list_of_children:
                if len(child.__list_of_children) < child.__number_of_children:
                    child.insert(value_to_insert, number_of_children)
                    break

    def depth_first_search(self, value_to_find):
        if self.__value == value_to_find:
            return self
        elif self.__list_of_children:
            for child in self.__list_of_children:
                found_value = child.depth_first_search(value_to_find)
                if isinstance(found_value, Child) and found_value.__value == value_to_find:
                    return found_value.depth_first_search(value_to_find)


root = Child(1,3)
root.insert(2,3)
root.insert(3,3)
root.insert(4,3)
root.insert(5,3)
root.insert(6,3)
root.insert(7,3)
root.insert(8,3)
print root.depth_first_search(6)
