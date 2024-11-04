#-improting libaries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

#Creates a main window where it will contain all the widgest for GUI and assigns the window to a varibale called "root"
#It as well specifies on how big the window for the application should be
root = Tk()
root.geometry('700x600')

#Creates and then Connects to the database file that stores the information of inventories every time the prorgam is run
conn = sqlite3.connect('Cave_Gallery_Inventory.db')
c=conn.cursor()

#Creates a tabel within the database that contains 6 fields that will hold the information of the inventories
#(this part of code only needs to be run once so the table is created and it is saved within the database).
'''
c.execute("""CREATE TABLE Cave_Gallery_Inventories (
        IDnumber number,
        Date text,
        Description text,
        Price float,
        Category text,
        Status text
        )""")    
'''

# Function that opens a new widget when the user selects to add inventory
def Add_Inventory():

    global Inventory_IDnumber
    global Inventory_Date
    global Inventory_Description
    global Inventory_Price
    global Inventory_Category
    global Inventory_Status

    # Creates a new frame when the user selcted the sub menu to add inventory
    adding_inventory_frame= Frame(root, width= 650, height=300)
    #Background colour of the frame
    adding_inventory_frame['background'] = '#c5d2d7'
    # Placement of the frame
    adding_inventory_frame.grid(row=2, column=0)
    adding_inventory_frame.grid_propagate(False)

    Label(adding_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 1)
    Label(adding_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 2)
    
    # Lables for the 6 fields that will show what information must be inserted in the entry next to it
    Label(adding_inventory_frame, text = 'Entry ID number', bg = '#f6f8f9', width = 24).grid(row = 4, column = 0)
    Label(adding_inventory_frame, text = 'Date of entry',bg = '#f6f8f9', width = 24).grid(row = 6, column = 0)
    Label(adding_inventory_frame, text = 'Item Description',bg = '#f6f8f9', width = 24).grid(row = 8, column = 0)
    Label(adding_inventory_frame, text = 'Price',bg = '#f6f8f9', width = 24).grid(row = 10, column = 0 )
    Label(adding_inventory_frame, text = 'Category',bg = '#f6f8f9', width = 24).grid(row = 12, column = 0 )
    Label(adding_inventory_frame, text = 'Status',bg = '#f6f8f9', width = 24).grid(row = 14, column = 0 )

    # Entries for the 6 fields where the user will input the information of the inventory 
    Inventory_IDnumber = ttk.Entry(adding_inventory_frame, width = 28)
    Inventory_Date = ttk.Entry(adding_inventory_frame, width = 28)
    Inventory_Description = ttk.Entry(adding_inventory_frame, width = 28)
    Inventory_Price = ttk.Entry(adding_inventory_frame, width = 28)
    Inventory_Category = ttk.Combobox(adding_inventory_frame, width = 25) 
    Inventory_Category['values'] = ('Furniture', ' Technology',' Music')
    Inventory_Status = ttk.Combobox(adding_inventory_frame, width = 25) 
    Inventory_Status['values'] = ('Sale', 'Reserved',' Sold')

    #Telling the program where to put the entries for the 6 fields
    Inventory_IDnumber.grid(row = 4,column = 1)
    Inventory_Date.grid(row = 6, column = 1)
    Inventory_Description.grid(row = 8, column = 1)
    Inventory_Price.grid(row = 10, column = 1)
    Inventory_Category.grid(row = 12, column = 1)
    Inventory_Status.grid(row = 14, column = 1)

    # Button for the user when they have inputted all of the information of the inventory into the entries
    ttk.Button(adding_inventory_frame, text = 'Confirm', command= submit).grid(row= 14, column=5)

