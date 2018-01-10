import unittest
from simplefile import print_and_add


class TestPrint_and_add_2(unittest.TestCase):

    def test1(self):
        self.assertEqual(print_and_add(5,6),11)


if __name__ == '__main__':
    unittest.main()



