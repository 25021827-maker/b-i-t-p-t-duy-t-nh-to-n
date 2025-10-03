n=int(input("số điện: "))
if n<=50:
    print("tiền điện là: ",n*1500)
elif 50<n<=100:
    print("tiền điện là: ",50*1500+(n-50)*2000)
else:
    print("tiền điện là: ",50*2500+(n-100)*3000)