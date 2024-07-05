#MO5 Testing section
#assert affirmative
#assert sum([1, 2, 3]) == 6, "Should be 6"

#assert negative
#assert sum([1, 2, 3]) == 5, "Should be 6"

#testing in py instead of an REPL (which i was
#doing already, see above)
#TEST_SUM.PY
#def test_sum():
#    assert sum([1, 2, 3]) == 6, "Should be 6"

#if __name__ == "__main__":
#    test_sum()
#    print("Everything passed")

#TEST_SUM_2.PY
#def test_sum():
 #   assert sum([1, 2, 3]) == 6, "Should be 6"

#def test_sum_tuple():
#    assert sum((1, 2, 2)) == 6, "Should be 6"

#if __name__ == "__main__":
#    test_sum()
#    test_sum_tuple()
#    print("Everything passed")


#TEST_SUM_UNITTEST.PY
#import unittest


#class TestSum(unittest.TestCase):

#    def test_sum(self):
#        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

#    def test_sum_tuple(self):
#        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

#if __name__ == '__main__':
#    unittest.main()

#also installed the nose2 using my CLI as instructed
