# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:31:09 2022

@author: malgo
"""
to_buy_eq = {}
bought_eq = {}
bill = []
while
try:
    budget =  int(input("how much money you want to spend on this eq?:"))
except ValueError:
    print(f"{budget} is too abstract, use numeric value")
    budget =  int(input("how much money you want to spend on this eq?:"))

bill_sum = None
choice = 666
class home_eq():
    
    
    def __init__(self, name, price, quantity = 1):
        
        self.name = name
        self.price = pricedog
        
        self.quantity = quantity
        global bill
    
    def add_to_dict(self, proper_dict, bought_container):
        if self.name not in bought_container:
            if self.quantity == 1:
                proper_dict[self.name] = self.price
                bill.append(self.price)
                return proper_dict, bill
        
            else:
                proper_dict[self.name] = self.price * self.quantity
                bill.append(self.price)
                return proper_dict
        else:
            print("You already had this element in the bought_eq. Do you want to continue? [press y/n]")
    
    def current_bill(self):
        global bill_sum
        bill_sum = sum(bill)
        print(f"Your current bill is {bill_sum} pln")
    
    def current_budget(self):
        global budget 

        print(f"Your current budget is {budget} pln")
    
    def pay(self, to_buy, bought):
        global budget, bill_sum
        bill_sum = sum(bill)
        budget -= bill_sum
        bill.clear()
        bill_sum = sum(bill)
        bought.update(to_buy)
        to_buy.clear()
        print(f"Your current budget is {budget} pln and bill is {bill_sum}")

    def check_bought(self, bought_container):
        
        for key, value in bought_container.items():
            print(f"{key}: {value}")
        print(f"In total. {len(bought_container.keys())} elements bought. {sum(bought_container.values())} money spent")



while choice != 0:
    print("\nChoose number:\n 1. Add new object to bag\n 2. Check current bill\n 3. Check walllet\n 4. Buy and clear bag\n 5. See your purchased items\n 6. Remove items from the bag\n 0. Exit")
    choice = int(input("Your choice:"))
    if choice == 1:
        product = input("Set a name of product you want to buy:")
        price = int(input("Set a price of product you want to buy:"))
        home_object = home_eq(product, price)
        home_object.add_to_dict(to_buy_eq, bought_eq)
        print(f"\n{home_object.name} was added to bag")
        choice = 666
    elif choice == 2:
        try:
            home_object.current_bill()
        except NameError:
            print("Your bag is empty, your current bill is 0 pln")
    elif choice == 3:
        try:
            home_object.current_budget()
        except NameError:
            print(f"Your current budget is {budget} pln")
    elif choice == 4:
        try:
            home_object.pay(to_buy_eq, bought_eq)
        except NameError:
            print("Your bag is empty you do not have to paid for it")