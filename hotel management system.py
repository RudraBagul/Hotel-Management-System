import random as rand

class Hotel:
    __bill=0
    def __init__(self,name):
        self.__name=name
        self.greet()
        
    def greet(self):
        print(f"Welcome to our hotel {self.__name}")
        print("How can I help you")
        menu=(input("Enter yes to see menu or enter no :"))
        if menu=="yes" or menu=="Yes" or menu=="YES":
            self.menu()
        else:
            print("Thankyou for visiting our hotel")
    def menu (self):
        print()
        self.my_menu=input("\"Menu\"\nEnter 1 for Veg Platter\nEnter 2 for Rice Plate\nEnter 3 for Dal Tadka\nEnter 4 for Biryani\nEnter 5 for Veg Pulao\nEnter your order:")
        if int(self.my_menu)<1 or int(self.my_menu)>5:
            print("You entered wrong input")   
        else:
            self.amount()
    def amount(self):
        if self.my_menu=="1":
            print("You have orderd Veg Platter")
            print("Prise of  Veg Platter:100 Rs")
            Hotel.__bill+=100
            #print("your bill",Hotel.bill)
            # print(f"your current bill is {Hotel.bill}Rs")
            order=(input("If you like to order more enter yes or no:"))
            if order=="yes" or order=="Yes" or order=="YES":
                print()
                self.menu()
                
            elif order=="no" or order=="No" or order=="NO":
                print("Your order is taken")
                print(f"Your current bill is {Hotel.__bill}Rs")
                print()
                self.bill_split()

            else:
                print("you entered wrong input")
            
                

        elif self.my_menu=="2":
            #half plate
            half=input("Do you want half palte of Rice Plate Yes or No:")
            if half=="yes" or half=="Yes" or half=="YES":
                print("You have orderd half plate of Rice Plate")
                print("Prise of  Rice Plate:50 Rs")
                Hotel.__bill+=50
                order=(input("If you like to order more enter yes or no:"))
                if order=="yes" or order=="Yes" or order=="YES":
                    self.menu()
                    print()
                elif order=="no" or order=="No" or order=="NO":
                    print("Your order is taken")
                    print(f"Your current bill is {Hotel.__bill}Rs")
                    print()
                    self.bill_split()
                    
                else:
                    print("you entered wrong input")
            #full plate
            elif half=="no" or half=="No" or half=="NO":
                print("You have orderd Rice Plate")
                print("Prise of  Rice Plate:100 Rs")
                Hotel.__bill+=100
                order=(input("If you like to order more enter yes or no:"))
                if order=="yes" or order=="Yes" or order=="YES":
                    self.menu()
                    print()
                elif order=="no" or order=="No" or order=="NO":
                    print("Your order is taken")
                    print(f"Your current bill is {Hotel.__bill}Rs")
                    print()
                    self.bill_split()
                   
                else:
                    print("you entered wrong input")

        elif self.my_menu=="3":
            #half plate
            half=input("Do you want half palte of Dal Tadka Yes or No:")
            if half=="yes" or half=="Yes" or half=="YES":
                print("You have orderd half plate of Dal Tadka")
                print("Prise of  Dal Tadka:50 Rs")
                Hotel.__bill+=50
                order=(input("If you like to order more enter yes or no:"))
                if order=="yes" or order=="Yes" or order=="YES":
                    self.menu()
                    print()
                elif order=="no" or order=="No" or order=="NO":
                    print("Your order is taken")
                    print(f"Your current bill is {Hotel.__bill}Rs")
                    print()
                    self.bill_split()
                    
                else:
                    print("you entered wrong input")

            #full plate
            elif half=="no" or half=="No" or half=="NO":
                print("You have orderd Dal Tadka")
                print("Prise of  Dal Tadka:100 Rs")
                Hotel.__bill+=100
                order=(input("If you like to order more enter yes or no:"))
                if order=="yes" or order=="Yes" or order=="YES":
                    self.menu()
                    print()
                elif order=="no" or order=="No" or order=="NO":
                    print("Your order is taken")
                    print(f"Your current bill is {Hotel.__bill}Rs")
                    print()
                    self.bill_split()
                    
                else:
                    print("you entered wrong input")

        elif self.my_menu=="4":
            #half plate
            half=input("Do you want half palte of Biryani Yes or No:")
            if half=="yes" or half=="Yes" or half=="YES":
                print("You have orderd half plate of Biryani")
                print("Prise of  Biryani:50 Rs")
                Hotel.__bill+=50
                order=(input("If you like to order more enter yes or no:"))
                if order=="yes" or order=="Yes" or order=="YES":
                    self.menu()
                    print()
                elif order=="no" or order=="No" or order=="NO":
                    print("Your order is taken")
                    print(f"Your current bill is {Hotel.__bill}Rs")
                    print()
                    self.bill_split()
                    
                else:
                    print("you entered wrong input")

            #full plate
            elif half=="no" or half=="No" or half=="NO":
                print("You have orderd Biryani")
                print("Prise of  Biryani:100 Rs")
                Hotel.__bill+=100
                order=(input("If you like to order more enter yes or no:"))
                if order=="yes" or order=="Yes" or order=="YES":
                    self.menu()
                    print()
                elif order=="no" or order=="No" or order=="NO":
                    print("Your order is taken")
                    print(f"Your current bill is {Hotel.__bill}Rs")
                    print()
                    self.bill_split()
                    
                else:
                    print("you entered wrong input")

        elif self.my_menu=="5":
            #half plate
            half=input("Do you want half palte of Veg Pulao Yes or No:")
            if half=="yes" or half=="Yes" or half=="YES":
                print("You have orderd half plate of Veg Pulao")
                print("Prise of Veg Pulao:50 Rs")
                Hotel.__bill+=50
                order=(input("If you like to order more enter yes or no:"))
                if order=="yes" or order=="Yes" or order=="YES":
                    self.menu()
                    print()
                elif order=="no" or order=="No" or order=="NO":
                    print("Your order is taken")
                    print(f"Your current bill is {Hotel.__bill}Rs")
                    print()
                    self.bill_split()
                else:
                    print("you entered wrong input")

            #full plate
            elif half=="no" or half=="No" or half=="NO":
                print("You have orderd Veg Pulao")
                print("Prise of  Veg Pulao:100 Rs")
                Hotel.__bill+=100
                order=(input("If you like to order more enter yes or no:"))
                if order=="yes" or order=="Yes" or order=="YES":
                    self.menu()
                    print()
                elif order=="no" or order=="No" or order=="NO":
                    print("Your order is taken")
                    print(f"Your current bill is {Hotel.__bill}Rs")
                    print()
                    self.bill_split()
                
                else:
                    print("you entered wrong input")
        else:
            print("You entered wrong input")
        

    def bill_split(self):
        bill=Hotel.__bill
        tip=float(input("enter the tip?"))
        print(f"Your current bill is {Hotel.__bill}Rs and tip is {tip}")
        intrest_no=input("do you want to split bill or one will pay enter  \"yes:split\"  or  \"no:one will pay\" : ")

        if intrest_no=="no":
            friends=["rudra","falguni","swati","mahesh","mangala"]
            person=(rand.randint(0,4))
            if person == 0:
                print("rudra will pay the bill")
                print()
            elif person == 1:
                print("falguni will pay the bill")
                print()
            elif person == 2:
                print("swati will pay the bill")
                print()
            elif person == 3:
                print("mahesh will pay the bill")
                print()
            else:
                print("mangala will pay the bill")
                print()
            print(f"pay amount (Bill is {Hotel.__bill}Rs and Tip is {tip}) Totle: {bill+tip}")
            print("THANKYOU FOR VISITING OUR HOTEL ....")
            print("IF YOU LIKE THAN PLEASE VISIT AGAIN.....")
            

        elif intrest_no=="yes":
            #with persent tip
            split=int(input("enter the split?"))
            tip_perct=(tip/100)
            total=(bill+(bill*tip_perct))
            one_person_bill=(total/split)
            print(f"each person should pay roundoffly  {round(one_person_bill)}")
            print(f"each person should pay {(one_person_bill)}")

            print("THANKYOU FOR VISITING OUR HOTEL ....")
            print("IF YOU LIKE THAN PLEASE VISIT AGAIN.....")

        else:
            print("You entered wrong input")
        
name=input("Enter your name:")
p1=Hotel(f"{name}")