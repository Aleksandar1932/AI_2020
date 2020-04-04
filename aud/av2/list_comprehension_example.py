def identity(nums):
    """Identity:
    Given a list of numbers, write a list comprehension that produces a copy of the list.
        >>> identity([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]
        >>> identity([])
        []
    """
    return [number for number in nums]


def doubled(nums):
    """Doubled:
    Given a list of numbers, write a list comprehension that produces a list of each number doubled.
        >>> doubled([1, 2, 3, 4, 5])
        [2, 4, 6, 8, 10]
        >>> doubled([-2, 2, -10, 10])
        [-4, 4, -20, 20]
    """
    return [number * 2 for number in nums]


def squared(nums):
    """Squared:
    Given a list of numbers, write a list comprehension that produces a list of the squares of each number.
        >>> squared([1, 2, 3, 4, 5])
        [1, 4, 9, 16, 25]
        >>> squared([-2, 2, -10, 10])
        [4, 4, 100, 100]
    """
    return [pow(number, 2) for number in nums]


def evens(nums):
    """Evens:
    Given a list of numbers, write a list comprehension that produces a list of only the even numbers in that list.
        >>> evens([1, 2, 3, 4, 5])
        [2, 4]
        >>> evens([1, 3, 5])
        []
        >>> evens([-2, -4, -7])
        [-2, -4]
    """
    return [number for number in nums if number % 2 == 0]


def odds(nums):
    """Odds:
    Given a list of numbers, write a list comprehension that produces a list of only the odd numbers in that list.
        >>> odds([1, 2, 3, 4, 5])
        [1, 3, 5]
        >>> odds([2, 4, 6])
        []
        >>> odds([-2, -4, -7])
        [-7]
    """
    return [number for number in nums if number % 2 != 0]


def positives(nums):
    """Positives:
    Given a list of numbers, write a list comprehension that produces a list of only the positive numbers in that list.
        >>> positives([-2, -1, 0, 1, 2])
        [1, 2]
    """
    return [number for number in nums if number > 0]


def selective_stringify_nums(nums):
    """Selectively stringify nums:
    Given a list of numbers, write a list comprehension that produces a list of strings of each number that is divisible by 5.
        >>> selective_stringify_nums([25, 91, 22, -7, -20])
        ['25', '-20']
    """
    return [str(number) for number in nums if number % 5 == 0]


def words_not_the(sentence):
    """Words not 'the'
    Given a sentence, produce a list of the lengths of each word in the sentence, but only if the word is not 'the'.
        >>> words_not_the('the quick brown fox jumps over the lazy dog')
        [5, 5, 3, 5, 4, 4, 3]
    """
    return [len(word) for word in sentence.split() if word != 'the']


def vowels(word):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    """Vowels:
    Given a string representing a word, write a list comprehension that produces a list of all the vowels in that word.
        >>> vowels('mathematics')
        ['a', 'e', 'a', 'i']
    """
    return [character for character in word if character in vowels_list]


def vowels_set(word):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    """Vowels set:
    Given a string representing a word, write a set comprehension that produces a set of all the vowels in that word.
        >>> vowels_set('mathematics')
        set(['a', 'i', 'e'])
    """
    return {character for character in word if character in vowels_list}


def disemvowel(sentence):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    """Disemvowel:
    Given a sentence, return the sentence with all vowels removed.
        >>> disemvowel('the quick brown fox jumps over the lazy dog')
        'th qck brwn fx jmps vr th lzy dg'
    """
    return [character for word in sentence for character in word if character not in vowels_list]


def wiggle_numbers(nums):
    """Wiggle numbers:
    Given a list of number, return the list with all even numbers doubled, and all odd numbers turned negative.
        >>> wiggle_numbers([72, 26, 79, 70, 20, 68, 43, -71, 71, -2])
        [144, 52, -79, 140, 40, 136, -43, 71, -71, -4]
    """
    return [number * 2 if number % 2 == 0 else number * -1 for number in nums]


def encrypt_lol(sentence):
    bottom = ord('a')
    upper = ord('y')
    """Encrypt lol:
    Given a sentence, return the setence will all it's letter transposed by 1 in the alphabet, but only if the letter is a-y.
        >>> encrypt_lol('the quick brown fox jumps over the lazy dog')
        'uif rvjdl cspxo gpy kvnqt pwfs uif mbzy eph'
    """

    return [chr(ord(character)+1) if bottom <= ord(character) <= upper else chr(ord(character)) for word in sentence for character in word]


# STOP HERE! You solved everything!
if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n*** ALL TESTS PASSED!\n')
