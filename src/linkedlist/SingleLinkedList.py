# -*- coding: utf-8 -*-
class SingleLinkedNode(object):
    def __init__(self):
        self.value = None
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def append_node_to_tail(self, value):
        """
        Append the node to the LinkedList tail
        :param value:
        """
        if self.head is None:
            self.head = SingleLinkedNode()

        node = self.head
        while node.next:
            node = node.next

        new_node = SingleLinkedNode()
        new_node.value = value
        node.next = new_node

    def find_node(self, value):
        """
        Find the target node by value
        :param value:
        :return: the target value if found, none otherwise
        """
        if self.head is None: return None
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

        return None

    def delete_node(self, value):
        """
        Delete the node by value
        :param value:
        """
        if self.head is None: return
        node = self.head
        while node.next and node.next.value != value:
            node = node.next

        node.next = node.next.next if node.next else None


    def traversal_list(self):
        """
        Traversal the whole list, and print nodes
        """
        if self.head is None: return

        node = self.head
        node = node.next
        while node:
            print(node.value)
            node = node.next


    def clear_list(self):
        """
        Clear the whole linkedList
        """
        self.head = None

    def has_cycle(self):
        """
        Determine if the LinkedList has cycle
        :return: true if has, false otherwise
        """
        if self.head is None: return True

        walker = self.head
        runner = self.head
        while walker and runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner: return True

        return False


if __name__ == '__main__':
    single_linkedlist = SingleLinkedList()
    single_linkedlist.append_node_to_tail(1)
    single_linkedlist.traversal_list()

    # find_hc_node = single_linkedlist.find_node(1)
    # if find_hc_node is not None:
    #     print find_hc_node.value
    # find_fc_node = single_linkedlist.find_node(2)
    # if find_fc_node is None:
    #     print("find fail case passed")
    # print "*" * 10
    # single_linkedlist.delete_node(1)
    # single_linkedlist.traversal_list()
    # print "*" * 10
    # single_linkedlist.append_node_to_tail(2)
    # single_linkedlist.traversal_list()

