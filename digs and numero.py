s=input("Key in an alphanumeric sentence")
d={"Digs":0,"Letter":0}
for c in s:
    if c.isdigit():
        d["Digs"]+=1
    elif:
     d["Letter"]+=1
    else:
        pass
print("letters ", d["Letter"])
print("Digits ",d["Digs"])
