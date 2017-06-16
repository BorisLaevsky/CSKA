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
        next_level = []
        if len(self.__list_of_children) < self.__number_of_children:
            self.__list_of_children.append(Child(value_to_insert, number_of_children, None, []))
            self.__list_of_children[-1].__parent = self
            return True
        else:
            for child in self.__list_of_children:
                if len(child.__list_of_children) < child.__number_of_children:
                    return child.insert(value_to_insert, number_of_children)
                else:
                    next_level.append(child)
            for child in next_level:
                insert_success = child.insert(value_to_insert, number_of_children)
                if insert_success:
                    return insert_success


    def depth_first_search(self, value_to_find):
        if self.__value == value_to_find:
            return self
        elif self.__list_of_children:
            for child in self.__list_of_children:
                found_value = child.depth_first_search(value_to_find)
                if isinstance(found_value, Child) and found_value.__value == value_to_find:
                    return found_value

    def breadth_first_search(self, value_to_find):
        explored = Child(None, None, None, [])
        if self.__value == value_to_find:
            return self
        elif self.__list_of_children:
            for child in self.__list_of_children:
                if child.__value == value_to_find:
                    return child
                else:
                    explored.__list_of_children += child.__list_of_children
            return explored.breadth_first_search(value_to_find)

root = Child(1,3)
root.insert(2,3)
root.insert(3,3)
root.insert(4,3)
root.insert(5,3)
root.insert(6,3)
root.insert(7,3)
root.insert(8,3)
root.insert(9,3)
root.insert(10,3)
root.insert(11,3)
root.insert(12,3)
root.insert(13,3)
root.insert(14,3)
root.insert(15,3)
print root.breadth_first_search(15)
print root.get_kth_child(1).get_kth_child(1).get_kth_child(2)
