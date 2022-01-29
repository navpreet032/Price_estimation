from tkinter import *

from database import Database 
from AmazonDb import Data_base
db=Database('Mydb.db')

AmazonDb=Data_base('Amazon.db')
FlipkartDb=Data_base('Flipkart.db')
OlXDb=Data_base('OLX.db')



window = Tk()

window.geometry("1349x756")
window.configure(bg = "grey")
canvas = Canvas(
    window,
    bg = "grey",
    height = 756,
    width = 1349,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
menuCanvas= Canvas(
    window,
    bg='#272727',
    height=750,
    width=200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    
)
menuCanvas.place(x=0,y=0)

def SetbestPrice():
 price=Bst_product[3] -(0.2*Bst_product[3])#20%off
 db.update(selected_item[0],Bst_product[1],Bst_product[2],price,Bst_product[4])
 addtolist()

def Algorithm(a=None):
 A_db=AmazonDb.fetch(a)
 F_db=FlipkartDb.fetch(a)
 O_db=OlXDb.fetch(a)  
 Mrp_A=922337203
 Mrp_F=922337203
 Mrp_O=922337203
 Age_A=0
 Age_F=0
 Age_O=0
 isPresent_A=''
 isPresent_F=''
 isPresent_O=''
 if(a!=None):
    if(len(A_db)!=0 and A_db[0][1]==a):
        Mrp_A=A_db[0][3]
        Age_A=A_db[0][4]
    else:
        isPresent_A=False
        Mrp_A=92233720

    if(len(F_db)!=0 and F_db[0][1]==a):
        Mrp_F=F_db[0][3]
        Age_F=F_db[0][4]
    else:
        isPresent_F=False
        Mrp_F=922337203

    if(len(O_db)!=0 and O_db[0][1]==a):
        Mrp_O=O_db[0][3]
        Age_O=O_db[0][4]
    else:
        isPresent_O=False
        Mrp_O=92233703

    
    #````````````````````````````````````````````````````    
    global Bst_product
    lowest_MRP=min(Mrp_A,Mrp_F,Mrp_O)
    print(lowest_MRP)
    #````````````````````````````````````````````````````  
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^>
    if(lowest_MRP==Mrp_A):
        Bst_product=A_db[0]
        Db_results.delete(0,END)
        Db_results.insert(END,["Provided By Amazon : ","Name = " +Bst_product[1],'Mrp = '+Bst_product[2]])
        Db_results2.delete(0,END)
        Db_results2.insert(END,["Price = " +str(Bst_product[3]),'Age = '+str(Bst_product[4])])
    elif(lowest_MRP==Mrp_F):
        Bst_product=F_db[0]
        Db_results.delete(0,END)
        Db_results2.delete(0,END)
        Db_results.insert(END,["Provided By Flipkart : ","Name = " + Bst_product[1],'Mrp = '+Bst_product[2]])
        Db_results2.insert(END,["Price = " +str(Bst_product[3]),'Age = '+str(Bst_product[4])])
    elif(lowest_MRP==Mrp_O):
        Bst_product=O_db[0]
        Db_results.delete(0,END)
        Db_results2.delete(0,END)
        Db_results.insert(END,["Provided By OLX : ", "Name = " +Bst_product[1],'Mrp = '+Bst_product[2]])
        Db_results2.insert(END,["Price = " +str(Bst_product[3]),'Age = '+str(Bst_product[4])])
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
    if(Mrp_A==Mrp_F and Mrp_A==Mrp_O):
       Bst_product=None
       Db_results.delete(0,END)
       Db_results2.delete(0,END)
       Db_results2.insert(END,"All database have same Price")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    else:
     if (Mrp_A==Mrp_F):
        if(Age_A<Age_F):
         Bst_product= A_db[0]#Amazon
         Db_results.delete(0,END)
         Db_results.insert(END,["Provided By Amazon : ","Name = " +Bst_product[1],'Mrp = '+Bst_product[2]])
         Db_results2.delete(0,END)
         Db_results2.insert(END,["Price = " +str(Bst_product[3]),'Age = '+str(Bst_product[4])])
        else:
            Bst_product=F_db[0]#Flipkart
            Db_results.delete(0,END)
            Db_results2.delete(0,END)
            Db_results.insert(END,["Provided By Flipkart : ","Name = " + Bst_product[1],'Mrp = '+Bst_product[2]])
            Db_results2.insert(END,["Price = " +str(Bst_product[3]),'Age = '+str(Bst_product[4])])

     if (Mrp_F==Mrp_O):
        if(Age_F<Age_O):
            Bst_product=(F_db[0])#Flipkart
            Db_results.delete(0,END)
            Db_results2.delete(0,END)
            Db_results.insert(END,["Provided By Flipkart : ", "Name = " +Bst_product[1],'Mrp = '+Bst_product[2]])
            Db_results2.insert(END,["Price = " +str(Bst_product[3]),'Age = '+str(Bst_product[4])])
        else:
             Bst_product=(O_db[0])#Olx
             Db_results.delete(0,END)
             Db_results2.delete(0,END)
             Db_results.insert(END,["Provided By OLX : ", "Name = " +Bst_product[1],'Mrp = '+Bst_product[2]])
             Db_results2.insert(END,["Price = " +str(Bst_product[3]),'Age = '+str(Bst_product[4])])

     if (Mrp_A==Mrp_O):
        if(Age_O<Age_A):
            Bst_product=(O_db[0])#Olx
            Db_results.delete(0,END)
            Db_results2.delete(0,END)
            Db_results.insert(END,["Provided By OLX : ", Bst_product[1],'Mrp = '+Bst_product[2]])
            Db_results2.insert(END,["Price = " +str(Bst_product[3]),'Age = '+str(Bst_product[4])])
        else:
            Bst_product=(A_db[0])#Amazon
            Db_results.delete(0,END)
            Db_results2.delete(0,END)
            Db_results.insert(END,["Provided By Amazon : ", Bst_product[1],'Mrp = '+Bst_product[2]])
            Db_results2.insert(END,["Price = " +str(Bst_product[3]),'Age = '+str(Bst_product[4])])
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^>
 else:
    Db_results2.delete(0,END)
    Db_results.delete(0,END)


def clr():
    Name_txt.delete(0,END)
    Name_txt.insert(END,selected_item[1])
    MRP_txt.delete(0,END)
    MRP_txt.insert(END,selected_item[2])
    Price_txt.delete(0,END)
    Price_txt.insert(END,selected_item[3])
    Age_txt.delete(0,END)
    Age_txt.insert(END,selected_item[4])
    


def addtolist():#Add's data to listbox1
    listbox1.delete(0,END)
    for data in db.fetch():
        listbox1.insert(END,data)
    
def selectitem(event):#Returns the index of selected item
    try:
     global selected_item
     index=listbox1.curselection()[0]
     selected_item=listbox1.get(index)
     print(selected_item[1])
     Algorithm(selected_item[1])
     Update_butt_2.configure(state=NORMAL)
     clr()#Refresh the list
    except IndexError:
        Algorithm()
        clr()
        Update_butt_2.configure(state=DISABLED)
        print('Item not present')
        
def removeFromDb():#Removes data from db
    db.remove(selected_item[0])
    clr()
    addtolist()

def updateDb():#Update data
    db.update(selected_item[0],Name_txt.get(),MRP_txt.get(),Price_txt.get(),Age_txt.get())
    addtolist()

def AddnewWin():#Add new window
    def insertToDB():#insert data into Db
      db.insert(P_name.get(),P_Mrp.get(),P_Price.get(),P_age.get())  
      addtolist()
     #/////////////////////////////////////////////////////////////\ 
    AddnewWIN= Toplevel(window)
    AddnewWIN.geometry("750x250")
    
    P_name=Entry(AddnewWIN,font=('helvetica',22,'bold'),bd=3,width=12)
    P_name.place(x=100,y=15)
    
    P_Mrp=Entry(AddnewWIN,font=('helvetica',22,'bold'),bd=3,width=12)
    P_Mrp.place(x=100,y=100)

    P_Price=Entry(AddnewWIN,font=('helvetica',22,'bold'),bd=3,width=12)
    P_Price.place(x=490,y=15)

    P_age=Entry(AddnewWIN,font=('helvetica',22,'bold'),bd=3,width=12)
    P_age.place(x=490,y=100)

    label_age=Label(AddnewWIN,text="Product Age   ").place(x=400,y=100)
    lable_Pname=Label(AddnewWIN,text="Productname   ").place(x=10,y=20)
    lable_Pprice=Label(AddnewWIN,text="Price ").place(x=400,y=18)
    lable_Pname=Label(AddnewWIN,text="MRP ").place(x=10,y=110)
    save_button=Button(AddnewWIN,text="Save",command=insertToDB).place(x=600,y=200)
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
AddnewButton=Button(window,bg="#222222",fg='grey',bd=0,padx=40,height=1,text="Add new",command=AddnewWin)
AddnewButton.place(x=20,y=14)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  

def lightMode():
    
    canvas.configure(bg='white')
    window.configure(bg='white')
    Theme_menu.configure(bg='white' ,fg='black')
    file_menu.configure(bg='white',fg='black')
def darkMode():
    canvas.configure(bg='grey')
    window.configure(bg='grey')
    Theme_menu.configure(bg='#222222',fg='grey')
    file_menu.configure(bg='#222222',fg='grey')
#code for menubar
menubar = Menu(window)
#/////////////////////////////////////////////////////
file_menu=Menu(menubar,background='#222222',foreground='grey')
menubar.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label='settings')
file_menu.add_separator()
file_menu.add_command(label='Exit',command=window.quit)
#//////////////////////////////////////////////////////
Theme_menu=Menu(menubar,background='#222222',fg='grey')
menubar.add_cascade(label="Theme",menu=Theme_menu)
Theme_menu.add_command(label='LIGHT',command=lightMode)
Theme_menu.add_command(label='DARK',command=darkMode)
window.config(menu=menubar )
#/////////////////////////////////////////////////////\



