from datetime import datetime

name=input("Enter Your Name:")
#lists of items
lists='''
Rice    Rs 20000/kg
Sugar   RS 30/kg
Salt    Rs 2/kg
Oil     Rs 200/kg
paneer  Rs 2000/kg
maggi   Rs 20/kg
Boost   Rs 205/kg
'''
#declaration purpose
price=0
pricelist=[]
totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]
#rates for items
items={'Rice':20000,
       'sugar':30,
       'salt':2,
       'oil':200,
       'paneer':2000,
       'maggi':20,
       'Boost':205
       }
option= int(input("for list of items press 1: "))
if option==1:
    print(lists)
for i in range(len(items)):
    input1=int(input("if you want to add press 1 or 2 for exit:"))
    if input1==2:
        break
    if input1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice * 5) / 100
            finalamount = gst + totalprice
        else:
            print("Entered item is not available")
    else:
        print("Entered wrong number")
    inp = input("can i bill the items YES or NO:")
    if inp == 'YES':
        pass
        if finalamount != 0:
            print(25*"=","Dmart",25*"=")
            print(28*" ","Warangal")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*'',ilist[i],3*'',qlist[i],8*" ",plist[i])
            print(78*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalamount:','Rs',finalamount)
            print(75*"-")
            print(20*" ",'Thanks for visiting')
            print(75*"-")
