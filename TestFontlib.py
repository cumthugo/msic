from Fontlib import *
import unittest

class FontLibTestCase(unittest.TestCase):
    def testSimpleWidth(self):
        self.assertEqual(1,GetTextWidth('./unittest/VWThesis_MQB_Regular_140425.TTF',12,u"222"))



if __name__ == '__main__':
    unittest.main()
