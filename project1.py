#genrate random passwords
import random
import string

pass_len = 9
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charValues)
    
print("your random password is: ", password)