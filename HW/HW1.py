#%%
# E.1:
#Write a python script that reads a string from the user input and print the following
#i. Number of uppercase letters in the string.
#ii. Number of lowercase letters in the string
#iii. Number of digits in the string
#iv. Number of whitespace characters in the string

#i.
x = input("Please type a string:")
print(x)
count = 0
lower_ct = 0
dig_ct = 0
sp_ct = 0
for i in x:
    if i.isupper() == True:
        count += 1
#print("Capital Letters:",  count)
    elif i.islower() == True:
        lower_ct += 1
    elif i.isdigit() == True:
        dig_ct += 1
    elif i.isspace() == True:
        sp_ct += 1
print("Capital Letters:", count)
print("Lowercase Letters:", lower_ct)
print("Digitals:", dig_ct)
print("Whitspace:", sp_ct)

#%%
#E.2:
#Write a python script that accepts a string then create a new string by shifting one position to
#left.
#Example: input : class 2021 output: lass 2021c
text = input('Enter a string: ')
newtext = text[1:] + text[0]
print('New string:', newtext)

#%%
#E.3:
#Write a python script that a user input his name and program display its initials.
#Hint: Assuming, user always enter first name, middle name and last name.

name = input('Please enter you your fullname:')
print('Thsi is the name you entered:', name)
#x = x.split()
def get_initials(x):
    print(x[0].upper())
    for i in range(1, len(x)-1):
        if x[i] == ' ':
            print(x[i+1].upper())
            return 
print(get_initials(x))

#
#def printInitials(name):
#     
#    if (len(name) == 0):
#        return
# 
#    # Split the string using 'space'
#    # and print the first character of
#    # every word
#    words = name.split(" ")
#    for word in words:
#        print(word[0].upper(), end = " ")
#        
#printInitials(name)
#%%
#E.4:
#Write a python script that accepts a string to setup a passwords. The password must have the
#following requirements
#• The password must be at least eight characters long.
#• It must contain at least one uppercase letter.
#• It must contain at least one lowercase letter.
#• It must contain at least one numeric digit.

password = input('Please set up the password:')


#%%
#E.5:
#Write a python script that reads a given string character by character and count the repeated
#characters then store it by length of those character(s).

#%%
#E.6:
#Write a python script to find all lower and upper case combinations of a given string.
#Example: input: abc output: ’abc’, ’abC’, ’aBc’, ...

#%%
#E.7:
#Write a python script that
#i. Read first n lines of a file.
#ii. Find the longest words.
#iii. Count the number of lines in a text file.
#iv. Count the frequency of words in a file.
#Hint: first create a test.txt file and dump some textual data in it. Then test your code.

#%%
#.8:
#Answer all the class exercise questions and submit it (Check the instructions).