# searchBar_img= PhotoImage( file=("assests/searchBG.png"))

# searchBar_BG = canvas.create_image(
#     800,#x
#     32,#y
   
#     image=searchBar_img
# )



#div For products::::::::::::::::::::::::::::::::::::::::::::
div1=Frame(window,height=590,width=900,bg='#272727',cursor='trek')
div1.place(x=350,y=200)




Details_txt=Label(div1,text="Name Price MRP Productage",bg='#272727',fg='white',font=('helvetica',12,'bold')).place(x=5,y=0)
listbox1=Listbox(div1,bg='#272727',width=60,height=35,foreground='grey',borderwidth=0)
listbox1.place(x=10,y=20)
listbox1.bind('<<ListboxSelect>>',selectitem)

L_Name_txt=Label(div1,text="Productname",bg='#272727',fg='white',font=('helvetica',12,'bold')).place(x=550,y=53)
Name_txt=Entry(div1,font=('helvetica',10),bd=3,width=20,bg='#272727',fg='white')
Name_txt.place(x=680,y=50,height=25)

L_MRP_txt=Label(div1,text="MRP  ",bg='#272727',fg='white',font=('helvetica',12,'bold')).place(x=550,y=119)
MRP_txt=Entry(div1,font=('helvetica',10),bd=3,width=20,bg='#272727',fg='white')
MRP_txt.place(x=680,y=120,height=25)