#Function to add the data of the inventory into the database after the button was pressed
def submit():



    #Connects to the database that stores the information of inventories
    conn = sqlite3.connect('Cave_Gallery_Inventory.db')
    c=conn.cursor()

    # Gets and inserts the information inside the variables that was inputted in the 6 entries to the 6 fields in Cave_Gallery_Inventories database
    c.execute("INSERT INTO Cave_Gallery_Inventories Values (:IDnumber, :Date, :Description, :Price, :Category, :Status)",
              {
               
                  'IDnumber': Inventory_IDnumber.get(),
                  'Date': Inventory_Date.get(),
                  'Description': Inventory_Description.get(),
                  'Price': Inventory_Price.get(),
                  'Category': Inventory_Category.get(),
                  'Status':Inventory_Status.get()
              })
        
    conn.commit()

    # Deletes the text that was inputted into the 6 entries after data has be inputted into the database
    Inventory_IDnumber.delete(0, 'end')
    Inventory_Date.delete(0, 'end')
    Inventory_Description.delete(0, 'end')
    Inventory_Price.delete(0, 'end')
    Inventory_Category.delete(0, 'end')
    Inventory_Status.delete(0, 'end')

    # Message Box that will display that the infromation that has been inputted has been saved
    messagebox.showinfo(title = "Confirmation", message = "Inventory has been added")

# Function to opens a new widget when the user selects to display inventory
def Display_Inventories():

    global Search_IDnumber


    # Creates a new frame when the user selcted the sub menu to display inventory
    display_inventory_frame= Frame(root, width= 650, height=300)
    display_inventory_frame['background'] = '#c5d2d7'
    display_inventory_frame.grid(row=2, column=0)
    display_inventory_frame.grid_propagate(False)

    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 1)
    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 2)

    # Label to tell the user to insert the ID of the inventory if they want to display infromation of a specific inventory
    Label(display_inventory_frame, text = 'Search Inventory by ID', bg = '#f6f8f9', width=20).grid(row = 3, column = 1)

    # Entry for the user to insert the ID of the specific inventory
    Search_IDnumber = ttk.Entry(display_inventory_frame, width = 20)
    Search_IDnumber.grid(row = 3, column = 2)
    
    #Button when the user inputted the ID of the specific inventory they want to search 
    ttk.Button(display_inventory_frame, text = 'Search Inventory', command= search).grid(row= 3, column=3)

    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 4, column = 1)

    #Button when the user wants to display the information of all the inventoires in the database 
    ttk.Button(display_inventory_frame, text = 'Show Inventory', command= display, width=24).grid(row= 5, column=1)

# Function that opens a new widget when the user presses the button to display sepcific inventory
def search():

    
    # Creates a new frame when the user selcted to display the infomration of the specific inventory
    display_inventory_frame= Frame(root, width= 650, height=300)
    display_inventory_frame['background'] = '#c5d2d7'
    display_inventory_frame.grid(row=2, column=0)
    display_inventory_frame.grid_propagate(False)

    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 5, column = 1)
    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 5, column = 2)
    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 5, column = 3)
    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 5, column = 4)
    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 5, column = 5)
    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 5, column = 6)

    # Lables to tell the user which information belongs to which field after the information has been displayed of the specific inventory 
    Label(display_inventory_frame, text = 'ID number', bg = '#e2e8ec', width=12).grid(row = 6, column = 1, padx=10)
    Label(display_inventory_frame, text = 'Date of entry', bg = '#e2e8ec', width = 12).grid(row = 6, column = 2, padx=10)
    Label(display_inventory_frame, text = 'Item Description', bg = '#e2e8ec', width = 12).grid(row = 6, column = 3, padx=10)
    Label(display_inventory_frame, text = 'Price', bg = '#e2e8ec', width = 12).grid(row = 6, column = 4 , padx=10)
    Label(display_inventory_frame, text = 'Category', bg = '#e2e8ec', width = 12).grid(row = 6, column = 5, padx=10 )
    Label(display_inventory_frame, text = 'Status', bg = '#e2e8ec', width = 12).grid(row = 6, column = 6, padx=10)

    #Connects to the database that will store the information    
    conn = sqlite3.connect('Cave_Gallery_Inventory.db')
    c=conn.cursor()
    record_id= Search_IDnumber.get()

    # Select all the information that belongs to the inventory ID that the user inputted in the entry
    c.execute("SELECT * FROM Cave_Gallery_Inventories WHERE IDnumber = " + record_id)
    records = c.fetchall()

    # Variables to store the values of each data of the specific inventories
    Search_ID_record = ''
    Search_Date_record = ''
    Search_Description_record = ''
    Search_Price_record = ''
    Search_Category_record = ''
    Search_Status_record = ''

    #Loop through record inside database and insert the data into the variable
    for record_ in records:
        Search_ID_record += str(record_[0])
        Search_Date_record += str(record_[1])
        Search_Description_record +=  str(record_[2])
        Search_Price_record += str(record_[3])
        Search_Category_record +=  str(record_[4])
        Search_Status_record +=  str(record_[5])

    
        
    #Creates Lables to display the informationm of the specific invenotry
    Search_ID_records_label = Label(display_inventory_frame, text = Search_ID_record, bg = '#ffffff', width = 12)
    Search_ID_records_label.grid(row = 7, column = 1)
    
    Search_Date_records_label = Label(display_inventory_frame, text = Search_Date_record, bg = '#ffffff', width = 12)
    Search_Date_records_label.grid(row = 7 , column = 2)

    Search_Description_records_label = Label(display_inventory_frame, text = Search_Description_record, bg = '#ffffff', width = 12)
    Search_Description_records_label.grid(row = 7 , column = 3)

    Search_Price_records_label = Label(display_inventory_frame, text = Search_Price_record, bg = '#ffffff', width = 12)
    Search_Price_records_label.grid(row = 7 , column = 4)

    Search_Category_records_label = Label(display_inventory_frame, text = Search_Category_record, bg = '#ffffff', width = 12)
    Search_Category_records_label.grid(row = 7 , column = 5)

    Search_Status_records_label = Label(display_inventory_frame, text = Search_Status_record, bg = '#ffffff',width = 12)
    Search_Status_records_label.grid(row = 7 , column = 6)






    conn.commit()


