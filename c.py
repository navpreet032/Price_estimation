from AmazonDb import Data_base 
db=Data_base('OLX.db')
db.insert("Swift Dzire","1000000",600000,3)
db.insert('Honda city',"1200000",500000,12)
db.insert('LG Washing Machine',"30000",13000,2)
db.insert('Mg Washing Machine',"32000",25000,1)
db.insert('Hero Bicycle',"5000",800,3)
db.insert('Awm Bicycle',"5000",1500,2)
db.insert('Sports Bicycle',"10000",4000,1)
db.insert('Lady cycle',"5000",500,1)
db.insert('MG Car',"2500000",1000000,11)#10 lkh
db.insert('Tata Tiago',"1500000",400000,2)
db.insert('Innova Crysta',"2100000",1000000,6)
db.insert('Zebronics Mouse',"1000",110,1)
db.insert('Zebronics Keyboard',"1000",160,1)
db.insert('Giga PC',"15000",5000,2)
db.insert('AMD Redon',"20000",7000,2)
db.insert('AMD Ryzen7',"22000",14000,3)
db.insert('Hp laptop',"30000",12000,2)
db.insert('acer laptop',"32000",1800,1)
db.insert('Asus laptop',"35000",12000,2)
db.insert('Lg mobile',"15000",9000,3)
db.insert('Iphone5',"30000",12000,2)
db.insert('Iphone10',"35000",15000,2)
db.insert('Iphone12',"100000",50000,1)
db.insert('Samsung galaxy',"25000",12000,2)
db.insert('Poco p2',"20000",8000,2)
db.insert('Tata AC',"35000",18000,2)
db.insert('Ogen AC',"35000",1300,1)
db.insert('Ro',"10000",1200,3)
db.insert('Fan',"2500",200,1)
db.insert('Lamp',"1000",80,1)






# A_db=AmazonDb.fetch(a)
    # F_db=FlipkartDb.fetch(a)
    # O_db=OlXDb.fetch(a)
    # global PriceIn_A 
    # global PriceIn_F
    # global PriceIn_O
    # #--------------------------------
    # if(len(A_db)!=0):
    #  if(a==A_db[0][1]):
    #     PriceIn_A=A_db[0][3]
    #     #print('AAAA')
        
    # else:
    #     PriceIn_A=922337203
    # #--------------------------------    
    # if(len(F_db)!=0):
    #  if(a==F_db[0][1]):
    #     PriceIn_F=F_db[0][3]
    #     #print('FFFF')
    # else:
    #     PriceIn_F=922337203
    # #--------------------------------
    # if(len(O_db)!=0):
    #  if(a==O_db[0][1]):
    #     PriceIn_O=O_db[0][3]
    #    #print('OOO')
    # else:
    #     PriceIn_O=922337203    
    # #--------------------------------

    # #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # if(len(A_db)!=0):
    #  if(A_db[0][3]==min(PriceIn_A,PriceIn_F,PriceIn_O)):
    #     print('A')
    # #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    
    # if(len(F_db)!=0):
    #  if(F_db[0][3]==min(PriceIn_A,PriceIn_F,PriceIn_O)):
    #     print('F')
    # #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # if(len(O_db)!=0):    
    #  if(O_db[0][3]==min(PriceIn_A,PriceIn_F,PriceIn_O)):
    #     print('o')
    # #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # if(A_db[0][3]==F_db[0][3]):#A==B
    #     if(A_db[0][4]>F_db[0][4]):
    #         #Return
    # if(A_db[0][3]==F_db[0][3]):#A==C