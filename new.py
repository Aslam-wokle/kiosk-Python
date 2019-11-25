"""
Author: Muhammad Aslam Hamdi Bin Amran
Date: 28-10-2019
"""
import numpy as np
import os, datetime

date = datetime.date.today()

master_dir = os.path.join(os.getcwd(),"MASTER")+"--"+date.strftime("%d %B %Y")
sell_dir = os.path.join(master_dir,"SALES")+"--"+date.strftime("%d %B %Y")
buy_dir = os.path.join(master_dir,"RESTOCK")+"--"+date.strftime("%d %B %Y")

if not os.path.exists(master_dir):
    os.makedirs(master_dir)
    
    if not os.path.exists(sell_dir) and not os.path.exists(buy_dir):
        os.makedirs(sell_dir)
        os.makedirs(buy_dir)        
    else:
        pass    
else:
    pass

master_R = []
master_qty = []
sell_R = []
sell_qty = []
buy_R = []
buy_qty = []
item = []

a = np.genfromtxt('item.txt',delimiter = ',',dtype = str)

class stock:
    
    def __init__(self, code, description, stock_level, min_stock, max_stock, buying_price, selling_price):

        self.code = int(code)
        self.description = description
        self.stock_level = int(stock_level)
        self.min_stock = 5
        self.max_stock = 25
        self.buying_price = float(buying_price)
        self.selling_price = float(selling_price)
        self_profit = float(0)

    def display():
        
        print("-------Wokle Kiosk--------")
        print()
        print("CODE:DESCRIPTION:   STOCK:    PRICE:")

        for r in range(24,len(a)):
            for c in a:
                print(c[0],"%-14s"%c[1],"%09s"%c[2],"%09s"%c[6])


    def sell(self):

        print("Stock available for ",self.description," is ",self.stock_level,"\n")
        if int(self.stock_level) > 0:
            qty = int(input("How many "+self.description+" need to sell?\n"))
            sell_qty.extend([qty])
            master_qty.extend([qty])
            print()
            a[self.code-1][2] = int(self.stock_level) - qty
            if int(self.stock_level) - qty < 0:
                print(self.description,"is not available for that quantity")
                print()
                print(self.description)
                print("Stock: ",self.stock_level)
                a[self.code-1][2] = int(self.stock_level)
                print()
            elif int(self.stock_level) - qty >= 0:
                self.stock_level = int(a[self.code-1][2])
                total = qty * self.selling_price
                print()
                print(qty,self.description,"will be RM",total,"\n")
                sell_R.extend([self.code])
                master_R.extend([self.code])

        elif self.stock_level <=0:
            print("Sorry!!",self.description,"is already out of stock")
            print()

    def buy(self):        

        print("Restock quantity must be at least 1")
        print()
        qty = int(input("""How much you want to restock for """+self.description+"?\n"
                    """(Press 0 to cancel)"""+"\n"))
        buy_qty.extend([qty])

        if qty != 0:
            a[self.code-1][2] = int(self.stock_level) + qty
            self.stock_level = a[self.code-1][2]
            print()
            print(self.description,"has",self.stock_level,"of stock")
            print()
            total= self.buying_price * qty
            print(qty,self.description,"will be RM",total,"\n")
            buy_R.extend([self.code])
            
        else:
            print("\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n")

def buy_receipt():

    i = 0
    total = 0
    count = len(buy_R)
    tmp = 0
    with open("wokle.txt",'r',encoding = "utf-8") as f:
#"D:/Unikl/Semester 5/OOP/Python/Kiosk/RESTOCK/BUY_"+str(b.code)+"--"+str(date)+".txt","wt",encoding = "utf-8") as f1:
        with open(buy_dir+"/BUY_"+str(b.code)+"--"+str(date)+".txt","wt",encoding = "utf-8") as f1:
            for line in f:
                f1.write(line)

            print("""
--------------------#RECEIPT#------------------------

CODE:DESCRIPTION:   QUANTITY:    PRICE/unit:    TOTAL:
""")
            f1.write("\n")
            while i < count:

                for r in range(count):
                        x = int(buy_R[r])
                        qty = int(buy_qty[r])
                        b_price = float(a[x-1][5])
                        price = qty*b_price
                        x1 = ("{:.2f}".format(price))
                        print(a[x-1][0],"%-14s"%a[x-1][1],"%12s"%qty,"%13s"%a[x-1][5],"%09s"%price)
                        f1.write(str(a[x-1][0])+"%10s"%str(a[x-1][1])+"%012s"%(str(qty))+"%016s"%(str(a[x-1][5]))+"%015s"%(str(x1)))
                        f1.write("\n")
                        tmp += price
                        i = i+1
            print()
            print("Overall Total: RM",tmp)
            print("""
--------------------THANK YOU !!!--------------------
""")
            f1.write("\nOverall Total: RM"+str(tmp))

            f1.write("""

--------------------THANK YOU !!!--------------------            
        """)
    buy_R.clear()
    b.plus()

