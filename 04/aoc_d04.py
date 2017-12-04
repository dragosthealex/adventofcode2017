"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

Your puzzle answer was 451.

--- Part Two ---

For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
Under this new system policy, how many passphrases are valid?

Your puzzle answer was 223.

Both parts of this puzzle are complete! They provide two gold stars: **

"""


def count_valid_words(phrases, valid_func):
    return sum(1 for p in phrases if valid_func(p))


def is_valid_passphrase(passphrase):
    words = set()
    for word in passphrase.split():
        word = word.strip()
        if word in words:
            return False
        words.add(word)
    return True


def is_valid_passphrase_no_anagrams(passphrase):
    words = set()
    for word in passphrase.split():
        word = ''.join(sorted(word.strip()))
        if word in words:
            return False
        words.add(word)
    return True


if __name__ == '__main__':
    with open('input.txt') as f:
        contents = f.readlines()
        print(count_valid_words(contents, is_valid_passphrase))
        print(count_valid_words(contents, is_valid_passphrase_no_anagrams))
