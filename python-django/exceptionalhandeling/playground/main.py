

a = "abc"

try:
    print(a[10])
    # print(int(a))
except Exception as e:
    print(f"Internval Server Error : {e}")

# a = "abc"

# try:
#     print(a[10])
#     # print(int(a))
# except ValueError:
#     print("Please pass integer values")
# except IndexError:
#     print("please choose index less than len of string")