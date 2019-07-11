lines=[]
while(True):
    s=input("KEY")
    if s:
        lines.append(s.upper())
    else:
        break;
for sentence in lines:
    print(sentence)
