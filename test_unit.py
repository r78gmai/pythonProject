import unittest


# テスト対象のplus 関数
def plus(a, b):
    return a + b

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    # テストプログラム
    def test_plus(self):
        self.assertEqual(10, plus(2, 8))
        #self.assertEqual(20, plus(2, 8))

if __name__ == '__main__':
    unittest.main()
