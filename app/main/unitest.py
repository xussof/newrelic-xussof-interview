import unittest

from main import common_words
from random_word import RandomWords

txtfolder = "../txtfolder"

class TestOutput(unittest.TestCase):
    r = RandomWords()

    #Generating file to read lately with random words
    file = open(txtfolder + "/test.txt", "w") 
    i = 0
    while i < 50:
        file.write("How are you " + str(r.get_random_word()) + " ")
        if i < 30:
            file.write("Monolitic scheme supervision " + str(r.get_random_word()) + " ") 
            if i < 20:
                file.write("Terrified of cats " + str(r.get_random_word()) + " ") 
        i += 1
    file.close()
    
    common_words()

if __name__ == '__main__':
    unittest.main()

