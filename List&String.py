# list
# 1
list1 = [1,2,3,4,5]
print(list1[2])

# 2
list1.append(6)
print(list1)
list1.pop(1)
print(list1)

# 3
list2 = [10,20,30,40,50,60,70,80,90,100]
print(list2[:5])
print(list2[7:])
print(list2[::2])

# 4
list3 = [1,2,3,4,5,6,7,8,9,10]
print(sum(list3))
print(list3[-1],list3[0])

# 5
print([x**2 for x in list3])

#6
list4 = [[1,2,3],[4,5,6],[7,8,9]]
print(list4[1][1])

# string
# 1
string1 = "Hello, World!"
print(string1[0],string1[-1])

# 2
string2 = "Python Programming"
print(string2.split()[0])
print(string2.split()[1])

# 3
print(string2.upper())
print(string1.replace("World", "Python"))

# 4
print("Hello" + " " + "World")

# 5
string3 = "apple,banana,cherry"
print(string3.split(","))

#6
name = "Aspyn"
age = 24
print(f"My name is {name} and I am {age} years old")

#7
name = input("Write your name : ")
print(name[::-1])

# Bonus 1
palindrome = input("write the words :")
if palindrome == palindrome[::-1]:
    print(f"{palindrome} is a palindrome.")
else:
    print(f"{palindrome} is not a palindrome.")

# Bonus 2
list5 = ["P","y","t","h","o","n"]
print("".join(list5))