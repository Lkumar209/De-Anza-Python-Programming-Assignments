''''
Laxya  Kumar
Email Domain Finder
'''


bool = True

while bool:
    email = input("Enter your email: ")
    if(email.count('@') != 1) or (email.count('.') < 1):
        print("Invalid email address")
    else:
        bool = False

atpos = email.find('@')
dotpos = email.find('.')
print(email[atpos+1:dotpos])


'''
Result 1:

Enter your email: laxya20supercell@gmail.com
gmail

Result 2:

Enter your email: johnnykevins@hotmail.com
hotmail
'''