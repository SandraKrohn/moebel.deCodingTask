import unittest
import sumForName

class TestSumForName(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sumForName.nameSum("Ivan"), 46)
        self.assertEqual(sumForName.nameSum("Günther Jauch"), 115)
        self.assertEqual(sumForName.nameSum("_Mozart!"), 93)

if __name__ == '__main__':
    unittest.main()