# Function that opens a new widget when the user selects to display all the inventories
def display():

    # Creates a new frame when the user selcted to display the infomration of all the inventories
    display_inventory_frame= Frame(root, width= 650, height=300)
    display_inventory_frame['background'] = '#c5d2d7'
    display_inventory_frame.grid(row=2, column=0)
    display_inventory_frame.grid_propagate(False)
    
    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 1)
    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 2)
    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 3)
    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 4)
    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 5)
    Label(display_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 6)

    # Lables to tell the user which information belongs to which field after the information has been displayed of the inventoryies
    Label(display_inventory_frame, text = 'Entry ID number', bg = '#e2e8ec').grid(row = 3, column = 1, padx=10)
    Label(display_inventory_frame, text = 'Date of entry', bg = '#e2e8ec', width = 12).grid(row = 3, column = 2, padx=10)
    Label(display_inventory_frame, text = 'Item Description', bg = '#e2e8ec', width = 12).grid(row = 3, column = 3, padx=10)
    Label(display_inventory_frame, text = 'Price', bg = '#e2e8ec', width = 12).grid(row = 3, column = 4 , padx=10)
    Label(display_inventory_frame, text = 'Category', bg = '#e2e8ec', width = 12).grid(row = 3, column = 5, padx=10 )
    Label(display_inventory_frame, text = 'Status', bg = '#e2e8ec', width = 12).grid(row = 3, column = 6, padx=10)

    
    #Connects to the database that stores the information
    conn = sqlite3.connect('Cave_Gallery_Inventory.db')
    c=conn.cursor()

    #Select all the information of all the inventories inisde the databse
    c.execute("SELECT *, oid FROM Cave_Gallery_Inventories")
    records = c.fetchall()


    # Variables to store the values of each data of all the inventories
    ID_record = ''
    Date_record = ''
    Description_record = ''
    Price_record = ''
    Category_record = ''
    Status_record = ''

    #Loop through each record inside database and insert the data into the variable
    for record_ in records:
        ID_record += str(record_[0]) + "\n"
        Date_record += str(record_[1]) + "\n"
        Description_record +=  str(record_[2]) + "\n"
        Price_record += str(record_[3]) + "\n"
        Category_record +=  str(record_[4]) + "\n"
        Status_record +=  str(record_[5]) + "\n"
        
    #Creates Lables to display the informationm of all the invenotries
    ID_records_label = Label(display_inventory_frame, text = ID_record, bg = '#ffffff', width = 12)
    ID_records_label.grid(row = 4, column = 1)
    
    Date_records_label = Label(display_inventory_frame, text = Date_record, bg = '#ffffff', width = 12)
    Date_records_label.grid(row = 4 , column = 2)

    Description_records_label = Label(display_inventory_frame, text = Description_record, bg = '#ffffff', width = 12)
    Description_records_label.grid(row = 4 , column = 3)

    Price_records_label = Label(display_inventory_frame, text = Price_record, bg = '#ffffff', width = 12)
    Price_records_label.grid(row = 4 , column = 4)

    Category_records_label = Label(display_inventory_frame, text = Category_record, bg = '#ffffff', width = 12)
    Category_records_label.grid(row = 4 , column = 5)

    Status_records_label = Label(display_inventory_frame, text = Status_record, bg = '#ffffff',width = 12)
    Status_records_label.grid(row = 4 , column = 6)






    conn.commit()