L_Price_txt=Label(div1,text="Price ",bg='#272727',fg='white',font=('helvetica',12,'bold')).place(x=550,y=183)
Price_txt=Entry(div1,font=('helvetica',10),bd=3,width=20,bg='#272727',fg='white')
Price_txt.place(x=680,y=180,height=25)

L_Age_txt=Label(div1,text="Product Age  ",bg='#272727',fg='white',font=('helvetica',12,'bold')).place(x=550,y=233)
Age_txt=Entry(div1,font=('helvetica',10),bd=3,width=10,bg='#272727',fg='white')
Age_txt.place(x=680,y=230,height=25)

Yearsold_txt=Label(div1,text="years old  ",bg='#272727',fg='white',font=('helvetica',8,'bold')).place(x=780,y=233)

Delete_butt=Button(div1,bg="#222222",fg='grey',bd=0,padx=40,height=1,text="Delete",command=removeFromDb)
Delete_butt.place(x=750,y=500)

Update_butt=Button(div1,bg="#222222",fg='grey',bd=0,padx=40,height=1,text="Update",command=updateDb)
Update_butt.place(x=600,y=500)

Db_results=Entry(div1,font=('helvetica',10),bd=0,width=55,bg='#272727',fg='white')
Db_results.place(x=500,y=300)
Db_results2=Entry(div1,font=('helvetica',10),bd=0,width=55,bg='#272727',fg='white')
Db_results2.place(x=500,y=350)

Update_butt_2=Button(div1,bg="#222222",fg='grey',bd=0,padx=40,height=1,text="Set Best Price",command=SetbestPrice)
Update_butt_2.place(x=400,y=500)
addtolist()
window.resizable(True, True)
window.mainloop()
