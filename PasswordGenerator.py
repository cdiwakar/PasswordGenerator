from random import sample

small='abcdefghijklmnopqrestuvwxyz'
caps='ZYXWVUTSRQPONMLKJIHGFEDCBA'
NUM='1234567890'
sym='!@#$%^&*()'

string= small+caps+NUM+sym
len=16
password="".join(sample(string,len))
print("Your new password is : " + password)
