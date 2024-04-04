#Importing mysql connector into the code
import mysql.connector
from mysql.connector import errors
import tkinter as tk

#Connecting to the inventory system database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Peterguchman@101",
    database="Inventory_Management_System"

)

mycursor = db.cursor()


#Code for creating the Inventory management system's database
#mycursor.execute("CREATE DATABASE Inventory_Management_System")

#Code for creating Products table
#mycursor.execute("CREATE TABLE Products("
                # "Product_ID int PRIMARY KEY AUTO_INCREMENT,"
                 #"Product_Name VARCHAR(255) NOT NULL,"
                 #"Product_Quantity int NOT NULL)")


#code for creating user table
#mycursor.execute("CREATE TABLE Users("
                 #"User_ID int PRIMARY KEY AUTO_INCREMENT,"
                 #"User_Name VARCHAR(255) NOT NULL,"
                 #"User_email VARCHAR(255) NOT NULL)")


# code for creating Purchase management table
#mycursor.execute("CREATE TABLE Purchase("
                 #"Purchase_ID int PRIMARY KEY AUTO_INCREMENT,"
                 #"Buyer_ID int NOT NULL,"
                 #"FOREIGN KEY (Buyer_ID) REFERENCES Users(USER_ID),"
                 #"Buyer VARCHAR(255) NOT NULL,"
                 #"Product_Name VARCHAR (255) NOT NULL,"
                 #"Amount_Bought int NOT NULL)")


#code for creating sales management table
#mycursor.execute("CREATE TABLE Sales("
                 #"Sale_ID int PRIMARY KEY AUTO_INCREMENT,"
                 #"Product_ID int NOT NULL,"
                 #"FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID),"
                 #"Product_Name VARCHAR (255) NOT NULL,"
                 #"Amount_Sold int NOT NULL,"
                 #"Amount_Remaining int NOT NULL)")
#function to add a product
def add_product():
    product_name = entry_product_name.get()
    quantity = entry_quantity.get()

    add_product_query = "INSERT INTO product (product_name, quantity) VALUES (%s, %s)"
    data_product = (product_name, quantity)

    mycursor.execute(add_product_query, data_product)
    db.commit()

    # Clear the input fields
    entry_product_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)

# Function to update a product
def update_product():
    product_id = entry_product_id.get()
    product_name = entry_product_name.get()
    quantity = entry_quantity.get()

    update_product_query = "UPDATE product SET product_name=%s, quantity=%s WHERE product_id=%s"
    data_product = (product_name, quantity, product_id)

    mycursor.execute(update_product_query, data_product)
    db.commit()

    # Clear the input fields
    entry_product_id.delete(0, tk.END)
    entry_product_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)

# Function to delete a product
def delete_product():
    product_id = entry_product_id.get()

    delete_product_query = "DELETE FROM product WHERE product_id=%s"
    data_product = (product_id,)

    mycursor.execute(delete_product_query, data_product)
    db.commit()

    # Clear the input field
    entry_product_id.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Product Management")

# Create input fields and labels
entry_product_id = tk.Entry(window)
entry_product_id.grid(row=0, column=1)
entry_product_name = tk.Entry(window)
entry_product_name.grid(row=1, column=1)
entry_quantity = tk.Entry(window)
entry_quantity.grid(row=2, column=1)

# Create labels for input fields
tk.Label(window, text="Product ID").grid(row=0, column=0)
tk.Label(window, text="Product Name").grid(row=1, column=0)
tk.Label(window, text="Quantity").grid(row=2, column=0)

# Create buttons
add_product_button = tk.Button(window, text="Add Product", command=add_product)
add_product_button.grid(row=3, column=0)
update_product_button = tk.Button(window, text="Update Product", command=update_product)
update_product_button.grid(row=3, column=1)
delete_product_button = tk.Button(window, text="Delete Product", command=delete_product)
delete_product_button.grid(row=3, column=2)


#function to add users
def add_user():
    user_name = entry_user_name.get()
    email = entry_email.get()

    add_user_query = "INSERT INTO Users (User_Name, User_email) VALUES (%s, %s)"
    data_user = (user_name, email)

    mycursor.execute(add_user_query, data_user)
    db.commit()

    # Clear the input fields
    entry_user_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Function to update users