# Function that opens a new widget when the user selects to update inventory
def Update_Inventories():

    
    global Updated_IDnumber
    global Edit_IDnumber
    global Edit_Date
    global Edit_Description
    global Edit_Price
    global Edit_Category
    global Edit_Status

    # Creates a new frame when the user selcted the sub menu to delete inventory
    update_inventory_frame= Frame(root, width= 650, height=300)
    update_inventory_frame['background'] = '#c5d2d7'
    update_inventory_frame.grid(row=2, column=0)
    update_inventory_frame.grid_propagate(False)

    Label(update_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 1)
    Label(update_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 2)
    

    # Label to tell the user to insert the ID of the inventory that they want to update the inforamtion of
    Label(update_inventory_frame, text = 'Enter Exsisting ID number', bg = '#f6f8f9', width=24).grid(row = 3, column = 1)

    #Entry for the user to input the ID of the inventory they want to update
    Updated_IDnumber = ttk.Entry(update_inventory_frame, width = 24)
    Updated_IDnumber.grid(row = 3, column = 2)

    #Button to search the information of the inventory that the user inputted the ID of and insert it into the entries
    ttk.Button(update_inventory_frame, text = 'Search Inventory', command= update).grid(row= 4, column=3)

    #Labels to create space between the button and the labels
    Label(update_inventory_frame, bg = '#c5d2d7').grid(row = 4, column = 1)
    Label(update_inventory_frame, bg = '#c5d2d7').grid(row = 5, column = 1)
    Label(update_inventory_frame, bg = '#c5d2d7').grid(row = 4, column = 2)
    Label(update_inventory_frame, bg = '#c5d2d7').grid(row = 5, column = 2)

    # Lables to tell the user which information belongs to which field after the information has been displayed of the specific inventory 
    Label(update_inventory_frame, text = 'Entry ID number', bg = '#f6f8f9', width=24).grid(row = 6, column = 1)
    Label(update_inventory_frame, text = 'Date of entry:', bg = '#f6f8f9', width=24).grid(row = 7, column = 1)
    Label(update_inventory_frame, text = 'Item Description', bg = '#f6f8f9', width=24).grid(row = 8, column = 1)
    Label(update_inventory_frame, text = 'Price', bg = '#f6f8f9', width=24).grid(row = 9, column = 1 )
    Label(update_inventory_frame, text = 'Category', bg = '#f6f8f9', width=24).grid(row = 10, column = 1 )
    Label(update_inventory_frame, text = 'Status', bg = '#f6f8f9', width=24).grid(row = 11, column = 1 )
    
    # Entries that will display the current information of the inventory that has been saved in to the databse
    # The user will be able to edit the data in the entries if they want to update any of the information
    Edit_IDnumber = ttk.Entry(update_inventory_frame,  width = 28)
    Edit_Date = ttk.Entry(update_inventory_frame,  width = 28)
    Edit_Description = ttk.Entry(update_inventory_frame, width = 28)
    Edit_Price = ttk.Entry(update_inventory_frame, width = 28)
    Edit_Category = ttk.Combobox(update_inventory_frame, width = 25) 
    Edit_Category['values'] = ('Furniture', ' Technology',' Music')
    Edit_Status = ttk.Combobox(update_inventory_frame, width = 25) 
    Edit_Status['values'] = ('Sale', 'Reserved',' Sold')

    
    # Telling the program where to put the 6 entries that will contain the information
    Edit_IDnumber.grid(row = 6, column = 2)
    Edit_Date.grid(row = 7, column = 2)
    Edit_Description.grid(row = 8, column = 2)
    Edit_Price.grid(row = 9, column = 2)
    Edit_Category.grid(row = 10, column = 2)
    Edit_Status.grid(row = 11, column = 2)

    
    # Button that will save the information of the inventory after the user finished updating
    ttk.Button(update_inventory_frame, text = 'Save Inventory', command= update_save).grid(row= 12, column=3)
    
    
