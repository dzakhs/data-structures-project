"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack
class TestStack(unittest.TestCase):
    def test_stack(self):
        item = Stack()
        self.assertEqual(item.top, None)

    def test_push(self):
        item = Stack()
        item.push("data")
        self.assertEqual(item.top.data, "data")


    def test_pop(self):
        item = Stack()
        item.push("data")
        item.pop()
        self.assertEqual(item.top, None)

    def test__str__(self):
        pass