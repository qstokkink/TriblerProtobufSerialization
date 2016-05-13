import unittest

import messages
import struct
from exception import *
from serializer import Serializer

class TestUnserialize(unittest.TestCase):
    
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
        self.args = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 0, 0, "a", "b", "c", "d"]

    def setUp(self):
        self.calls = 0
        self.s = Serializer()
        self.enc = self.s.serialize("Test", *self.args)

    def test_no_persistent_start(self):
        def f(obj):
            self.calls += 1

        self.s.add_handler("Test", f)
        self.s.unserialize("GARBAGE" + self.enc, persistent_start = False)

        self.assertEqual(self.calls, 0)

    def test_no_persistent_end(self):
        def f(obj):
            self.calls += 1

        self.s.add_handler("Test", f)
        self.s.unserialize(self.enc + "GARBAGE", persistent_end = False)

        self.assertEqual(self.calls, 0)

    def test_persistent_start(self):
        def f(obj):
            self.assertTrue(obj.IsInitialized())
            for (_, value) in obj.ListFields():
                self.assertIn(value, self.args)
            self.calls += 1

        self.s.add_handler("Test", f)
        self.s.unserialize("GARBAGE" + self.enc, persistent_start = True)

        self.assertEqual(self.calls, 1)

    def test_persistent_end(self):
        def f(obj):
            self.assertTrue(obj.IsInitialized())
            for (_, value) in obj.ListFields():
                self.assertIn(value, self.args)
            self.calls += 1

        self.s.add_handler("Test", f)
        self.s.unserialize(self.enc + "GARBAGE", persistent_end = True)

        self.assertEqual(self.calls, 1)

    def test_header_attack(self):
        def f(obj):
            self.assertTrue(obj.IsInitialized())
            for (_, value) in obj.ListFields():
                self.assertIn(value, self.args)
            self.calls += 1

        self.s.add_handler("Test", f)
        self.s.unserialize(struct.pack('20s',"Test") + self.enc, persistent_start = True)
        
        self.assertEqual(self.calls, 1)

    def test_double_header_attack(self):
        def f(obj):
            self.assertTrue(obj.IsInitialized())
            for (_, value) in obj.ListFields():
                self.assertIn(value, self.args)
            self.calls += 1

        self.s.add_handler("Test", f)
        self.s.unserialize(struct.pack('20s',"Test") +
                            struct.pack('20s',"Test") + self.enc[:-1],
                            persistent_start = True,
                            keep_remainder = True)
        
        self.assertEqual(self.calls, 0)

    def test_header_attack_non_persistent(self):
        def f(obj):
            self.assertTrue(obj.IsInitialized())
            for (_, value) in obj.ListFields():
                self.assertIn(value, self.args)
            self.calls += 1

        self.s.add_handler("Test", f)
        self.s.unserialize(struct.pack('20s',"Test") + self.enc, persistent_start = False)
        
        self.assertEqual(self.calls, 0)

    def test_double(self):
        def f(obj):
            self.assertTrue(obj.IsInitialized())
            for (_, value) in obj.ListFields():
                self.assertIn(value, self.args)
            self.calls += 1

        self.s.add_handler("Test", f)
        self.s.unserialize(self.enc + self.enc, persistent_end = True, keep_remainder = True)

        self.assertEqual(self.calls, 2)

    def test_class_handler(self):
        class T:
            def on_test(this, obj):
                self.assertTrue(obj.IsInitialized())
                for (_, value) in obj.ListFields():
                    self.assertIn(value, self.args)
                self.calls += 1

        self.s.add_package_handler("test", T())
        self.s.unserialize(self.enc)

        self.assertEqual(self.calls, 1)

    def test_keep_remainder(self):
        def f(obj):
            self.assertTrue(obj.IsInitialized())
            for (_, value) in obj.ListFields():
                self.assertIn(value, self.args)
            self.calls += 1

        self.s.add_handler("Test", f)
        self.s.unserialize(self.enc + self.enc[:10], persistent_end = True, keep_remainder = True)
        self.s.unserialize(self.enc[10:], persistent_end = True, keep_remainder = False)

        self.assertEqual(self.calls, 2)
        

if __name__ == '__main__':
    unittest.main()
