

items=[["tomato",1],["potato",2],["chocolate",3],["soap",0.5],["pepsi",1]] 
choosed_items=[]

def addItem():
    choice=-99 # dummy value
    while choice !=2:
      print("Enter")
      print("1. To Add A New Item")
      print("2. Go Back To CheckOut!!")
      
      choice=int(input())
      if choice==1:
         item_name = input("Enter The Name of The Item: ")
         item_quantity = int(input("Enter The Quantity: "))
       
         for choosen_item in items:
             choosen_it =choosen_item[0]
             if item_name.lower() == choosen_it.lower():   
                 if len(choosed_items) > 0:                
                     for comper_item in choosed_items:
                         index = choosed_items.index(comper_item)
                         comper_it, comper_qyt=comper_item
                         if item_name.lower() == comper_it.lower():
                            comper_qyt += item_quantity
                            comper_item=comper_it, comper_qyt
                            choosed_items[index]=comper_item
                            break
                         else:
                            new_item = [item_name, item_quantity]
                            choosed_items.append(new_item)
                            break
                 else:
                     new_item = [item_name, item_quantity]
                     choosed_items.append(new_item)
                 break
             else:
                 print("Item Is Unavailable")
                  
      elif choice ==2:
        print("Back To CheckOut!!")
      else:
        print("Invalid Input") 
          
def checkTotal():
   total_bill = 0.0 
   if len(choosed_items) == 0:
      total_bill = 0.0
      return total_bill
   else:
      for name_item in choosed_items:
         item_checkname, item_quantit = name_item
         for iteme in items:
             name , price = iteme
             if item_checkname == name:
                item_price = price * item_quantit
                total_bill +=item_price
                print(" ITEM : " + item_checkname+" ||QTY : " + str(item_quantit)+" ||Price Of Item: "+str(price) +" ||Total Per Item :" +str(item_price)+" $ ")
   return total_bill
         
def addCoupon(): 
        coupons = 0.0
        coupon_value = float(input("Enter The Value Of The Coupon: "))  
        coupons = coupon_value
        return coupons
def checkout(x):
    total = checkTotal()
    Coupon = x
    print("Total Of The Order (Without Coupons):", total)
    print("Total Of The Coupons:", Coupon)
    total_to_pay = total - Coupon
    print("Total To Pay:", total_to_pay)   
    choosed_items.clear()
   
def newOrder():
  choice=-99 # dummy value
  Coupon=float()
  while choice !=4:
    print("Enter")
    print("1. To Add An item")
    print("2. To Check The Total")
    print("3. To Add A Coupon")
    print("4. To Checkout")

    choice=int(input())
    
    if choice==1:
       addItem()
    elif choice ==2:
      total = checkTotal()
      print("The Total Of Your Bill Is", total)
    elif choice ==3:  
      Coupon = addCoupon()
      print("Coupon Of "+ str(Coupon) +" $ Added.")
    elif choice ==4:
        if Coupon > 0 :
           checkout(Coupon)
        else:
           checkout(0.0) 
    else:
       print("Invalid Input")


def mainMenu():
  choice=-99 # dummy value
  while choice !=2:
    print("Enter")
    print("1. To Start A New Order")
    print("2. To Close The Program")
    
    choice=int(input())
    
    if choice==1:
      print("Starting A New Order...")
      newOrder()
    elif choice ==2:
      print("Bye Bye")
    else:
      print("Invalid Input")
      
      
mainMenu()

