def average(a,b): # type in 'average(a,b)' to return the average of those two numbers
    return (a+b)/2
# float() returns a decimal number
# int() returns a whole number
# strings are enclosed in single or double quotes, strings types are different from number types
# booleans are true/false values(<,>,==) greater than, less than, equal to
# type() tells you what data type or class you are working with
# use 'something = [a,b,c,...]' for lists, each item seperated by a comma or leave as '[]' to make an empty list
# use 'something.append(d)' to add 'd' to the list
# lists can hold all classes of data
# cannot add a list and a number
# use 'something.remove(d)' to remove d from the list, everything else stays in order
# You can print lists pg 28

name_list = ['Abe','Bob','Chloe','Daphne']
score_list = [55,63,72,84]

# Remember counting starts with 0
print(name_list[0], score_list[0])

n = 2
print(name_list[n], score_list[n+1])

for i in range(4):
    print(name_list[i], score_list[i])

for i, name in enumerate(name_list):
    print(name,"has index",i)

c = [4,True,'hello']
# Type in c[0] to return the value in list c, at index 0, which is 4

# Range of list items use (:) example myList[1:6] returns index items 1,2,3,4,5 which are values 2,3,4,5,6
# remember counting starts with 0 and the range syntax excludes the last index in this case index 6
myList=[1,2,3,4,5,6,7]

# If you dont specify the ending it will return all items from the first specified point to the end of the list including the last
# Access last items on a list using -1, -2 ect.
# To find the index of an item type in c.index('hello') to return the index place of the value in parenthesis, in this case it would be 2
# To see if an item is in a list type 'value in list' ex. '3 in c' would return False 'True in c' would return True
# Strings use these commands as well.
# len(d) tells us how many characters are in string d

running_sum = 0          # Create a variable
for i in range(10):      # Set a loop
    running_sum +=5      # What you want the loop to do
print(running_sum)       # Print result


def mySum(num):          # sigma n
    running_sum = 0
    for i in range(1,num+1):
        running_sum += i
    return running_sum

def mySum2(num):          # sigma n squared + 1
    running_sum = 0
    for i in range(num+1):
        running_sum += i**2 +1
    return running_sum

def averagenum(numlist):   # takes the sum of a list and divides it by the number of items in the list
    return sum(numlist)/len(numlist)

d = [53,28,54,84,65,60,22,93,62,27,16,25,74,42,4,42,15,96,11,70,83,97,75]

