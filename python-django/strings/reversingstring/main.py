string = "madam"
# print(string)
# print(string[::-1])

# if string == string[::-1]:
#     print(f"{string} is palindrome")
# else:
#     print(f"{string} is not palindrome")
# reversing string
rev_str = ""
for i in range(len(string)-1,-1,-1):
    # print(string[i])
    rev_str += string[i]
print(rev_str)


if string == rev_str:
    print(f"{string} is palindrome")
else:
    print(f"{string} is not palindrome")


# str1 = "abc"
# str2 = "def"
# str3 = str1 + str2
# print(str3)