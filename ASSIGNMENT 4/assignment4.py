# Suggest a map for country since we didnt use api to location to valid a cities
mapp=("Tripoli","Akkar","Jbeil","tyre","saida","beirut","zahle","batroun","nabtih","Jounieh",
      "Baalbek","Kfarshima","Ghaziyeh","Aley","Baabda")

#Add a new city to the company
def add_city(company_city):
    city_exist = False
    company_city_exist = False
    company_city = company_city
    print()
    print ("The Cities That You Can Added To Company Cities That Can You Added To DRIVER: ")
    for m in mapp:
     print(m, end=' ')
    print()
    print()
    city_name = input("Enter the name of the city: ")
  
    #Check if the city in the map of country to accept it 
    for i in mapp:
      if i.lower()==city_name.lower():
         city_exist = True
    for j in company_city :      # Check if city is added before to cities that deliver to it
      if j.lower() == city_name.lower():  
         company_city_exist=True     
    
    if city_exist == True:        #after checkin we add a new city
       if company_city_exist == False:
          company_city.append(city_name)
       else :
          print("City Is Already Exits") 
    else:
       print ("The City Is Not Valid For These Company")
   
    return company_city
#*****************************************************************************************
# Add a new driver and their route
def add_driver_route(company_city,drivers):
    company_city = company_city
    drivers = drivers
    name = False
    driver_city=[]
    answer = 1000
    driver_name = input("Enter the first name of the driver : ")
    x = driver_name.isalpha()     # check if their is sapces number or any chacracter other alphabet
    #Check if driver is added before
    for i in drivers:
       if i.lower() == driver_name.lower():
          name = True
    if x == True :      
     if name == False:
       while  answer != '2':        # add the cities to the route of drivers
         print ("Company Cities Can Choose It: ")
         for m in company_city:
          print(m, end=' ')
         print()
         print()
         company_city_exist = False
         driver_city_exist = False  
         print("\nEnter:")
         print("1. Add a New City For " + driver_name +" Route : ")
         print("2. Finish Adding Route For "+ driver_name)
         answer = (input("Your choice: "))  
         
         if answer =='1':          
            cityname = input("Enter The Name Of City: ")
            for j in company_city :
                if j.lower() == cityname.lower():
                   company_city_exist = True
                   
            for k in driver_city :      #check if city added before to driver route
                if k.lower() == cityname.lower():
                    driver_city_exist = True
                   
            if company_city_exist == True : # add city after checking
               if driver_city_exist == False:
                  driver_city.append(cityname) 
               else:
                  print ("The City Is Already Added In The Route") 
            else:  
                print ("The City Is Not Found In The Company Cities Please Add It Before")
        
         elif answer =='2':          # Check if we Add a driver with no route of cities   
             if len(driver_city) > 0:  # will not add the driver
                 drivers[driver_name] = driver_city
             else:
                 print ("Since Their Is No City Added To The Route The Driver Will Not Added ")
         else:
             print("Invalid choice. Please choose a valid option.")
     else:
       print("The Driver Is Exist Go And Update By Adding And Removing From Their Route.")
    else:
        print("Invalid name Please try agian") 
    
    return drivers
#*********************************************************************************************
def add_new_city_for_route(company_city,drivers):# modify the route of driver by adding new cities
    company_city = company_city
    drivers = drivers
    driver_cities=[]
    company_city_exist = False
    driver_city_exist = False 
    name=False
    driver_name = input("Enter the name of the driver : ")
    for i in drivers:             #check if driver in dictionary to add city to him
        if i.lower() == driver_name.lower():
           driver_cities=  drivers[driver_name]
           name = True
    print ("Company Cities Can Choose It: ")
    for m in company_city:
     print(m, end=' ')
    print()
    print() 
    if name == True:
       
       cityname = input("Enter The Name Of City That You Want To Add It In The Route : ") 
       print ("The Order Of The Cities To The Driver "+ driver_name +" : ")
       m=1
       for k in driver_cities: 
          print (str(m) +" : "+ k)
          m= m + 1
          if k.lower() == cityname.lower():    # check if city added before to driver
             driver_city_exist = True 
       for j in company_city:
          if j.lower() == cityname.lower():
            company_city_exist = True       
       if driver_city_exist == False:
          if company_city_exist == True:
             print("\nEnter:")                #add city as the user want
             print(" 1. To Add It To The Beginning Of The Route.")
             print("-1. To Add It To The End Of The Route.")
             print("Enter A Number Choosed Behind The Cities To Be The index Of New City In The Route. ")
             answer = (input("Your choice: ")) 
             if answer =='1' :
                 driver_cities.insert(0, cityname)
             elif answer == '-1' :
                 driver_cities.append(cityname)
             elif answer > '0' or answer < str(len(driver_cities)-1) :
                 num = (int(answer) - 1)
                 driver_cities.insert(num, cityname)
             else:
                 print("Invalid choice. Please choose a valid option.")  
          else:
               print("The City Is Not Found In The Company Cities Please Add It Before.") 
       else:
          print("The City Is Already Added In The Route.") 
    else:
       print("The Driver Is Not Found Go And Add The Driver And Their Route.")
    return drivers
