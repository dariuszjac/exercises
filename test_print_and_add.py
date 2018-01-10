import unittest
from simplefile import print_and_add


class TestPrint_and_add(unittest.TestCase):

    def test1(self):
        self.assertEqual(print_and_add(2,3),5)


if __name__ == '__main__':
    unittest.main()



