import re

def inverser_mot(mot):
    # Extraire les lettres sans la ponctuation
    lettres = [char for char in mot if char.isalpha()]
    
    # Inverser les lettres
    lettres_inverses = lettres[::-1]
    
    resultat = []
    
    # Parcourir le mot original pour replacer les lettres inversées et gérer les majuscules
    for i, char in enumerate(mot):
        if char.isalpha():
            # On récupère la lettre inversée
            inversed_char = lettres_inverses.pop(0)
            
            # Si la lettre d'origine est en majuscule, on garde cette majuscule dans le résultat
            if char.isupper():
                resultat.append(inversed_char.upper())
            else:
                resultat.append(inversed_char.lower())
        else:
            # Ajouter directement la ponctuation ou les autres caractères
            resultat.append(char)
    
    return ''.join(resultat)

def zorglangue(phrase):
    mots = re.findall(r'\w+|[^\w\s]', phrase, re.UNICODE)
    mots_inverses = [inverser_mot(mot) for mot in mots]  # Inverser les mots
    resultat = ''
    
    for i, mot in enumerate(mots):
        # On gère les apostrophes pour éviter les espaces incorrects
        if mot == "'" and i > 0:
            resultat += mot
        elif i > 0 and mots[i-1] != "'" and not re.match(r'[^\w\s]', mot):
            # On ajoute un espace avant les mots alphanumériques uniquement
            resultat += ' ' + mots_inverses[i]
        else:
            resultat += mots_inverses[i]
    
    return resultat

phrase = "J'espère qu'Anthony sera satisfait du résultat."
resultat = zorglangue(phrase)
print(f"Phrase en Zorglangue : {resultat}")