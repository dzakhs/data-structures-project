"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList, Node
class TestLinkedlist(unittest.TestCase):
    def test_insert_beginning_1(self):
        ll = LinkedList()
        ll.insert_beginning({"id" : 1})
        self.assertEqual(ll.head.data, {"id" : 1})
        self.assertEqual(ll.end.data, {"id": 1})

    def test_insert_beginning_2(self):
        ll = LinkedList()
        ll.insert_beginning({"id" : 1})
        ll.insert_beginning({"id": 2})
        self.assertEqual(ll.head.data, {"id" : 2})
        self.assertEqual(ll.end.data, {"id": 1})

    def test_insert_at_end_1(self):
        ll = LinkedList()
        ll.insert_at_end({"id" : 1})
        self.assertEqual(ll.head.data, {"id": 1})
        self.assertEqual(ll.end.data, {"id": 1})

    def test_insert_at_end_2(self):
        ll = LinkedList()
        ll.insert_at_end({"id" : 1})
        ll.insert_at_end({"id": 2})
        self.assertEqual(ll.head.data, {"id": 1})
        self.assertEqual(ll.end.data, {"id": 2})

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({"id" : 1})
        ll.insert_at_end({"id" : 2})
        data = ll.to_list()
        self.assertEqual(data, [{"id" : 1}, {"id" : 2}])


    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({"id": 1})
        ll.insert_at_end({"id": 2})
        result = ll.get_data_by_id(1)
        self.assertEqual(result, {"id": 1})


class TestNode(unittest.TestCase):
    def test_init(self):
        item = Node(data=None, next_node=None)
        self.assertIsNone(item.data)
        self.assertIsNone(item.next_node)
