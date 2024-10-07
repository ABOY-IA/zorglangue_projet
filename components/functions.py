import re

def inverser_mot(mot):
    lettres = [char for char in mot if char.isalpha()]
    lettres_inverses = lettres[::-1]
    resultat = []
    
    for i, char in enumerate(mot):
        if char.isalpha():
            inversed_char = lettres_inverses.pop(0)
            if char.isupper():
                resultat.append(inversed_char.upper())
            else:
                resultat.append(inversed_char.lower())
        else:
            resultat.append(char)
    
    return ''.join(resultat)

def zorglangue(phrase):
    mots = re.findall(r'\w+|[^\w\s]', phrase, re.UNICODE)
    mots_inverses = [inverser_mot(mot) for mot in mots]
    resultat = ''
    
    for i, mot in enumerate(mots):
        if mot == "'" and i > 0:
            resultat += mot
        elif i > 0 and mots[i-1] != "'" and not re.match(r'[^\w\s]', mot):
            resultat += ' ' + mots_inverses[i]
        else:
            resultat += mots_inverses[i]
    
    return resultat