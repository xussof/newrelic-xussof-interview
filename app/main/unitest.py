#Create a file with 100 lines on which we place 60 times
#How are you
# 20 times 
# Fine thank you
# 10 times 
# You are welcome




import unittest
from main import test
from StringIO import StringIO
class TestSum(unittest.TestCase):

    # def test_sum(self):
    # with captured_output(self) as (out, err):
    #     test()
    #     # This can go inside or outside the `with` block
    # output = out.getvalue().strip()
    # self.assertEqual(output, 'hello world!')
    
    # def test_sum_tuple(self):
    #     self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
    def test_foo():

        

        out = StringIO()
        test(out=out)
        output = out.getvalue().strip()
        assert output == 'hello world!'

if __name__ == '__main__':
    unittest.main()