# Function that displays the data of the inventory that the user wants to updates when user presses the button
def update():

    global record_oid
    
    #Connects to the database that stores the information of inventories
    conn = sqlite3.connect('Cave_Gallery_Inventory.db')
    c=conn.cursor()
    update_record_id= Updated_IDnumber.get()
    record_oid=' '
    
    # Selects all the information that belongs to the inventory ID that the user inputted in the that they want to update
    c.execute("SELECT *, oid FROM Cave_Gallery_Inventories WHERE IDnumber = " + update_record_id)
    records = c.fetchall()


    #Loop through the records
    for record_ in records:
        #Inserts the data of the inventory from the Cave_Gallery_Inventories database that user inputted the ID of into the entries after the button has been pressed
        Edit_IDnumber.insert(0, record_[0])
        Edit_Date.insert(0, record_[1])
        Edit_Description.insert(0, record_[2])
        Edit_Price.insert(0, record_[3])
        Edit_Category.insert(0, record_[4]) 
        Edit_Status.insert(0, record_[5])
        record_oid += str(record_[6])

    conn.commit()
    
# Function that saves the updated data after the user presses the button 
def update_save():

    #Connects to the database that stores the information of inventories
    conn = sqlite3.connect('Cave_Gallery_Inventory.db')
    c=conn.cursor()

    update_record_id= Updated_IDnumber.get()

    #Updates the new data that has been inserted in the entries by the user into the Cave_Gallery_Inventories database
    c.execute("""UPDATE Cave_Gallery_Inventories SET
        IDnumber = :ID,
        Date = :Date,
        Description= :Description,
        Price = :Price,
        Category = :Category,
        Status = :Status

        WHERE oid = :oid""",
        {
        'ID': Edit_IDnumber.get(),
        'Date': Edit_Date.get(),
        'Description': Edit_Description.get(),
        'Price': Edit_Price.get(),
        'Category': Edit_Category.get(),
        'Status': Edit_Status.get(),
        'oid': record_oid

        })

    
    # Deletes the text that was inputted into the 6 entries after the new data has be inputted into the database

    Edit_IDnumber.delete(0, 'end')
    Edit_IDnumber.delete(0, 'end')
    Edit_Date.delete(0, 'end')
    Edit_Description.delete(0, 'end')
    Edit_Price.delete(0, 'end')
    Edit_Category.delete(0, 'end')
    Edit_Status.delete(0, 'end')

    # Message Box that will display that the data that was inserted has been updated
    messagebox.showinfo(title = "Confirmation", message = "Inventory has been updated")
    
    conn.commit()

    
