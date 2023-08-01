try:
    s=input("Enter Password(ONLY ALPHABET):")
except:
    print("Enter Valid Input.....")

crack=""
c=0

for i in range(0,len(s)):
    if s.isalpha():
        v=ord(s[i])
    else:
        print("Enter Valid Input.....")
        c+=1
        break
    for j in range(65,123):
        if j==v:
            r=chr(v)
            crack+=r
        else:
            pass

if c==1:
    pass
else:
    print(f"Your Password is crack:{crack}")