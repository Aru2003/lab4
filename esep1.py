soz=str(input())
upper=0
lower = 0
for i in soz:
    if i.isupper():
        upper+=1
    else:
        lower+=1
if upper>lower:
    print(soz.upper())
else:
    print(soz.lower())