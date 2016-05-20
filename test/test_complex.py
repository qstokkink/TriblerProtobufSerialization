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

if __name__ == '__main__':
    unittest.main()
