# Author: blacklight2000
# Last updated: 2 Mar 2015


def count_letters(phrase):
    """
    Function takes a phrase as input and returns a count for each letter
    in the phrase

    :type: string
    :params phrase that may include non-alphabetic cruft such as punctuation

    :type dict
    :return a count for each letter in the phrase
    """

    import re
    phrase = phrase.lower()
    phrase = re.sub(r'\W', '', phrase)
    letters = sorted(list(phrase))
    letter_array = sorted(list(set(phrase)))
    letters_dict = {}
    for letter in letter_array:
        letters_dict[letter] = letters.count(letter)
    return letters_dict


if __name__ == '__main__':
    STRING = "Hello, world!"
    ANSWER = {'d': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}
    assert(count_letters(STRING) == ANSWER)
    from operator import itemgetter as getitem
    REVERSE_SORT_ANSWER  \
        = [('l', 3), ('o', 2), ('e', 1), ('d', 1), ('h', 1), ('r', 1), ('w', 1)]
    # assert(sorted(ANSWER.items(), key=getitem(1), reverse=True)  \
    #     == REVERSE_SORT_ANSWER)
    assert(sorted(count_letters(STRING).items(), key=getitem(1), reverse=True) \
        == REVERSE_SORT_ANSWER)
    
