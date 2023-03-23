"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue

class TestQueue(unittest.TestCase):
    def test_queue(self):
        item = Queue()
        self.assertEqual(item.head, None)
        self.assertEqual(item.tail, None)

    def test_enqueue(self):
        item = Queue()
        item.enqueue('data')
        self.assertEqual(self.head, 'data')
        self.assertEqual(self.tail, 'data')


    def test__str__(self):
        pass