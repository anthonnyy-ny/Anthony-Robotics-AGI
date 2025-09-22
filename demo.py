# -*- coding: utf-8 -*-

def digits_or_letters(s:str)->str:
    digits,letters=0,0

    for c in s:
        if c.isdigit():
            digits+=1
        elif c.isalpha():
            letters+=1
    
    if digits>letters:
        return "letters"
    elif letters>digits:
        return "digits"
    else:
        return "tie"

digits_or_letters()