def update_user():
    user_id = entry_user_id.get()
    user_name = entry_user_name.get()
    email = entry_email.get()

    update_user_query = "UPDATE Users SET User_Name=%s, User_email=%s WHERE User_ID=%s"
    data_user = (user_name, email, user_id)

    mycursor.execute(update_user_query, data_user)
    db.commit()

    # Clear the input fields
    entry_user_id.delete(0, tk.END)
    entry_user_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Function to delete a user
def delete_user():
    user_id = entry_user_id.get()

    delete_user_query = "DELETE FROM Users WHERE User_ID=%s"
    data_user = (user_id,)

    mycursor.execute(delete_user_query, data_user)
    db.commit()

    # Clear the input field
    entry_user_id.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("User Management")

# Create input fields and labels
entry_user_id = tk.Entry(window)
entry_user_id.grid(row=0, column=1)
entry_user_name = tk.Entry(window)
entry_user_name.grid(row=1, column=1)
entry_email = tk.Entry(window)
entry_email.grid(row=2, column=1)

# Create labels for input fields
tk.Label(window, text="User ID").grid(row=0, column=0)
tk.Label(window, text="User Name").grid(row=1, column=0)
tk.Label(window, text="Email").grid(row=2, column=0)

# Create buttons
add_product_button = tk.Button(window, text="Add user", command=add_user)
add_product_button.grid(row=3, column=0)
update_product_button = tk.Button(window, text="Update user", command=update_user)
update_product_button.grid(row=3, column=1)
delete_product_button = tk.Button(window, text="Delete user", command=delete_user)
delete_product_button.grid(row=3, column=2)


# Function to add an item to the database
def add_item(conn, c):
    item = entry_item.get()
    quantity = int(entry_quantity.get())
    c.execute("INSERT INTO Products (Product_Name, Quantity) VALUES (%s, %s)", (item, quantity))
    conn.commit()
    entry_item.delete(0, 'end')
    entry_quantity.delete(0, 'end')


# Function to delete an item from the database
def delete_item(conn, c, item):
    item = entry_item.get()
    quantity = int(entry_quantity.get())
    cid = get_product_id(conn, c, item)
    if cid:
        c.execute("SELECT quantity FROM Products WHERE Product_Name=%s AND Product_ID=%s", (item, cid))
        result = c.fetchone()
        if result:
            current_quantity = result[0]
            if current_quantity >= quantity:
                c.execute("UPDATE Products SET Quantity=Quantity-%s WHERE Product_Name=%s AND Product_ID=%s",
                          (quantity, item, cid))
                conn.commit()
                remaining_quantity = current_quantity - quantity
                return remaining_quantity
            else:
                print("Error: Insufficient quantity to delete.")
        else:
            print("Error: Product not found.")
    else:
        print("Error: Product ID not found.")
    entry_item.delete(0, 'end')
    entry_quantity.delete(0, 'end')


# Function to update the quantity of an item in the database
def update_item(conn, c):
    item = entry_item.get()
    quantity = int(entry_quantity.get())
    cid = get_product_id(conn, c, item)
    if cid:
        c.execute("UPDATE Products SET Quantity=%s WHERE Product_ID=%s", (quantity, cid))
        conn.commit()
    entry_item.delete(0, 'end')
    entry_quantity.delete(0, 'end')


# Function to get the product id from the database
def get_product_id(conn, c, product_name):
    c.execute("SELECT Product_ID FROM Products WHERE Product_Name=%s", (product_name,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        return None


# Create the main window
root = tk.Tk()

# Create a connection and a cursor
conn = db
c = conn.cursor()

# Create the table
#create_table(conn, c)

# Create labels and entry fields for the item and quantity
label_item = tk.Label(root, text='Product Name')
label_item.pack()
entry_item = tk.Entry(root)
entry_item.pack()
label_quantity = tk.Label(root, text='Quantity')
label_quantity.pack()
entry_quantity = tk.Entry(root)
entry_quantity.pack()

# Create labels and entry fields for the product id
label_product_id = tk.Label(root, text='Product ID')
label_product_id.pack()
entry_product_id = tk.Entry(root)
entry_product_id.pack()

# Create buttons to add, delete, and update items
button_add = tk.Button(root, text='Add', command=lambda: add_item(conn, c))
button_add.pack()
button_delete = tk.Button(root, text='Delete', command=lambda: delete_item(conn, c, entry_item.get()))
button_delete.pack()
button_update = tk.Button(root, text='Update', command=lambda: update_item(conn, c))
button_update.pack()

# Run the main loop
window.mainloop()

# Close the database connection
mycursor.close()
db.close()