# Function that opens a new widget when the user selects to delete inventory
def Delete_Inventories():

    global Delete_IDnumber_record
    global Delete_IDnumber
    global Delete_Date
    global Delete_Description
    global Delete_Price
    global Delete_Category
    global Delete_Status

    # Creates a new frame when the user selcted the sub menu to delete inventory
    delete_inventory_frame= Frame(root, width= 650, height=300)
    delete_inventory_frame['background'] = '#c5d2d7'
    delete_inventory_frame.grid(row=2, column=0)
    delete_inventory_frame.grid_propagate(False)


    Label(delete_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 1)
    Label(delete_inventory_frame, bg = '#c5d2d7').grid(row = 2, column = 2)

    # Label to tell the user to insert the ID of the inventory that they want to delete the inforamtion of
    Label(delete_inventory_frame, text = 'Enter Exsisting Inventory ID number', bg = '#f6f8f9', width=28).grid(row = 3, column = 1)

    #Entry for the user to input the ID of the inventory they want to delete
    Delete_IDnumber_record = ttk.Entry(delete_inventory_frame, width = 24)
    Delete_IDnumber_record.grid(row = 3, column = 2)
    
    #Button to search the information of the inventory that the user inputted the ID of and insert it into the entries
    ttk.Button(delete_inventory_frame, text = 'Search Inventory', command= delete).grid(row= 4, column=3)

    Label(delete_inventory_frame, bg = '#c5d2d7').grid(row = 4, column = 1)
    Label(delete_inventory_frame, bg = '#c5d2d7').grid(row = 5, column = 1)
    Label(delete_inventory_frame, bg = '#c5d2d7').grid(row = 4, column = 2)
    Label(delete_inventory_frame, bg = '#c5d2d7').grid(row = 5, column = 2)

    # Lables to tell the user which information belongs to which field after the information has been displayed of the specific inventory 
    Label(delete_inventory_frame, text = 'Entry ID number', bg = '#f6f8f9', width=24).grid(row = 6, column = 1)
    Label(delete_inventory_frame, text = 'Date of entry:', bg = '#f6f8f9', width=24).grid(row = 7, column = 1)
    Label(delete_inventory_frame, text = 'Item Description', bg = '#f6f8f9', width=24).grid(row = 8, column = 1)
    Label(delete_inventory_frame, text = 'Price', bg = '#f6f8f9', width=24).grid(row = 9, column = 1 )
    Label(delete_inventory_frame, text = 'Category', bg = '#f6f8f9', width=24).grid(row = 10, column = 1 )
    Label(delete_inventory_frame, text = 'Status', bg = '#f6f8f9', width=24).grid(row = 11, column = 1 )
    
    # Entries that will display the current information of the inventory that has been saved in to the databse
    # The user will be able to make sure that its the correct inventory they want to delete 
    Delete_IDnumber = ttk.Entry(delete_inventory_frame,  width = 28)
    Delete_Date = ttk.Entry(delete_inventory_frame,  width = 28)
    Delete_Description = ttk.Entry(delete_inventory_frame, width = 28)
    Delete_Price = ttk.Entry(delete_inventory_frame, width = 28)
    Delete_Category = ttk.Entry(delete_inventory_frame, width = 28) 
    Delete_Status = ttk.Entry(delete_inventory_frame, width = 28) 


    
    # Telling the program where to put the 6 entries that will contain the information
    Delete_IDnumber.grid(row = 6, column = 2)
    Delete_Date.grid(row = 7, column = 2)
    Delete_Description.grid(row = 8, column = 2)
    Delete_Price.grid(row = 9, column = 2)
    Delete_Category.grid(row = 10, column = 2)
    Delete_Status.grid(row = 11, column = 2)

    # Button that will delete the information of the inventory that has been chosen by the user
    ttk.Button(delete_inventory_frame, text = 'Delete Inventory', command= delete_save).grid(row= 12, column=3)


# Function that displays the data of the inventory that the user wants to delete when user presses the button
def delete():


    # Connects to the database that stores the information of inventories
    conn = sqlite3.connect('Cave_Gallery_Inventory.db')
    c=conn.cursor()
    delete_record_id= Delete_IDnumber_record.get()
    
    # Selects all the information that belongs to the inventory ID that the user inputted in the that they want to delete
    c.execute("SELECT * FROM Cave_Gallery_Inventories WHERE IDnumber = " + delete_record_id)
    records = c.fetchall()


    #Inserts the data of the inventory that user inputted the ID of into the entries after the button was pressed
    for record_ in records:
        Delete_IDnumber.insert(0, record_[0])
        Delete_Date.insert(0, record_[1])
        Delete_Description.insert(0, record_[2])
        Delete_Price.insert(0, record_[3])
        Delete_Category.insert(0, record_[4]) 
        Delete_Status.insert(0, record_[5])

