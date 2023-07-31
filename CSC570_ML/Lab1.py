from datetime import datetime
import random

'''
1a. Write a program to display information about the current date and time.
'''

now = datetime.now()
print("Now:", now, "\n")

dtstring = now.strftime("%d/%m/%Y %H : %M : %S")
print("Dstring:", dtstring, "\n")

print("Day:", dtstring[0:2])
print("Month:", dtstring[3:5])
print("Year:", dtstring[6:10])
print("Hour:", dtstring[11:13])
print("Minute:", dtstring[16:19])
print("Second:", dtstring[21:23])
print("\n***********************\n")

'''
1b. Invert string and check for palindrome
'''
i = 4
j = 0
palindrome = 0

word = input("Enter a 5 letter string: ")
if len(word) != 5:
    print("Input is not a 5 letter string.")
    exit()
else:
    while(i >= 0):
        print(word[i], " ")
        if(word[i].lower() != word[j].lower()):
            palindrome = 1
        i-=1
        j+=1

    if (palindrome == 0):
        print("It's a palindrome!\n")
    else:
        print("It's NOT a palindrome!\n")

print("\n***********************\n")

'''
2a.
'''

def findOrderedSubstring(subs, mainstr):

    if(subs.lower() in mainstr.lower()):
        print("True")
    else:
        print("False")

findOrderedSubstring("love", "lovelace")
findOrderedSubstring("Love", "lovelace")
findOrderedSubstring("dina", "dinosaur")

print("\n***********************\n")

'''
2b.
'''

def cumulative(numlst):
    lst = []
    oldsum = 0
    for num in numlst:
        oldsum += num
        lst.append(oldsum)

    return lst


lst = cumulative([1,2,3])
print(lst)

lst = cumulative([2,5,8])
print(lst)

print("\n***********************\n")

'''
2c.
'''
def getNames():
    
    for i in range(0,3):
        user = input("Enter name: \n").lower().split()
        user = "".join(user) 
        print(createEmail(user), "\n")

def createEmail(user):
    email = ""
    for i in range(0,5):
        email += random.choice(user)

    email += "@gmail.com"
    return email


getNames()

