# =================================================================
# Class_Ex1:
# Write a function that prints all the chars from string1 that appears in string2.
# Note: Just use the Strings functionality no packages should be used.
# ----------------------------------------------------------------
#%%
print(20*'-' + 'Begin Q1' + 20*'-')

s1 = 'abcdefg'
s2 = 'ab'

for i in s1:
    if i in s2:
      
       print(f' Duplicate elements are:{i}')
        





print(20*'-' + 'End Q1' + 20*'-')

#%%
# =================================================================
# Class_Ex2:
# Write a function that counts the numbers of a particular letter in a string.
# For example count the number of letter a in abstract.
# Note: Compare your function with a count method
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q2' + 20*'-')

s1 = 'abstract'
count = 0
list = []
for i in s1:
    if i == 'a':
        count += 1
        
print(f'number of a: {count}')
        
#print(s1.count('a'))

print(20*'-' + 'End Q2' + 20*'-')

#%%
# =================================================================
# Class_Ex3:
# Write a function that reads the Story text and finds the strings in the curly brackets.
# Note: You are allowed to use the strings methods
# Copy a text from wiki and add some curly bracket in the text call the string Story.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q3' + 20*'-')

str = "dhfhuehfsbvhfdnbnx{FSsffs,ee}sgss{dgfy}egfhs"
substr = "{"

#print(string_story.find('{'))
#print(string_story[string_story.find('{'):string_story.find('}')])
start = 0
end = 0
for i in str:
    if i == '{':
        start = str.find(i, start) + 1
    elif i == '}':
        end = str.find(i, end)
        print(str[start:end])

#?????????????????
        
         

#def find_all(a_str, sub):
#    start = 0
#    while True:
#        start = a_str.find(sub, start)
#        if start == -1: return
#        yield start
#        start += len(sub)

#print(list(find_all(str,substr)))

print(20*'-' + 'End Q3' + 20*'-')

#%%
# =================================================================
# Class_Ex4:
# Write a function that read the first n lines of a file.
# Use test_1.txt as sample text.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q4' + 20*'-')


#def read_first_lins(data, n):
#    f = open(data,'r',encoding = 'utf-8')
#    return print(f.readlines(n))    
#
#read_first_lins("T1.txt", 4)
def read_lines(data, n): 
    f = open(data,'r',encoding = 'utf-8')
    head = [next(f) for x in range(n)]
    return print(head)

print(20*'-' + 'End Q4' + 20*'-')

#%%%
# =================================================================
# Class_Ex5:
# Write a function that read a file line by line and store it into a list.
# Use test_1.txt as sample text.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q5' + 20*'-')

with open('T1.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
print(lines)




print(20*'-' + 'End Q5' + 20*'-')
#%%
# =================================================================
# Class_Ex6:
# Write a function that read two text files and combine each line from first
# text file with the corresponding line in second text file.
# Use T1.txt and T2.txt as sample text.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q6' + 20*'-')







print(20*'-' + 'End Q6' + 20*'-')
# =================================================================
# Class_Ex7:
# Write a function that create a text file where all letters of English alphabet
# put together by number of letters on each line (use n as argument in the function).
# Sample output
# function(3)
# ABC
# DEF
# ...
# ...
# ...
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q7' + 20*'-')








print(20*'-' + 'End Q7' + 20*'-')
# =================================================================
# Class_Ex8:
# Write a function that reads a text file and count number of words.
# Note: USe test_1.txt as a sample text.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q8' + 20*'-')







print(20*'-' + 'End Q8' + 20*'-')
# =================================================================
# Class_Ex9:
# Write a script that go over over elements and repeat it each as many times as its count.
# Sample Output = ['o' ,'o', 'o', 'g' ,'g', 'f']
# Use Collections
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q9' + 20*'-')







print(20*'-' + 'End Q9' + 20*'-')
# =================================================================
# Class_Ex10:
# Write a program that appends couple of integers to a list
# and then with certain index start the the list over that index.
# Note: use deque
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q10' + 20*'-')









print(20*'-' + 'End Q10' + 20*'-')
# =================================================================
# Class_Ex11:
# Write a script using os command that finds only directories, files and all directories, files in a  path.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q11' + 20*'-')







print(20*'-' + 'End Q11' + 20*'-')
# =================================================================
# Class_Ex12:
# Write a script that create a file and write a specific text in it and rename the file name.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q12' + 20*'-')









print(20*'-' + 'End Q12' + 20*'-')
# =================================================================
# Class_Ex13:
#  Write a script  that scan a specified directory find which is  file and which is a directory.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q13' + 20*'-')









print(20*'-' + 'End Q13' + 20*'-')
# =================================================================








print(20*'-' + 'End Q15' + 20*'-')
# %%