def sell_receipt():

    i = 0
    total = 0
    count = len(sell_R)
    tmp = 0
    with open("wokle.txt",'r',encoding = "utf-8") as f:
#"D:/Unikl/Semester 5/OOP/Python/Kiosk/SELL/SELL_"+str(s.code)+"--"+str(date)+".txt","wt",encoding = "utf-8") as f1:
        with open(sell_dir+"/SALES_"+str(s.code)+"--"+str(date)+".txt","wt",encoding = "utf-8") as f1:
            for line in f:
                f1.write(line)
            print("""
--------------------#RECEIPT#------------------------

CODE:DESCRIPTION:   QUANTITY:    PRICE/unit:    TOTAL:
""")
            f1.write("\n")
            while i < count:

                for r in range(count):
                        x = int(sell_R[r])
                        qty = int(sell_qty[r])
                        s_price = float(a[x-1][5])
                        price = qty*s_price
                        x1 = ("{:.2f}".format(price))
                        print(a[x-1][0],"%-14s"%a[x-1][1],"%12s"%qty,"%13s"%a[x-1][6],"%09s"%price)
                        f1.write(str(a[x-1][0])+"%10s"%str(a[x-1][1])+"%012s"%(str(qty))+"%016s"%(str(a[x-1][6]))+"%015s"%(str(x1)))
                        f1.write("\n")
                        tmp += price
                        i = i+1
            print()
            print("Overall Total: RM",tmp)
            print("""
--------------------THANK YOU !!!--------------------
""")
            f1.write("\nOverall Total: RM"+str(tmp))

            f1.write("""

--------------------THANK YOU !!!--------------------           
        """)
    sell_qty.clear()
    sell_R.clear()
    s.plus()
    
def master_receipt():

    i = 0
    total = 0
    count = len(master_R)
    #with open("wokle.txt",'r',encoding = "utf-8") as f:
#"D:/Unikl/Semester 5/OOP/Python/Kiosk/RESTOCK/BUY_"+str(b.code)+"--"+str(date)+".txt","wt",encoding = "utf-8") as f1:
    with open("master.txt",'r',encoding = "utf-8") as f:
        with open(master_dir+"/MASTER_"+"--"+str(date)+".txt","wt",encoding = "utf-8") as f1:
            for line in f:
                f1.write(line)
                
            f1.write("\n")
            while i < count:

                for r in range(count):
                    x = int(master_R[r])
                    qty = int(master_qty[r])
                    s_price = float(a[x-1][6])
                    b_price = float(a[x-1][5])
                    price_s = float(("{:.2f}".format(qty*s_price)))
                    price_b = float(("{:.2f}".format(qty*b_price)))
                    profit = float(("{:.2f}".format(price_s-price_b)))
                    f1.write(str(a[x-1][0])+"%14s"%str(a[x-1][1])+"%14s"%str(qty)+"%14s"%str(price_b)+"%12s"%str(price_s)+"%12s"%str(profit))
                    f1.write("\n")
                    total += profit
                    i = i+1

            f1.write("\nOverall Total: RM"+str(total))
            f1.write("""

-------------------------#THANK YOU#--------------------------------           
        """)
    master_qty.clear()
    master_R.clear()
    
class reciept:
    def __init__ (self,code):
        self.code=code

    def plus(self):
        self.code+=1
b=reciept(0)
s=reciept(0)
             
