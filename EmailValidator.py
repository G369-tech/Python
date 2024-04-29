print('======== HariPrabodham ========')
print('-------------------------------')
print('Valid Email Address Checker')
print('-------------------------------')

import re
def email(user_email):
    email_condition = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(email_condition, user_email):
        print("Valid email address")
    else:
        print("Invalid email address")

user_email = input("Enter the email: ")
email(user_email)
