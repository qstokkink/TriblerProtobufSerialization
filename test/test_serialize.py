import struct
import unittest

import messages
from exception import *
from serializer import Serializer

class TestSerialize(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        messages.MESSAGES.append(__import__("test_pb2", globals(), locals(), [], -1))
        self.blank_args = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 0, 0, "a", "b", "c", "d"]
        self.neg_args = [-1.0, 0, -1.0, 0, -1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, "", "", "", ""]
        self.illegal_len_args = [
                                [0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", ""]
                            ]
        self.too_long_args = [
                                [0, 0, 0, 0, 0, 32768, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 32768, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 32768, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32768, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32768, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32768, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32768, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32768, 0, 0, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32768, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32768, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, -32769, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, -32769, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -32769, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -32769, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -32769, 0, 0, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -32769, 0, 0, "", "", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "aaa", "", ""],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", "aaa"]
                            ]

    def setUp(self):
        self.s = Serializer()

    def test_id(self):
        enc = self.s.serialize("Test", *self.blank_args)
        (name, ) = struct.unpack_from('20s', enc)

        self.assertTrue(name.startswith('Test'))

    def test_values(self):
        enc = self.s.serialize("Test", *self.blank_args)

        def f(obj):
            self.assertTrue(obj.IsInitialized())
            for (_, value) in obj.ListFields():
                self.assertIn(value, self.blank_args)

        self.s.add_handler("Test", f)
        self.s.unserialize(enc)

    def test_negative_values(self):
        enc = self.s.serialize("Test", *self.neg_args)

        def f(obj):
            self.assertTrue(obj.IsInitialized())
            for (_, value) in obj.ListFields():
                self.assertIn(value, self.neg_args)

        self.s.add_handler("Test", f)
        self.s.unserialize(enc)

    def test_illegal_length_option(self):
        for args in self.illegal_len_args:
            with self.assertRaises(FieldLengthUnsupportedException):
                self.s.serialize("Test", *args)

    def test_too_long_option(self):
        for args in self.too_long_args:
            with self.assertRaises(FieldTooLongException):
                self.s.serialize("Test", *args)

if __name__ == '__main__':
    unittest.main()