def menu():

    print("""
    Assalamualaikum !!!

                    Hajimemashite !!!
""")
    print("""
    (づ｡◕‿‿◕｡)づ           (づ｡◕‿‿◕｡)づ
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    █░░░░░░░░▀█▄▀▄▀██████░▀█▄▀▄▀██████
    ░░░░ ░░░░░░░▀█▄█▄███▀░░░ ▀█▄█▄███

              イらっしゃい
       Welcome to Wokle's Kiosk!!!
         """)
    x = True
    while x:
        #stock.receipt()
        
        print("""
         _______________________
        |0. Exit                |
        |1. Display all items   |
        |2. Sell items          |
        |3. Buy items(Restock)  |
        |4. Closing             |
        |_______________________|
        """)

        x = int(input("Please enter your choice: "))
        print()        
    
        if x == 1:
            print()
            stock.display()

        elif x == 2:
            
            while 1:
                print("CODE:DESCRIPTION:   STOCK:    PRICE:")
        
                for r in range(24,len(a)):
                    for c in a:
                        print(c[0],"%-14s"%c[1],"%09s"%c[2],"%09s"%c[6])
                print()

                sold = int(input("Please enter the item's code need to sell (Press 0 to exit to main menu): "))
                print()
                if sold != 0:

                    if sold in range(26):
                        item[sold-1].sell()
                    else:
                        print("Code you enter is not in range Okyaku-sama !")
                        print()

                elif sold == 0:
                    ask = input("Do you need a receipt? (y/n): ")
                    print()

                    if ask == 'y':
                        sell_receipt()

                    elif ask == 'n':
                        sell_qty.clear()
                        sell_R.clear()
                        pass
                    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌ ホンク
    ───▄▄ █  WokLe Courier services        ホンク ! !
    ███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌  
    ▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀(@)▀  Out For Delivery !!!
                    """)
                    break

        elif x == 3:
            while 1:
                i = 0
                print("---Restock List---")
                print()
                print("CODE:DESCRIPTION:   STOCK:    PRICE/unit:")

                for r in range(24,len(a)):
                    r = 0
                    for c in a:
                        lvl = int(a[r][2])

                        if (lvl < 5):
                            x = 0
                            x = r
                            print(a[x][0],"%-14s"%a[x][1],"%09s"%a[x][2],"%09s"%a[x][5])

                        elif (lvl > 5):
                            pass
                    
                        r += 1
                        i += 1
                print()
                print("---------------------------------------------------------------------")
                new = int(input("Please enter the item's code to restock (Press 0 to exit to main menu): "))
                print()
                if new != 0:
                    if new in range(26):
                        item[new-1].buy()
                    else:
                        print("Please enter a valid value Okyaku-sama !")
                        print()

                elif new == 0:
                    ask = str(input("Do you need a receipt? (y/n): "))
                    #print(buy_dir)
                    if ask == 'y':
                        buy_receipt()
                        
                    elif ask == 'n':
                        buy_qty.clear()
                        buy_R.clear()
                        pass
                        
                    print("""
    ⠀⠀⠀⠀⠀ (\__/)⠀
    ⠀⠀⠀⠀⠀ (•ㅅ•)⠀⠀My NAAAAAME is
       ＿ノ⠀ヽ⠀ノ＼＿⠀⠀Gyoubu Masataka
      /  Y⠀⌒Ｙ⌒⠀Ｙ⠀ヽ⠀⠀ONIWA!
     |⠀  (三ヽ人⠀⠀/⠀⠀ |
     |⠀  ﾉ⠀¯¯\⠀￣￣ヽノ  As I breathe,
     ヽ＿＿＿⠀⠀＞､＿／ i shall let no one
     ⠀⠀ ｜⠀(⠀王⠀)〈  pass the stock gate ! !
     ⠀⠀ /⠀⠀ﾐ`——彡⠀\   
                    """)
                    x = True
                    break

        elif x == 4:
            while 1:
                print("""
         _______________________
        |0. Exit                |
        |1. Show drawer         |
        |2. Close Drawer        |
        |_______________________|
        """)

                x = int(input("Please enter your choice: "))
                print()
                if x == 1:
                    i = 0
                    total = 0
                    count = len(master_R)
                    print("""
-----------------------#MASTER RECEIPT#-----------------------------

CODE:DESCRIPTION:   QUANTITY:    BUY PRICE:  SELL PRICE:     PROFIT:
""")
                    while i < count:

                        for r in range(count):
                            x = int(master_R[r])
                            qty = int(master_qty[r])
                            s_price = float(a[x-1][6])
                            b_price = float(a[x-1][5])
                            price_s = float(("{:.2f}".format(qty*s_price)))
                            price_b = float(("{:.2f}".format(qty*b_price)))
                            profit = float(("{:.2f}".format(price_s-price_b)))
                            print(a[x-1][0],"%-14s"%a[x-1][1],"%12s"%qty,"%13s"%price_b,"%12s"%price_s,"%10s"%profit)
                            total += profit
                            i = i+1
                    print()
                    print("Overall Profit: RM",total)
                    print("""
-------------------------#THANK YOU#--------------------------------
""")

                elif x == 2:
                    ask = str(input("Are you sure want to close the drawer? (y/n) :"))
                    print()
                    if ask == 'y':
                        master_receipt()
                        print("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿  Drawer has been close!!
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⠒⠀⢀⡔⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢹⣿⣿   Lets Go
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠁⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿      Home !!!
⣿⣿⣿⣿⣿⠿⠟⠛⠛⠓⢄⡀⠀⢂⠀⠀⠀⠀⠠⡀⡌⠀⠀⠀⠀⠀⠀⢰⣿⣿
⣿⣿⣿⣿⢁⠄⢀⠀⠀⠀⠀⠈⠢⡄⠁⠀⢀⣀⠀⠘⠀⠀⠀⠀⡀⠀⣠⣾⣿⣿
⣿⣿⣿⣿⣯⡂⠀⠀⠀⠀⡀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⡠⠔⡞⣡⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣦⡠⠈⢦⡀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⢄⣾⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣆⢢⣿⣄⡀⠀⠀⠀⢐⠀⠀⡀⢐⠆⣹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣄⡄⠀⠈⠀⠀⠁⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡁⢘⣿⣿⣿⣿⣿⡀⢀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡸⣿⣿⠏⠻⠟⠀⡌⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⡋⠀⠀⠀⠠⠐⠉⠀⠀⢀⠨⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠆⠀⠀⠀⡀⠄⠀⠀⠈⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠏⠀⠀⢠⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠻⠿⣿⣿⣿⣿
⣿⣿⡿⠛⠉⠀⠀⠀⠀⠈⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿
⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻
""")                        
                        break
                    
                    elif ask == 'n':
                        pass
                    
                elif x == 0:
                    x = True
                    break
                
                else:
                    print("Please enter a valid choice Okyaku-Sama !")  
        
        elif x == 0:

            f = open("item.txt","+w")
            r = 0
            for r in range(24,len(a)):
                for c in a:
                    f = open("item.txt","+a")
                    f.write(str(c[0])+","+str(c[1])+","+str(c[2])+","+str(c[3])+","+str(c[4])+","
                            +str(c[5])+","+str(c[6])+"\n")

            print("""
        サようなら        Sayonara!
        ジャ, また あした  Thank YOU !!
        
            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄███████▀▀▀▀▀▀███████▄
         ▐████▀▒.BYE..▒▒▒▒▀██████▄
         ███▀▒▒▒▒..SEE.▒▒▒▒▒▀█████
         ▐██▒▒▒▒▒▒.YOU..▒▒▒▒▒▒████▌
         ▐█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▌
          █▒▄▀▀▀▀▀▄▒▒▄▀▀▀▀▀▄▒▐███▌
           ▐░░░▄▄░░▌▐░░░▄▄░░▌▐███▌
         ▄▀▌░░░▀▀░░▌▐░░░▀▀░░▌▒▀▒█▌
         ▌▒▀▄░░░░▄▀▒▒▀▄░░░▄▀▒▒▄▀▒▌
         ▀▄▐▒▀▀▀▀▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒█
           ▀▌▒▄██▄▄▄▄████▄▒▒▒▒█▀
            ▄██████████████▒▒▐▌
           ▀███▀▀████▀█████▀▒▌
             ▌▒▒▒▄▒▒▒▄▒▒▒▒▒▒▐
             ▌▒▒▒▒▀▀▀▒▒▒▒▒▒▒▐
                  """)
            x = None
            break
                        
        else:
            print("Please enter a valid choice Okyaku-Sama !")        

for x in range(25):
    item.append(stock(a[x][0],a[x][1],a[x][2],a[x][3],a[x][4],a[x][5],a[x][6]))

menu()


