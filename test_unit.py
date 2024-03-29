import unittest
# https://docs.python.org/ja/3/library/unittest.html

# テスト対象のplus 関数
def plus(a, b):
    return a + b
def minus(a, b):
    return a - b

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)            # aとb が同じであること　 # add assertion here
        self.assertEqual(10, min(20, 10))       # aとb が同じでないこと
        self.assertNotEqual(10, max(11, 10))    # aとb が同じでないこと
        self.assertTrue(True)                   # x が Trueであること
        self.assertIs("abc", "abc")             # a が b のオブジェクトであること
        self.assertIn('a', ['a', 'c'])          # b の中にa が存在すること


    # テストプログラム
    def test_plus(self):
        self.assertEqual(10, plus(2, 8))
        #self.assertEqual(20, plus(2, 8))

    def test_minus(self):
        self.assertEqual(10, minus(12, 2))


    # sample　実行
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):                              # 特定の例外があることをテスト
            s.split(2)

if __name__ == '__main__':
    unittest.main()
