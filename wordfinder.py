"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """
    Machine to print random word from specified path.
    
    >>> found_word = WordFinder(path = "words.txt")

    >>> found_word.random()
    

    >>> found_word.random()
    

    >>> found_word.random()
    

    
    """
    def __init__(self, path):
        file = open(path,'r')
        result = ""
        x = 0;
        rand_number = randint(0, 258000)
        while x < rand_number:
            next_line = file.readline()

            if  x == rand_number:
                result = next_line.strip()
                break;
            x+=1
        print(result)
        file.close()
        


    ...
