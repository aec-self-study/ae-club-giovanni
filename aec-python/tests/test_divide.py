import unittest

from calculate import aec_divide


class TestDivide(unittest.TestCase):
    def test_divide_normal(self):
        arg_ints = [20, 5]
        sub_result = aec_divide(arg_ints)
        self.assertEqual(sub_result, 4)

    def test_divide_0(self):
        arg_ints = [20, 0]
        sub_result = aec_divide(arg_ints)
        self.assertEqual(sub_result, 0)

    def test_divide_three(self):
        arg_ints = [20, 4, 2]
        with self.assertRaisesRegex(Exception, 'more than two args') as context:
            aec_divide(arg_ints)


if __name__ == "__main__":
    unittest.main()
