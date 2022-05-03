# import sys

# randomlist = ['a', 0, 2]
# for each_entry in randomlist:
#     try:
#         print("The entry is : ", each_entry)
#         r = 1/int(each_entry)
#         break

#     except:
#         print("OOps...!!! ", sys.exc_info()[2], " occured")
#         print()
#         print("Next Entry : ")
#         print()

# print("the reciprocal of : ", each_entry , " is ", r)



# import sys
# random = ['a',0,2]
# for entry in random:
#     try:
#         print("The entry is : ", entry)
#         r = 1/int(entry)
#         break
#     except Exception as e:
#         print("an error - ", e.__class__, " occured")



# a= "malav"
# b= True

# print(a.__class__)
# print(b.__class__)

# class human:
#     pass #this keyword is used to execute nothing.......blank....
# n = human()

# print(type(n))
# print(n.__class__)



try:
    a = input("Enter first number : ")
    b = input("Enter second number : ")
    result = int(a)/int(b)

except (ValueError):
    print("User has given the wrong input.")
else:
    print("Result is squared : ", result**2)
finally:
    print("ANyway this block will be always executed . ")



a = "python is good"
# print(a.isalnum)
# print(a.isupper)

print("everything is fine : " .format(a))