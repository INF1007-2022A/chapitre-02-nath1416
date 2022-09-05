#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    NouveauMot = ""
    for i in range(len(mot)):
        if ord("a") <= ord(mot[i]) <= ord("z"):
            NouveauMot += chr(ord(mot[i]) - 32)
        else:
            NouveauMot += mot[i]
    return NouveauMot


            
if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])


    print(mots)
