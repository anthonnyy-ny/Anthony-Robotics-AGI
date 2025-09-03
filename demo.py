while True:
    s1=input("s1: ")
    if s1=="0":
        break
    s2=input("s2: ")
    if s2=="0":
        break
    #print("string: "+s1+s2)
    if len(s1)>=len(s2):
        print("string: "+s1+s2)
    if len(s2)>=len(s1):
        print()
print("end")