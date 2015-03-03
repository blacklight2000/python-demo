""" count_words module """
import re

def count_words(phrase):
    """
        Returns count of words, except for common words such as 'the', '\
    this', etc. 
   
    :param string
    :returns words count, excluding common words such as 'the' 

    """
    exclude_words = set(['a', 'an', 'of', 'the', 'this'])
    phrase = re.sub(r'\W', ' ', phrase.lower())
    words = phrase.split()
    return len(words) - sum([words.count(x) for x in exclude_words])

if __name__ == '__main__':
    STRING = "The. Fox, juMpEd/ oVer@ THE. #lioN"
    assert(count_words(STRING)) == 4
