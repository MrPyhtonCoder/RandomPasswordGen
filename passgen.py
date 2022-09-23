import time
import random
print ("Welcome To The Random Password Generator")
time.sleep (2)
asking = input("Do You Want To Generate A Random Password       ")
if asking != "yes":
    quit ()
lower_case = "abcdefghijkmnlopqrstuvwxyz"
upper_case = "ABCDEFGHIJKMNLOPQRSTUVWXYZ"
num = "1234567890"
symbol = "[]{}*()._-"
ans = lower_case + upper_case + num + symbol
length = int(input("Enter The Length Of Your Becoming Password      "))
time.sleep (2)
password = "".join(random.sample(ans,length))
print ("Generating Password .....")
time.sleep (5)
print ("Random Generated Password Is       ",password)
aasking = input("Do You want To Generate Another Password?      ")
if aasking != "yes":
    quit ()
time.sleep (1)
length2 = int(input("Enter The Length Of Your Becoming Password      "))
print ("Generating Password .....")
time.sleep (4)
lower_case2 = "abcdefghijkmnlopqrstuvwxyz"
upper_case2 = "ABCDEFGHIJKMNLOPQRSTUVWXYZ"
num2 = "1234567890"
symbol2 = "[]{}*()._-"
ans2 = lower_case2 + upper_case2 + num2 + symbol2
password2 = "".join(random.sample(ans2,length2))
print ("Random Generated Password Is       ",password2)