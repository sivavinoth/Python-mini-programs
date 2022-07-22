# a=int(input('print number:'))
# for i in range(2,a):
#     if a%i !=0:
#         continue
#     else:
#         print("Its not a prime number")
#         break # here break is exicuted then it means else would not be exicuted.
# else:
#     print("Its a prime number")

lower_value = int(input ('Please, Enter the Lowest Range Value: '))
upper_value = int(input ('Please, Enter the Upper Range Value: '))

print ('The Prime Numbers in the range are: ')  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
           if (number % i) == 0:  
                break    
        else:  
            print (number)