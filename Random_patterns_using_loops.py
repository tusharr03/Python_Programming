num_1=[3,4,5,6,5,4,3]
for x_count in num_1:
    print('x' * x_count)

print("\n\n\n\n")

num_2=[7,6,5,8,7,4,2,1]
for x_count in num_2:
    print('X' * x_count) #this is a built in function only supported by python programming.
    # string is multiplied by an integer and hence the output is generated

print("\n\n\n\n")

#if pyhton doesn't have this type of function then we will use this method to print the following pattern
num_3=[2,3]
for x_count in num_3:
    output=''
    for count in range(x_count):
        output=output+'X'
    print(output)