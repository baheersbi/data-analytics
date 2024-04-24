# a = 90
# print(a)
# a = input("Please enter the first number:")
# b = input("Please enter the second number:")
# print("Please select the operator:")
# # print(op[2])
# op = ["Addition", "Subtraction", "Multiplication", "Division"]
# i =1
# for x in op:
#     print(str(i) +". " + x)
#     i=i+1
#
# op = input("Your choice:")
# if op=="1":
#     print("The sum of these two numbers:" + str(int(a) + int(b)))
# elif op=="2":
#     print("The subtraction of these two numbers:" + str(int(a) - int(b)))
# elif op=="3":
#     print("The multiplication of these two numbers:" + str(int(a) * int(b)))
# else:
#     print("The division of these two number:" + str(int(a) / int(b)))


# Let's modify your existing calculator program to include a loop that will continue
# asking the user if they want to perform more operations until they decide to stop.

while True:
    a = input("Please enter the first number: ")
    b = input("Please enter the second number: ")
    print("Please select the operator:")
    op = ["Addition", "Subtraction", "Multiplication", "Division"]
    for i, x in enumerate(op, start=1):
        print(f"{i}. {x}")

    op_choice = input("Your choice: ")
    if op_choice == "1":
        print("The sum of these two numbers: " + str(int(a) + int(b)))
    elif op_choice == "2":
        print("The subtraction of these two numbers: " + str(int(a) - int(b)))
    elif op_choice == "3":
        print("The multiplication of these two numbers: " + str(int(a) * int(b)))
    elif op_choice == "4":
        try:
            print("The division of these two numbers: " + str(int(a) / int(b)))
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice. Please select a valid operator.")

    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        print("Good bye!")
        break

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


