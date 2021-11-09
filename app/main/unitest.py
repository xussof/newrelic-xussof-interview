import unittest
import pytest

from mock import patch

from main import common_words, test
from random_word import RandomWords

from io import StringIO
import sys
txtfolder = "../txtfolder"
testfile = "/test.txt"
file_path = txtfolder + testfile



class Case(unittest.TestCase):
    
    r = RandomWords()

    #Generating file to read lately with random words
    file = open(txtfolder + testfile, "w") 
    i = 0
    while i < 50:
        file.write("How are you " + str(r.get_random_word()) + " ")
        if i < 30:
            file.write("Monolitic scheme supervision " + str(r.get_random_word()) + " ") 
            if i < 20:
                file.write("Terrified of cats " + str(r.get_random_word()) + " ") 
        i += 1
    file.close()
        
    common_words(file_path)

    
    # def test_foo(self):
    #     test()
    #     if not hasattr(sys.stdout, "getvalue"):
    #         self.fail("need to run in buffered mode")
    #     output = sys.stdout.getvalue().strip() # because stdout is an StringIO instance
    #     self.assertEqual(output,'hello world!')
    
    # def test_common_worlds(self):
        
    #     print(file_path)
    #     common_words(file_path)
    #     if not hasattr(sys.stdout, "getvalue"):
    #         self.fail("need to run in buffered mode")
    #     output = sys.stdout.getvalue().strip() # because stdout is an StringIO instance
    #     for i in output:
    #         print("Hola")
    #         print(sys.stdout.getvalue())
    #     # print(sys.stdout.getvalue())
    #     self.assertEqual(output,'hello world!')

if __name__ == '__main__':
    assert not hasattr(sys.stdout, "getvalue")
    unittest.main(module=__name__, buffer=True, exit=False)

