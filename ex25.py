#Ex25: Even More Pratice

def break_words(stuff):
    ''' This function will split string by whitespace '''
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    ''' Prints the first word after popping it off. '''
    word = words.pop(0)
    print(word)

def print_last_word(words):
    ''' Prints the last word after popping it off. '''
    word = words.pop(-1)
    print(word)