# Function that deletes the data of inventory that the user selected when the user presses the button
def delete_save():


    #Connects to the database that stores the information of inventories
    conn = sqlite3.connect('Cave_Gallery_Inventory.db')
    c=conn.cursor()

    #Deletes the data of the inventory that has been chosen by the user from the Cave_Gallery_Inventories database after the button has been pressed
    c.execute("DELETE from Cave_Gallery_Inventories WHERE IDnumber= " + Delete_IDnumber_record.get())

    # Deletes the text that was inputted into the 6 entries after the data of the ivnventory has been deleted form the Cave_Gallery_Inventories database
    Delete_IDnumber_record.delete(0, END)
    Delete_IDnumber.delete(0, END)
    Delete_Date.delete(0, END)
    Delete_Description.delete(0, END)
    Delete_Price.delete(0, END)
    Delete_Category.delete(0, END)
    Delete_Status.delete(0, END)

    # Message Box that will display that the data has been deleted from the database
    messagebox.showinfo(title = "Confirmation", message = "Inventory has been deleted")

    conn.commit()



#Creates the widget of the menu
menubar = Menu(root)
root.config(menu=menubar)

#Creates a menu bar for adding inventory into the database
createMenu = Menu(menubar)
menubar.add_cascade(label="Create", menu=createMenu)
#Creates a sub menu that the user can select which will bring the user into a different frame to add inventory
createMenu.add_command(label="Add Inventory", command=Add_Inventory)
createMenu.add_command(label="Exit", command=root.quit)

#Creates a menu bar for displaying inventory into the database
displayMenu  = Menu(menubar)
menubar.add_cascade(label="Display", menu=displayMenu)
#Creates a sub menu that the user can select which will bring the user into a different frame to display inventory
displayMenu.add_command(label="Display Inventories", command=Display_Inventories)
displayMenu.add_command(label="Exit", command=root.quit)

#Creates a menu bar for updating the inventory into the database
updateMenu  = Menu(menubar)
menubar.add_cascade(label="Update", menu=updateMenu)
#Creates a sub menu that the user can select which will bring the user into a different frame update inventory
updateMenu.add_command(label="Update Inventories", command=Update_Inventories)
updateMenu.add_command(label="Exit", command=root.quit)

#Creates a menu bar for deleting inventory into the database
deleteMenu  = Menu(menubar)
menubar.add_cascade(label="Delete", menu=deleteMenu)
#Creates a sub menu that the user can select which will bring the user into a different frame to delete inventory
deleteMenu.add_command(label="Delete Inventory", command=Delete_Inventories)
deleteMenu.add_command(label="Exit", command=root.quit)


# Frame for the header 
header_frame= Frame(root, width= 650, height=100)
# Colour of the background of the header
header_frame['background'] = '#70909c'
#Placement of the header
header_frame.grid(row=1, column=0)
#Stops the frame from shrinkings
header_frame.grid_propagate(False)


#Taking the image of the file that contains the logo and inserts into the program
logo = PhotoImage(file = 'logo.png')
Logo_label= Label(header_frame, image = logo)
#Placement of the logo
Logo_label.pack(side=RIGHT)
Logo_label.grid(row= 1, column = 1, rowspan=2,padx=160, pady=10)
# Colour of the background of the logo
Logo_label['background'] = '#70909c'

#Taking the image of the file that contains the title and inserts into the program
Title = PhotoImage(file = 'Title.png')
Title_label= Label(header_frame, image = Title)
#Placement of the title
Title_label.pack(side=LEFT)
Title_label.grid(row= 1, column = 0, rowspan=2)
#Colour of the background of the title
Title_label['background'] = '#70909c'


#Frame of the body that will contain lables and entries
body_frame= Frame(root, width= 650, height=300)
# Colour of the background of the header
body_frame['background'] = '#c5d2d7'
# Placement of the body
body_frame.grid(row=2, column=0)
#Stops the frame from shrinkings
body_frame.grid_propagate(False)










        

        
conn.commit()
root.mainloop()
