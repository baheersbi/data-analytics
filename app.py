# a = 90
# print(a)
a = input("Please enter the first number:")
b = input("Please enter the second number:")
print("Please select the operator:")
# print(op[2])
op = ["Addition", "Subtraction", "Multiplication", "Division"]
i =1
for x in op:
    print(str(i) +". " + x)
    i=i+1

op = input("Your choice:")
if op=="1":
    print("The sum of these two numbers:" + str(int(a) + int(b)))
elif op=="2":
    print("The subtraction of these two numbers:" + str(int(a) - int(b)))
elif op=="3":
    print("The multiplication of these two numbers:" + str(int(a) * int(b)))
else:
    print("The division of these two number:" + str(int(a) / int(b)))
# for x in op:
#     if x=="Multiplication":
#         break
#     print(x)

# for x in op:
#     if x=="Multiplication":
#         continue
#     print(x)

# print(op[2])
# print(len(op))


