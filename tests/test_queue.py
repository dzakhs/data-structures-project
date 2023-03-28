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
        self.assertEqual(item.head.data, 'data')
        self.assertEqual(item.tail.data, 'data')

    def test_dequeue(self):
        item =Queue()
        item.enqueue('data1')
        item.enqueue('data2')
        self.assertEqual(item.dequeue(), 'data1')
        item.dequeue()
        self.assertIsNone(item.dequeue())


    def test__str__(self):
        item = Queue()
        item.enqueue('data1')
        item.enqueue('data2')
        self.assertEqual(str(item), "data1\ndata2")