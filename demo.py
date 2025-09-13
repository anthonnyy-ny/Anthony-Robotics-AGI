s = input()
#print(' '.join(f"{ord(c):02X}" for c in s))

for c in s:
    print(" ".join(f"{ord(c):02x}"))
