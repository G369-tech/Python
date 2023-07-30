#Time Complexity:0(n)
#Space Complexity:0(1)
import re
print('1. Password should have atleast one numerical digit(0-9).')
print('____________________________________________________________')
print('2. Passwords length should be in between 8 to 15 characters.')
print('____________________________________________________________')
print('3. Password should have at least one lowercase letter(a- z).')
print('____________________________________________________________')
print('4. Password should have at least one uppercase letter(A- Z).')
print('____________________________________________________________')
print('5. Password should have at least one special character.[@_!#$%^&*()<>?/\|}{~:]')
print('____________________________________________________________')

try:
	s=input("Enter Password:")
except:
	print("Enter Valid Input...")

#Check Length of String
def character(s):
	if len(s)>=8 and len(s)<=15:
		return True
	else:
		pass

#Check Numerical is present or not
def numerical(s):
	for i in range(len(s)):
		if s[i].isdigit():
			return True
			break

#Check Upper Letter
def upper_l(s):
	for i in range(len(s)):
		if s[i].isupper():
			return True
			break

#Check Lower Letter
def lower_l(s):
	for i in range(len(s)):
		if s[i].islower():
			return True
			break

#Check Special Character
def special_c(s):
 
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(s) == None):
         pass
    else:
    	return True

#Check all Condotions for Password
if (special_c(s)==True and lower_l(s)==True and upper_l(s)==True and numerical(s)==True and character(s)==True):
	print("Password is Valid.")
else:
	for i in range(0,len(s)):
		if " "==s[i]:
			print("Space is not Valid.")
			break
	else:
		print("Password is not Valid")