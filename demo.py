# -*- coding: utf-8 -*-

def is_mirror(s1: str, s2: str) -> bool:
    f1 = ""
    for ch in s1:
        if ch.isalpha():
            f1 += ch
    print(f1)

    f2 = ""
    for ch in s2:
        if ch.isalpha():
            f2 += ch
    print(f2)
    
    return f1 == f2[::-1]

# Ê¾Àý²âÊÔ
print(is_mirror("abc", "cba"))              # True
print(is_mirror("Abc!", "cba"))             # False
print(is_mirror("A man, a plan!", "nalp a ,nam A"))  # True
print(is_mirror("123abc", "cba456"))        # True
