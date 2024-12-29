dictionary = {'Codingal': 1, 'After':2, 'Class':3, 'Project':4}
print("The original dictionary : " + str(dictionary))

value = int(input("Enter a value"))
res = 0
for key in dictionary:
    if dictionary[key] == value:
        res = res + 1

print("Frequency of the value is : " + str(res))