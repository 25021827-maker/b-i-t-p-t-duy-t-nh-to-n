n=int(input(""))
m=abs(n)
if m ==0:
    print("1")
else:
    dem=0
    while m>0:
        dem+=1
        m=m//10
    print(dem)


