SCRABBLE_VALUES = (
    ('a', 1), ('b', 3), ('c', 3), ('d', 2), ('e', 1),
    ('f', 4), ('g', 2), ('h', 4), ('i', 1), ('j', 8),
    ('k', 5), ('l', 1), ('m', 3), ('n', 1), ('o', 1),
    ('p', 3), ('q', 10), ('r', 1), ('s', 1), ('t', 1),
    ('u', 1), ('v', 4), ('w', 4), ('x', 8), ('y', 4),
    ('z', 10)
)

# Write your Scrabble code below

def read_scores_1(scores:tuple[tuple[int,str]]) -> dict[str, int]:
    """
    input the tuple and return the dict
    """
    # build a dict
    dict = {}
    # walk through the tuple
    for i in range(len(scores)):
        pair = scores[i]
        letter, score = pair # unpacking letter and score
        # add in dict
        dict[letter] = score
    return dict
        
print(read_scores_1(SCRABBLE_VALUES))

'''
def read_scores_2(scores:tuple[tuple[int,str]]) -> dict[str, int]:
    """
    input the tuple and return the dict
    """
    # build a dict 
    return dict(scores)
print(read_scores_2(SCRABBLE_VALUES))
'''


def get_score(scores:dict[str,int], word: str) -> int:
    score = 0
    confirmed_word = ''
    for letter in word:
        if letter.isalpha():
            confirmed_word +=letter # check the words are all letters
    for letter in confirmed_word:
        if letter in scores:
            score += scores[letter]
       # or  score = score + scores.get(letter,0)
    return score