#*********************************************************************************************
 # modify the route by deleting cities of drivers
def remove_city(company_city,drivers):
    company_city = company_city
    drivers = drivers
    driver_cities=[]
    driver_name = input("Enter the name of the driver : ")
    cityname = input("Enter The Name Of City That You Want To Remove From The Route : ")
    driver_city_exist = False
    name=False
    for i in drivers:   # check if city  and driver is found to delete city
      if i.lower() == driver_name.lower():
        driver_cities = drivers[driver_name]
        name=True
    for j in driver_cities:
       if j.lower() == cityname.lower():
        driver_city_exist=True 
    
    if name == True and driver_city_exist == True :
        if len(driver_cities) == 1:         # check if delete last city in the route 
            drivers.pop(driver_name)        # if last city remove it we delete the driver also
        else:    
          driver_cities.remove(cityname) 
          drivers[driver_name] =  driver_cities
    elif name == True and driver_city_exist == False:
       print ("The City Is Not Found To Romve It.") 
    else:
       print ("The Driver Not Found") 
    return drivers   
#********************************************************************************************
   # check if the city is avialble to deliver to it 
def available_driver (company_city,drivers,driver_available):
    company_city_exist = False
    city_exist = False
    company_city = company_city
    driver_available =driver_available
    drivers = drivers
    cityname = input("Enter The Name Of City That You Want To Deliver To It : ")
    for i in company_city:               #check if city in company cities and search if any driver
       if i.lower() == cityname.lower(): #has these city in their route
          company_city_exist = True
    if company_city_exist == True :
        
       for k in drivers: # 
         for j in drivers[k] :
           if cityname.lower() == j.lower():
             driver_available.append(k)
             city_exist = True
       if city_exist == False:
           print ("Their IS NO Driver Deliver To These City.")
       else:
           print ("The Drivers Deliver To These City are:")
    else:
        print ("The City Is Not Found In Company Cities.")        
             
    return driver_available         
#****************************************************************************************
def mainMenu():
  company_city=['beirut','saida']
  drivers={}
  drivers["alex"]=["saida","beirut"]
  driver_available=[]
  choice=-99 # dummy value
  while choice !='6':
    driver_available=[]  
    print("\nEnter:")
    print("1. To add a city")
    print("2. To add a driver")
    print("3. To add a city to the route of a driver")
    print("4. Remove a city from a driver’s route")
    print("5. To check the deliverability of a package")
    print("6. To Close The Program")
    choice = (input("Your choice: "))
    if choice == '1':
       company_city = add_city(company_city)
       print("Company City: ")
       for i in company_city:
           print(i)
       
    elif choice == '2':
         drivers = add_driver_route(company_city,drivers)
         for m in drivers: 
           print()
           print(m, end=" : ")
           for j in drivers[m] :
             print(j, end=" , ")
           
    elif choice == '3':
         drivers = add_new_city_for_route(company_city,drivers)
         for m in drivers: 
           print()
           print(m, end=" : ")
           for j in drivers[m] :
             print(j, end=" , ")
    elif choice == '4':
         drivers = remove_city(company_city,drivers)
         for m in drivers: 
           print()
           print(m, end=" : ")
           for j in drivers[m] :
             print(j, end=" , ")
    elif choice == '5':
          driver_available = available_driver (company_city,drivers,driver_available)
          for i in driver_available:
              print(i)     
    elif choice == '6': 
         print("GoodBye!!!")
    else:
         print("Invalid choice. Please choose a valid option.")




mainMenu()