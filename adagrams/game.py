# THIS IS AN EXPERIMENT!

import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

LETTER_SCORE = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

# word class defintion
class Word:
    def __init__(self, word):
        self.word = word
        self.length = len(word)
        self.score = score_word(word)

def draw_letters():
    # create list of randomly selected letters from letter pool
    chosen_letters = []
    remaining_letters_count = sum(LETTER_POOL.values())
    if remaining_letters_count >= 10:
        # do this 10 times:
        while len(chosen_letters) != 10:
            # from letter bank select random letter
            drawn_letter = random.choice(list(LETTER_POOL.items()))
            # check count of letter is not zero
            if LETTER_POOL[drawn_letter[0]] != 0:
                # add letter to list
                chosen_letters.append(drawn_letter[0])
                # decrease letter pool count by 1
                LETTER_POOL[drawn_letter[0]] -= 1
    return chosen_letters

def uses_available_letters(word, letter_bank):
    # checks to make sure that word is composed of elements in letter_bank
    letter_bank_copy = letter_bank[:]
    if not isinstance(word, str) and len(word) <= 10:
        return False
    # if word is valid    
    for char in word.upper():
        if char in letter_bank_copy:
            letter_bank_copy.remove(char)
        else:
            return False
    return True

def score_word(word):
    # word = Word(word)
    # return word.score
    total_word_score = 0
    for char in word.upper():
        total_word_score += LETTER_SCORE[char]
    if len(word) >= 7:
        total_word_score += 8
    return total_word_score

def get_highest_word_score(word_list):
    # returns highest scoring word and its score
    list_of_word_objects = [Word(word) for word in word_list]
    high_score = max(word.score for word in list_of_word_objects)
    high_score_words = [word for word in list_of_word_objects if word.score == high_score]
    if len(high_score_words) > 1:
        return tie_breaker(high_score_words, high_score)
    winning_word = high_score_words[0]
    return winning_word.word, winning_word.score

def tie_breaker(word_list, score):
    # return word if 10 chars long
    for word in word_list:
        if word.length == 10:
            return word.word, score
    # otherwise return shortest word
    winning_word = min(word_list, key= lambda w: w.length)
    return winning_word.word, score

    ## the following solution accesses the Word objects
    # min_length = min(word.length for word in word_list)
    # for word in word_list:
    #     if word.length == min_length:
    #         return word.word, word.score


# get_highest_word_score(['bob', 'rose', 'xylophone', 'WWW', 'MMMM'])
# get_highest_word_score(['WWW', 'MMMM'])
# get_highest_word_score(['WWW', 'MMMM', ''])
# get_highest_word_score(["AAAAAAAAAA", "BBBBBB"])
# words = ["BBBBBB", "AAAAAAAAAA"] # test_get_highest_word_tie_prefers_ten_letters_unsorted_list
# words = ["AAAAAAAAAA", "EEEEEEEEEE"] # return first instance of two 10 letter words
# get_highest_word_score(words)