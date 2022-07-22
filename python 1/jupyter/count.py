def count(n):
    count=0
    while(n>0):
        count=count+1
        n=n//10
    print("The number of digits in the number are:",count)

count(12345678123456781)