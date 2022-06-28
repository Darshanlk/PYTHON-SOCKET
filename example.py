
withdraw,balance=input().split()
if int(withdraw)%5==0 and (int(withdraw)+0.5)<=float(balance):
    print(float(balance)-int(withdraw)-0.5)
else:
    print(balance)