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
        messages.MESSAGES.append(__import__("test_complex_pb2", globals(), locals(), [], -1))

    def setUp(self):
        self.calls = 0
        self.s = Serializer()

    def test_unnamed_serialize(self):
        enc = self.s.serialize("TestComplex", [("normal", ["m1", "m2"])])        

        def f(obj):
            self.assertTrue(obj.IsInitialized())
            self.assertEqual(obj.nesteds[0].normal, "normal")
            self.assertEqual(obj.nesteds[0].multiple[0], "m1")
            self.assertEqual(obj.nesteds[0].multiple[1], "m2")
            self.calls += 1
        
        self.s.add_handler("TestComplex", f)
        self.s.unserialize(enc)
        self.assertEqual(self.calls, 1)

    def test_named_serialize(self):
        enc = self.s.serialize("TestComplex",
                            nesteds = [{
                                            "normal": "normal",
                                            "multiple": [
                                                        "m1", 
                                                        "m2"
                                                        ]
                                        }]
                            )        

        def f(obj):
            self.assertTrue(obj.IsInitialized())
            self.assertEqual(obj.nesteds[0].normal, "normal")
            self.assertEqual(obj.nesteds[0].multiple[0], "m1")
            self.assertEqual(obj.nesteds[0].multiple[1], "m2")
            self.calls += 1
        
        self.s.add_handler("TestComplex", f)
        self.s.unserialize(enc)
        self.assertEqual(self.calls, 1)

    def test_nested_length(self):
        with self.assertRaises(FieldTooLongException):
            self.s.serialize("TestComplex", [("", ["longerthantwentycharacters"])])

    def test_obj_onto_repeated(self):
        with self.assertRaises(FieldWrongTypeException):
            self.s.serialize("TestComplex", [("", ("m1",))])

    def test_repeated_onto_obj(self):
        with self.assertRaises(FieldWrongTypeException):
            self.s.serialize("TestComplex", [["", ["m1"]]])

    def test_unicode_strings(self):
        sbs = '}\xc8A\xc1\x8a}D\xe8\xea\x93}'
        enc = self.s.serialize("TestComplex", [(sbs, ["m1", "m2"])])

        def f(obj):
            self.assertTrue(obj.IsInitialized())
            for i in range(len(sbs)):
                self.assertEqual(ord(obj.nesteds[0].normal[i]), ord(sbs[i]))
            self.assertEqual(obj.nesteds[0].multiple[0], "m1")
            self.assertEqual(obj.nesteds[0].multiple[1], "m2")
            self.calls += 1

        self.s.add_handler("TestComplex", f)
        self.s.unserialize(enc)
        self.assertEqual(self.calls, 1)

    def test_optional_missing(self):
        enc = self.s.serialize("TestOptional")

        def f(obj):
            self.assertTrue(obj.IsInitialized())
            self.assertTrue(not obj.field)
            self.calls += 1

        self.s.add_handler("TestOptional", f)
        self.s.unserialize(enc)
        self.assertEqual(self.calls, 1)

    def test_optional_set(self):
        enc = self.s.serialize("TestOptional", "test")

        def f(obj):
            self.assertTrue(obj.IsInitialized())
            self.assertEqual(obj.field, "test")
            self.calls += 1

        self.s.add_handler("TestOptional", f)
        self.s.unserialize(enc)
        self.assertEqual(self.calls, 1)

if __name__ == '__main__':
    unittest.main()
