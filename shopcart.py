import random
captchalist=["AxcDVz","erTHJ","WdfBM"]
bag=[]
price=[]
priceofnuts=500
priceoffruits=200
priceofov=300
priceoffridge=50000
priceoftv=70000
priceofmobile=30000
priceofwh=1000
priceofmb=1000
priceofclock=2000
print("hello welcome to shopkart")
print("happy shopping :) :) ok first lets check out whats there in store ")
print("1) groceries")
print("2) electronic gadjects")
print("3) home decors")
print("enter 1 to continue shopping, any other number to exit")
c=int(input())
while(c==1):
	a=int(input("select the required category: or enter 0 to quit shopping "))                            #a is the required category
	if(a==0):
		break
    if(a==1):
		print("it seems like you ran short of GROCERIES at your home :0 ")
		print("well, no issues, available products : 1) nuts 2) fresh fruits 3) organic vegetables")
		b=input("select what you need: ")
		if(b=="nuts"):
			print("the price is : 500/-,discount=10%")
			n=float(priceofnuts*(10/100))
			priceofnuts=priceofnuts-n
			print(float(priceofnuts))
			price.append(priceofnuts)
			bag.append("nuts")
		elif(b=="freshfruits"):
			print("the price is :200/-,discount=10%")
			f=float(priceoffruits*(10/100))
			priceoffruits=priceoffruits-f
			print(float(priceoffruits))
			price.append(priceoffruits)
			bag.append("freshfruits")	
		elif(b=="organicvegetables"):
			print("the price is :300/-,discount=10%")
			v=float(priceofov*(10/100))
			priceofov=priceofov-v
			print(float(priceofov))
			price.append(priceofov)
			bag.append("organicvegetables")
		else:
			print("sorry such product doesnot exist")
    if(a==2):
		print("woah in need of some electronic gadjects,here they are 1)fridge 2)tv 3)mobile")
		d=input("ok select what you need:")
		if(d=="fridge"):
			print("the price is : 50000,dicount=10%")
			r=float(priceoffridge*(10/100))
			priceoffridge=priceoffridge-r
			print(float(priceoffridge))
			price.append(priceoffridge)
			bag.append("fridge")
		elif(d=="tv"):
			print("the price is: 70000/-,discount=10%")
			t=float(priceoftv*(10/100))
			priceoftv=priceoftv-t
			print(float(priceoftv))
			price.append(priceoftv)
			bag.append("tv")
		elif(d=="mobile"):
			print("the price is:30000/-,discount=10%")
			m=float(priceofmobile*(10/100))
			priceofmobile=priceofmobile-m
			print(float(priceofmobile))
			price.append(priceofmobile)
			bag.append("mobile")
		else:
			print("sorry such product doesnt exist :)")
    if(a==3):
		print("home decors it is;), 1)wallhanging 2)minibulb 3)clock")
		e=input("slect one: ")
		if(e=="wallhanging"):
			print("the price is 1000/-,discount=10%")
			w=float(priceofwh*(10/100))
			priceofwh=priceofwh-w
			print(float(priceofwh))
			price.append(priceofwh)
			bag.append("wallhanging")
		elif(e=="minibulb"):
			print("the price is :1000/-,discount=10%")
			h=float(priceofmb*(10/100))
			priceofmb=priceofmb-h
			print(float(priceofmb))
			price.append(priceofmb)
			bag.append("minibulb")
		elif(e=="clock"):
			print("the price is :2000/-,discount=10%")
			l=float(priceofclock*(10/100))
			priceofclock=priceofclock-l
			print(float(priceofclock))
			price.append(priceofclock)
			bag.append("clock")
		else:
			print("sorry such product doesnt exist")
    else:
        print("sorry such category doesnot exist")
print("this is your shopping bag" ,bag)
print("this is the respective price list of each object" ,price)
computer=random.choice(captchalist)
print("enter the captch for billing:",computer)
customer=input()
if(customer==computer):
    a=len(price)
    totalprice=0
    for i in range(0,a):
	    totalprice=totalprice+price[i]
    print("the toal price is: ",totalprice)
else:
    print("sorry the given input is wrong")
    














































		
