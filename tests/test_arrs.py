import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 5, "word", 3, "some text"], 2, "test"), "word")
        self.assertEqual(arrs.get([57, 45, 84, "cat", "dog"], 7, "test"), "test")

    def test_my_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([51, 7, "cat", "dog", 95, 45, "horse", 3], 2, 2), [])
        self.assertEqual(arrs.my_slice([41, 27, 3, 17, "frog", 8, "some text", True, 56], 4, None), ["frog", 8, "some text", True, 56])
        self.assertEqual(arrs.my_slice([7, 62, 5, 4, 15, 74], 1, 5), [62, 5, 4, 15])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], None, 5), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([], None, 5), [])

