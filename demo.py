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

print(digits_or_letters("abc123"))
print(digits_or_letters("a1b2c3d"))
print(digits_or_letters("1a2b3c4"))
print(digits_or_letters("abc123!@#DEF"))
print(digits_or_letters("H3110 W0R1D"))
print(digits_or_letters("P455W0RD"))