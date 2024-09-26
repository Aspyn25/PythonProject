countries = ["Brazil","Canada","Columbia", "Ecuador", "Iran"]
print(countries[:3])
print(countries[3:])

first = countries[0]
countries[0] = countries[1]
countries[1] = first
print(countries)

languages = ["C", "C++", "Python", "Java", "JavaScript"]
languages.append("SQL")
print(languages)

# + : concatenate (combine)
# 'nested' lists
students = [[1,"John", "Canada"],[2,"Max","USA"],[3,"Peter","UK"]]
print(students[2][1])

#list comprehension
