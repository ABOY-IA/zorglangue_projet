import string

def zorglangue(phrase):
    def reverse_word(word):
        if word[-1] in string.punctuation:
            return word[:-1][::-1] + word[-1]
        return word[::-1]

    mots_inverses = [reverse_word(mot) for mot in phrase.split()]
    return ' '.join(mots_inverses)