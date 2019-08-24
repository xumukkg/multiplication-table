a = int(input("Input the range: \n > "))
print("{: ^3}".format(" "), end ='')

for i in range(1, a):
    print("{: ^5}".format(i), end = " ")
print()
for i in range(1,a):
    print(i, end  ="  ")
   
    for j in range(1, a):

        print("{: ^5}".format(i*j), end = " ")
    print()    


