import logging
import struct
import unittest

import messages
from exception import *
from serializer import Serializer

class TestSerialize(unittest.TestCase):

    @classmethod
    def _clearMsgDefs(self):
        # Clear all non-test messages
        try:
            while True:
                messages.MESSAGES.pop()
        except IndexError:
            pass

    @classmethod
    def setUpClass(self):
        self._clearMsgDefs()
        messages.MESSAGES.append(__import__("test_pb2", globals(), locals(), [], -1))
        self.blank_args = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, True, 0, "a", "b", "c", "d"]
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

        self.assertTrue(name.startswith('test_pb2Test'))

    def test_values(self):
        enc = self.s.serialize("Test", *self.blank_args)

        def f(obj):
            self.assertTrue(obj.IsInitialized())
            for (_, value) in obj.ListFields():
                self.assertIn(value, self.blank_args)

        self.s.add_handler("Test", f)
        self.s.unserialize(enc)

    def test_explicit_call(self):
        enc = self.s.serialize("test.Test", *self.blank_args)

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

    def test_unknown_message(self):
        with self.assertRaises(UnknownMessageException):
            self.s.serialize("Unknown")

    def test_unknown_message_explicit(self):
        with self.assertRaises(UnknownMessageException):
            self.s.serialize("test.Unknown")

    def test_unknown_message_explicit2(self):
        with self.assertRaises(UnknownMessageException):
            self.s.serialize("t.Unknown")

    def test_incomplete_definition_empty(self):
        with self.assertRaises(FieldNotDefinedException):
            self.s.serialize("Test")

    def test_incomplete_definition_unnamed(self):
        with self.assertRaises(FieldNotDefinedException):
            self.s.serialize("Test", 0)

    def test_incomplete_definition_named(self):
        with self.assertRaises(FieldNotDefinedException):
            self.s.serialize("Test", boolnolen = 0)

    def test_incomplete_definition_hybrid(self):
        with self.assertRaises(FieldNotDefinedException):
            self.s.serialize("Test", 0, boolnolen = 0)

    def test_wrong_type(self):
        args = self.blank_args[:]
        args[0] = ""
        with self.assertRaises(FieldWrongTypeException):
            self.s.serialize("Test", *args)

    def test_wrong_type_value(self):
        args = self.blank_args[:]
        args[5] = 9999999999999999
        with self.assertRaises(FieldWrongTypeException):
            self.s.serialize("Test", *args)

    def test_hash_name(self):
        name = "test"
        for i in range(1,9):
            self.assertEqual(len(self.s._hash_name(name, i)),
                                min(i, len(name)))

    def test_reload_definitions(self):
        class T(logging.Filter):
            def filter(self, record):
                self.called = True
                return 0
        filter = T()
        filter.called = False
        logging.getLogger().addFilter(filter)

        self.assertIn("test_pb2Test", self.s.messages)
        self.s.load_definitions()
        self.assertIn("test_pb2Test", self.s.messages)
        self.assertTrue(filter.called)

        logging.getLogger().removeFilter(filter)

    def test_wrong_type_value_check(self):
        args = self.blank_args[:]
        args[1] = 1.10
        with self.assertRaises(FieldLengthUnsupportedException):
            self.s.serialize("Test", *args)

if __name__ == '__main__':
    unittest.main()
