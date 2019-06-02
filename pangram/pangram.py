def is_pangram(sentence):
    ''' Determine if a sentence contains every letter in the alphabet.
        Returns True or False.
    '''
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return set(sentence.lower()) >= alphabet
